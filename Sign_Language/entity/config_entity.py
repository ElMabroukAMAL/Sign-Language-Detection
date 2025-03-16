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



#inside the artifacts_dir it will create the data ingestion and feature folder   
@dataclass
class DataIngestionConfig:
    data_ingestion_dir: str = os.path.join(
        training_pipeline_config.artifacts_dir, DATA_INGESTION_DIR_NAME
    )

    feature_store_file_path: str = os.path.join(
        data_ingestion_dir, DATA_INGESTION_FEATURE_STORE_DIR
    )

    data_download_url: str = DATA_DOWNLOAD_URL




