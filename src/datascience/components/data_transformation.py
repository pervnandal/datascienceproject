import os
from src.datascience import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from src.datascience.entity.config_entity import (DataTransformationConfig)

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config=config

    def train_test_spliting(self):
        data=pd.read_csv(self.config.data_dir)
        
        # Data Spliting into train and test sets(0.75,0.25)
        train,test=train_test_split(data)
        
        train.to_csv(os.path.join(self.config.root_dir,"train.csv"),index= False)
        train.to_csv(os.path.join(self.config.root_dir,"test.csv"),index= False)
        
        logger.info("Splitted data into training and test sets")
        logger.info(f"Train set shape:{train.shape}")
        logger.info(f"Test set shape:{test.shape}")
        
        print(f"Train set shape:{train.shape}")
        print(f"Test set shape:{test.shape}")