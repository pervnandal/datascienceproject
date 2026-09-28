from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir:Path
    source_URL: str
    local_data_file: Path
    unzip_dir:Path


@dataclass
class DataValiationConfig:
    root_dir:Path
    unzip_data_dir:Path
    STATUS_FILE:str
    all_schema:dict

@dataclass
class DataTransformationConfig:
    root_dir:Path
    data_dir:Path

@dataclass
class ModelTrainerConfig:
    root_dir: Path
    train_dir: Path
    test_dir: Path
    model_name: str
    alpha:float
    l1_ratio:float
    target_column:str

