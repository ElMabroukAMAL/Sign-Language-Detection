#ingest data from github and unzip it
import os
import sys
from six.moves import urllib # to download files from internet
import zipfile # to unzip data
from Sign_Language.logger import logging
from Sign_Language.exception import SignException
from Sign_Language.entity.config_entity import DataIngestionConfig
from Sign_Language.entity.artifact_entity import DataIngestionArtifact



class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig = DataIngestionConfig()):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
           raise SignException(e, sys)
        
    

    def download_data(self) -> str:
        """
        Fetch data from the specified URL.
        Returns the path of the downloaded zip file.
        """
        try:
            dataset_url = self.data_ingestion_config.data_download_url  # Get dataset URL from config
            zip_download_dir = self.data_ingestion_config.data_ingestion_dir  # Directory to store the zip file
            os.makedirs(zip_download_dir, exist_ok=True)  # Create directory if it doesn't exist
            data_file_name = os.path.basename(dataset_url)  # Extract file name from URL
            zip_file_path = os.path.join(zip_download_dir, data_file_name)  # Define full path for zip file

            logging.info(f"Downloading data from {dataset_url} into file {zip_file_path}")
            urllib.request.urlretrieve(dataset_url, zip_file_path)  # Download the file
            logging.info(f"Downloaded data from {dataset_url} into file {zip_file_path}")

            return zip_file_path  # Return the path of the downloaded file

        except Exception as e:
            raise SignException(e, sys) 
        

    

    def extract_zip_file(self, zip_file_path: str) -> str:
        """
        Extracts the zip file into the data directory.
        Returns the path of the extracted files.
        """
        try:
            feature_store_path = self.data_ingestion_config.feature_store_file_path  # Get the extraction directory
            os.makedirs(feature_store_path, exist_ok=True)  # Create directory if it doesn't exist

            # Open and extract the zip file
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(feature_store_path)

            logging.info(f"Extracting zip file: {zip_file_path} into dir: {feature_store_path}")

            return feature_store_path  # Return the path where the files were extracted

        except Exception as e:
            raise SignException(e, sys)
        


    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        """
        Calls the methods one by one: download the data, then extract it.
        Returns a DataIngestionArtifact containing the paths of the zip file and extracted data.
        """
        logging.info("Entered initiate_data_ingestion method of Data_Ingestion class")
        try:
            zip_file_path = self.download_data()  # Download the dataset
            feature_store_path = self.extract_zip_file(zip_file_path)  # Extract the dataset

            # Create an artifact to store the paths of the downloaded and extracted files
            data_ingestion_artifact = DataIngestionArtifact(
                data_zip_file_path=zip_file_path,
                feature_store_path=feature_store_path
            )

            logging.info("Exited initiate_data_ingestion method of Data_Ingestion class")
            logging.info(f"Data ingestion artifact: {data_ingestion_artifact}")

            return data_ingestion_artifact  # Return the artifact

        except Exception as e:
            raise SignException(e, sys)