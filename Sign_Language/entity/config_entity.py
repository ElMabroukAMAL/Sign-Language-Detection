import os
from dataclasses import dataclass
from datetime import datetime
from Sign_Language.constant.training_pipeline import *

#create TIMESTAMP folder inside the ARTIFACTS_DIR to save each execution
TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

#we use class decorator to access to the variables defined in the class from other files
@dataclass
class TrainingPipelineConfig:
    artifacts_dir: str = os.path.join(ARTIFACTS_DIR,TIMESTAMP)

#initialize the class and return it as object
training_pipeline_config:TrainingPipelineConfig = TrainingPipelineConfig() 



#in the artifacts_dir it will create the data ingestion folder
@dataclass
class DataIngestionConfig:
    data_ingestion_dir: str = os.path.join(
        training_pipeline_config.artifacts_dir, DATA_INGESTION_DIR_NAME
    )

    feature_store_file_path: str = os.path.join(
        data_ingestion_dir, DATA_INGESTION_FEATURE_STORE_DIR
    )

    data_download_url: str = DATA_DOWNLOAD_URL


##in the artifacts_dir it will create the data validation folder
@dataclass
class DataValidationConfig:
    data_validation_dir: str = os.path.join(
        training_pipeline_config.artifacts_dir, DATA_VALIDATION_DIR_NAME
    )

    valid_status_file_dir: str = os.path.join(data_validation_dir, DATA_VALIDATION_STATUS_FILE)

    required_file_list = DATA_VALIDATION_ALL_REQUIRED_FILES


#in the artifacts_dir it will create the model trainer folder
@dataclass
class ModelTrainerConfig:
    model_trainer_dir: str = os.path.join(
        training_pipeline_config.artifacts_dir, MODEL_TRAINER_DIR_NAME
    )

    weight_name = MODEL_TRAINER_PRETRAINED_WEIGHT_NAME

    no_epochs = MODEL_TRAINER_NO_EPOCHS

    batch_size = MODEL_TRAINER_BATCH_SIZE