# Flow of the execution

import sys, os
from Sign_Language.logger import logging
from Sign_Language.exception import SignException
from Sign_Language.components.data_ingestion import DataIngestion
from Sign_Language.components.data_validation import DataValidation
from Sign_Language.components.model_trainer import ModelTrainer
from Sign_Language.entity.config_entity import (DataIngestionConfig, DataValidationConfig, ModelTrainerConfig)
from Sign_Language.entity.artifact_entity import (DataIngestionArtifact, DataValidationArtifact, ModelTrainerArtifact)


class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_validation_config = DataValidationConfig()
        self.model_trainer_config = ModelTrainerConfig()


    def start_data_ingestion(self)-> DataIngestionArtifact:
        try:
            logging.info("Entered the start_data_ingestion method of TrainPipeline class")
            logging.info("Getting the data from URL")

            # Create an instance of DataIngestion with the configured settings
            data_ingestion = DataIngestion(
                data_ingestion_config=self.data_ingestion_config
            )
            # Start the data ingestion process
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()

            logging.info("Got the data from URL")
            logging.info("Exited the start_data_ingestion method of TrainPipeline class")

            return data_ingestion_artifact  # Return the ingestion artifact

        except Exception as e:
            raise SignException(e, sys)
        

    def start_data_validation( self, data_ingestion_artifact: DataIngestionArtifact) -> DataValidationArtifact:
        logging.info("Entered the start_data_validation method of TrainPipeline class")
        try:
            data_validation = DataValidation(
                data_ingestion_artifact=data_ingestion_artifact,
                data_validation_config=self.data_validation_config,
            )

            data_validation_artifact = data_validation.initiate_data_validation()

            logging.info("Performed the data validation operation")
            logging.info("Exited the start_data_validation method of TrainPipeline class")

            return data_validation_artifact

        except Exception as e:
            raise SignException(e, sys)
        


    def start_model_trainer(self) -> ModelTrainerArtifact:
        try:
            model_trainer = ModelTrainer(
                model_trainer_config=self.model_trainer_config,
            )
            model_trainer_artifact = model_trainer.initiate_model_trainer()
            
            return model_trainer_artifact

        except Exception as e:
            raise SignException(e, sys)
        


    def run_pipeline(self) -> None:
        """
        Run the training pipeline
        """
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(
                data_ingestion_artifact=data_ingestion_artifact
            )
            if data_validation_artifact.validation_status == True:
                model_trainer_artifact = self.start_model_trainer()
            else:
                raise Exception("Your data is not in correct format")

        except Exception as e:
            raise SignException(e, sys)   