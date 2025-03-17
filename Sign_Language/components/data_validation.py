import os, sys
import shutil
from Sign_Language.logger import logging
from Sign_Language.exception import SignException
from Sign_Language.entity.config_entity import DataValidationConfig
from Sign_Language.entity.artifact_entity import (DataIngestionArtifact, DataValidationArtifact)


class DataValidation:
    def __init__(
        self,
        data_ingestion_artifact: DataIngestionArtifact,
        data_validation_config: DataValidationConfig,
    ):
        try:
            self.data_ingestion_artifact = data_ingestion_artifact  # Storing the data ingestion artifact
            self.data_validation_config = data_validation_config  # Storing the validation configuration

        except Exception as e:
            raise SignException(e, sys) 
        

    
    def validate_all_files_exist(self) -> bool:
        """
        Checks if all required files are present in the dataset directory.

        Returns:
        - bool: True if all required files exist, otherwise False.
        """
        try:
            validation_status = None  # Initializing validation status
            all_files = os.listdir(self.data_ingestion_artifact.feature_store_path)  # Listing all files in the feature store directory

            # Checking if all required files exist in the dataset
            for file in all_files:
                if file not in self.data_validation_config.required_file_list:  # If a required file is missing
                    validation_status = False 
                    os.makedirs(self.data_validation_config.data_validation_dir, exist_ok=True)  # Create validation directory if it doesn't exist
                    with open(self.data_validation_config.valid_status_file_dir, 'w') as f:
                        f.write(f"Validation status: {validation_status}")  # Save validation status to a file

                else:
                    validation_status = True 
                    os.makedirs(self.data_validation_config.data_validation_dir, exist_ok=True)  
                    with open(self.data_validation_config.valid_status_file_dir, 'w') as f:
                        f.write(f"Validation status: {validation_status}") 
            
            return validation_status 

        except Exception as e:
            raise SignException(e, sys)  
        

    
    def initiate_data_validation(self) -> DataValidationArtifact: 
        """
        Initiates the data validation process and returns a validation artifact.

        Returns:
        - DataValidationArtifact: An artifact containing the validation status.
        """
        logging.info("Entered initiate_data_validation method of DataValidation class")  # Logging method entry
        try:
            status = self.validate_all_files_exist()  
            data_validation_artifact = DataValidationArtifact(
                validation_status=status)  # Creating a validation artifact with the result

            logging.info("Exited initiate_data_validation method of DataValidation class")  
            logging.info(f"Data validation artifact: {data_validation_artifact}")  

            # If validation is successful, copy the data zip file to the principal directory for model trainer
            if status:
                shutil.copy(self.data_ingestion_artifact.data_zip_file_path, os.getcwd())

            return data_validation_artifact  

        except Exception as e:
            raise SignException(e, sys)