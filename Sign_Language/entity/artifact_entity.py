from dataclasses import dataclass

#return the paths for the next components 
@dataclass
class DataIngestionArtifact:
    data_zip_file_path:str
    feature_store_path:str