from src.utils.all_utils import read_yaml,create_directory,log
import argparse
import pandas as pd
import os

log_file = open("Logs\logs.txt", 'a+')
def get_data(config_path):
    try:
        
        config = read_yaml(config_path)
        remote_data_path = config["data_source"]
        df = pd.read_csv(remote_data_path,sep=",")
        log(log_file,f"sucessfully fetch data from {remote_data_path}") 
        artifacts_dir = config["artifacts"]['artifacts_dir']
        raw_local_dir = config["artifacts"]['raw_local_dir']
        raw_local_file = config["artifacts"]['raw_local_file'] 
        raw_local_dir_path = os.path.join(artifacts_dir, raw_local_dir)
        raw_local_file_path = os.path.join(raw_local_dir_path, raw_local_file)
        create_directory(dirs= [raw_local_dir_path])
        log(log_file,f"directory created at {raw_local_dir_path}")
        df.to_csv(raw_local_file_path, sep=",", index=False)
        log(log_file,f"data saved at {raw_local_file_path}")

    except Exception as e:
        log(log_file,str(e))
           


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="config/config.yaml")
    parsed_args = args.parse_args()
    get_data(config_path=parsed_args.config)