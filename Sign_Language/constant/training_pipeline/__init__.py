import os 

# Folder to save my data 
ARTIFACTS_DIR: str = "artifacts"

"""
Data Ingestion related constant"
"""
DATA_INGESTION_DIR_NAME: str = "data_ingestion" #inside it, download .rar file
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store" #doing the unrar operation
DATA_DOWNLOAD_URL: str = "https://github.com/ElMabroukAMAL/Sign-Language-Detection/raw/refs/heads/main/Data/Sign_Language_Data/Sign_Language_Data.zip"