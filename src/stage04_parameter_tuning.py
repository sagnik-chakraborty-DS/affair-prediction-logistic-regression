from src.utils.all_utils import read_yaml,create_directory,save_local_df,log
import argparse
import pandas as pd
import os
from imblearn.over_sampling import RandomOverSampler

log_file = open("Logs\logs.txt", 'a+')

def parameter_tuning(clean_data_path):
    try:
        config = read_yaml(clean_data_path)
        artifacts_dir = config["artifacts"]['artifacts_dir']
        clean_data_dir = config["artifacts"]['clean_data_dir']
        clean_data = config["artifacts"]['clean_data']
        clean_data_file_path = os.path.join(artifacts_dir, clean_data_dir, clean_data)
        clean_data=pd.read_csv(clean_data_file_path)
        log(log_file,f"sucessfully read clean data from {clean_data_file_path}")
        print(clean_data.head)
    except Exception as e:
        log(log_file,str(e))


if __name__ == '__main__':
    args = argparse.ArgumentParser()

    args.add_argument("--config", "-c", default="config/config.yaml")
    
    parsed_args = args.parse_args()
    parameter_tuning(clean_data_path=parsed_args.config)