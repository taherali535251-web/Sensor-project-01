import sys
import os
from src.components.data_ingestion import DataIngestion
from src.components.data_tranformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.exception import customException



class TrainingPipeline:

    def start_data_ingestion(self):
        try:
            data_ingestion = data_ingestion()
            feature_store_file_path = data_ingestion.initiate_data_ingestion()
            return feature_store_file_path
        except Exception as e:
            raise customException(e,sys)
        

    def start_data_transformation(self, feature_store_file_path):
        try:
            data_tranformation = DataTransformation(feature_store_file_path= feature_store_file_path)
            train_array, test_array, preprocessor_path = data_tranformation.initiate_data_tranformation
            return train_array,test_array,preprocessor_path
        except Exception as e:
            raise customException(e,sys)

    def start_model_training(self,train_array,test_array):
        try:
            model_trainer = ModelTrainer()
            model_score = model_trainer.initiate_model_trainer(
                train_array,test_array
            )
            return model_score
        except Exception as e:
            raise customException(e,sys)
        
    def run_pipeline(self):
        try:
            feature_store_file_path = self.start_data_ingestion()
            train_array,test_array,preprocessor_path = self.start_data_transformation(feature_store_file_path)
            r2_square = self.start_model_training(train_array,test_array)

            print("training completed. Trained modelscore:", r2_square)

        except Exception as e:
            raise customException(e,sys)


