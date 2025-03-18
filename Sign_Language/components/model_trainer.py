import os,sys
import yaml
from Sign_Language.utils.main_utils import read_yaml_file
from Sign_Language.logger import logging
from Sign_Language.exception import SignException
from Sign_Language.entity.config_entity import ModelTrainerConfig
from Sign_Language.entity.artifact_entity import ModelTrainerArtifact

class ModelTrainer:
    def __init__(
        self,
        model_trainer_config: ModelTrainerConfig,
    ):
        self.model_trainer_config = model_trainer_config

    
    def initiate_model_trainer(self,) -> ModelTrainerArtifact:
        logging.info("Entered initiate_model_trainer method of ModelTrainer class")

        try:
            #unzip the data
            logging.info("Unzipping data")
            os.system("unzip Sign_language_data.zip")
            os.system("rm Sign_language_data.zip")

            # Extract the number of classes parameter (nc) from the YAML configuration file
            with open("data.yaml", 'r') as stream:
                num_classes = str(yaml.safe_load(stream)['nc'])  # Reading number of classes from YAML file

            # Extract the model configuration file name (yolov5s)
            model_config_file_name = self.model_trainer_config.weight_name.split(".")[0]
            print(model_config_file_name)

            # Read the model configuration file
            config = read_yaml_file(f"yolov5/models/{model_config_file_name}.yaml")

            # Update the number of classes in the configuration file
            config['nc'] = int(num_classes)

            # Save the updated configuration to a new custom model file
            with open(f'yolov5/models/custom_{model_config_file_name}.yaml', 'w') as f:
                yaml.dump(config, f)

            # Train the YOLOv5 model using the specified configuration
            os.system(f"cd yolov5/ && python train.py --img 416 --batch {self.model_trainer_config.batch_size} --epochs {self.model_trainer_config.no_epochs} --data ../data.yaml --cfg ./models/custom_yolov5s.yaml --weights {self.model_trainer_config.weight_name} --name yolov5s_results  --cache")
            # Copy the best trained model to the working directory
            os.system("cp yolov5/runs/train/yolov5s_results/weights/best.pt yolov5/")
            # Create the model trainer directory
            os.makedirs(self.model_trainer_config.model_trainer_dir, exist_ok=True)
            # Copy the trained model to the model trainer directory
            os.system(f"cp yolov5/runs/train/yolov5s_results/weights/best.pt {self.model_trainer_config.model_trainer_dir}/")

            # Cleanup unnecessary files and directories
            os.system("rm -rf yolov5/runs") 
            os.system("rm -rf train")  
            os.system("rm -rf test")
            os.system("rm -rf data.yaml")  

            # Create an artifact object with the trained model's file path
            model_trainer_artifact = ModelTrainerArtifact(
                trained_model_file_path="yolov5/best.pt",
            )

            logging.info("Exited initiate_model_trainer method of ModelTrainer class") 
            logging.info(f"Model trainer artifact: {model_trainer_artifact}")  

            return model_trainer_artifact 

        except Exception as e:
            raise SignException(e, sys)