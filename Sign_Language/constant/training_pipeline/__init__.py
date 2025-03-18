import os 

# Folder to save my data 
ARTIFACTS_DIR: str = "artifacts"


"""
Data Ingestion related constant
"""
DATA_INGESTION_DIR_NAME: str = "data_ingestion" #inside it, download .zip file

DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store" #doing the unzip operation

#from Github
#DATA_DOWNLOAD_URL: str = "https://github.com/ElMabroukAMAL/Sign-Language-Detection/raw/refs/heads/main/Data/Sign_Language_Data/Sign_Language_Data.zip"

#from Google Drive
DATA_DOWNLOAD_URL: str = "https://drive.google.com/file/d/1SX8feD3A6GJbbeNtedNFJTFEd38acgqd/view?usp=sharing"


"""
Data Validation realted constant
"""
DATA_VALIDATION_DIR_NAME: str = "data_validation"

DATA_VALIDATION_STATUS_FILE = 'status.txt'

DATA_VALIDATION_ALL_REQUIRED_FILES = ["train", "test", "data.yaml"]


"""
MODEL TRAINER related constant 
"""
MODEL_TRAINER_DIR_NAME: str = "model_trainer"

MODEL_TRAINER_PRETRAINED_WEIGHT_NAME: str = "yolov5s.pt"

MODEL_TRAINER_NO_EPOCHS: int = 1

MODEL_TRAINER_BATCH_SIZE: int = 16