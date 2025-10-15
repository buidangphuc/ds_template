import os

import joblib
import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.linear_model import ElasticNet

from src.datascience.entity.config_entity import ModelTrainerConfig


class ModelTrainer:

    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        # test_data = pd.read_csv(self.config.test_data_path)

        train_x = train_data.drop([self.config.target_column], axis=1)
        # test_x = test_data.drop([self.config.target_column], axis=1)
        train_y = train_data[[self.config.target_column]]
        # test_y = test_data[[self.config.target_column]]

        lr = ElasticNet(
            alpha=self.config.alpha, l1_ratio=self.config.l1_ratio, random_state=42
        )
        with mlflow.start_run():
            mlflow.log_param("alpha", self.config.alpha)
            mlflow.log_param("l1_ratio", self.config.l1_ratio)
            mlflow.log_param("model_name", self.config.model_name)
            mlflow.log_param("target_column", self.config.target_column)
            lr.fit(train_x, train_y)

            joblib.dump(lr, os.path.join(self.config.root_dir, self.config.model_name))
            mlflow.sklearn.log_model(lr, "model")
