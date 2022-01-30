from src.utils.all_utils import read_yaml,create_directory,save_local_df,log
import argparse
import pandas as pd
import os
from imblearn.over_sampling import RandomOverSampler

log_file = open("Logs\logs.txt", 'a+')
def class_balance(train_data_path):
    try:
        config = read_yaml(train_data_path)
        artifacts_dir = config["artifacts"]['artifacts_dir']
        split_data_dir = config["artifacts"]['split_data_dir']
        train = config["artifacts"]['train']
        train_file_path = os.path.join(artifacts_dir, split_data_dir, train)
        train_data=pd.read_csv(train_file_path)       
        train_count_0s=train_data["affair"].value_counts()[0]
        train_count_1s=train_data["affair"].value_counts()[1]
        log(log_file,f"train data saved at { train_file_path} no of 0's {train_count_0s} and no of 1's {train_count_1s}")
        
        y=train_data["affair"]
        train_data.drop(["affair"],axis=1,inplace=True)
        ns=RandomOverSampler()
        train_data,y=ns.fit_resample(train_data,y)
        train_clean_data=pd.concat([train_data,y],axis=1)
        
        train_clean_data_0=train_clean_data["affair"].value_counts()[0]
        train_clean_data_1=train_clean_data["affair"].value_counts()[1]
        
        clean_data_dir = config["artifacts"]["clean_data_dir"]
        clean_data=config["artifacts"]["clean_data"]
        
        create_directory([os.path.join(artifacts_dir, clean_data_dir)])
        clean_data_path=os.path.join(artifacts_dir, clean_data_dir, clean_data)
        save_local_df(train_clean_data, clean_data_path)
        
        log(log_file,f"train clean data saved at { clean_data_path} no of 0's {train_clean_data_0} and no of 1's {train_clean_data_1}")
        
    except Exception as e:
        log(log_file,str(e)) 


if __name__ == '__main__':
    args = argparse.ArgumentParser()

    args.add_argument("--config", "-c", default="config/config.yaml")
    
    parsed_args = args.parse_args()
    class_balance(train_data_path=parsed_args.config)