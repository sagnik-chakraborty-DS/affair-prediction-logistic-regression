from sklearn.metrics import classification_report
from src.utils.all_utils import log, read_yaml, create_directory,save_report
import argparse
import pandas as pd
import os
import joblib

log_file = open("Logs\logs.txt", 'a+')
def evaluate(config_path):
    try: 
        config = read_yaml(config_path)
        artifacts_dir = config["artifacts"]['artifacts_dir']
        split_data_dir = config["artifacts"]["split_data_dir"]
        test_data_filename = config["artifacts"]["test"]
        test_data_path = os.path.join(artifacts_dir, split_data_dir, test_data_filename)
        test_data = pd.read_csv(test_data_path)
        
        test_y = test_data["affair"]
        test_x = test_data.drop("affair", axis=1) 
        
        model_dir = config["artifacts"]["model_dir"]
        model_filename = config["artifacts"]["model_filename"]
        model_path = os.path.join(artifacts_dir, model_dir, model_filename)
        
        
        lr = joblib.load(model_path)
        
        predicted_values=lr.predict(test_x)
        
        scores=classification_report(test_y,predicted_values)
        
        
        scores_dir = config["artifacts"]["reports_dir"]
        
        scores_filename = config["artifacts"]["scores"]

        scores_dir_path = os.path.join(artifacts_dir, scores_dir)
        create_directory([scores_dir_path])
        
        scores_filepath = os.path.join(scores_dir_path, scores_filename)
        save_report(scores,scores_filepath)
        log(log_file,f"report saved at {scores_filepath}")
 
    except Exception as e:
        log(log_file,str(e))

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="config/config.yaml")
    parsed_args = args.parse_args()
    evaluate(config_path=parsed_args.config)    