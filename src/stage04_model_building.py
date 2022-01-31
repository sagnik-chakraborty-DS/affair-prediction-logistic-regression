from src.utils.all_utils import read_yaml,create_directory,save_local_df,log
import argparse
import pandas as pd
import os
from sklearn.linear_model import LogisticRegression
import joblib

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
        
        train_x=clean_data.drop("affair",axis=1)
        train_y=clean_data["affair"]
        
        logmodel=LogisticRegression()
        logmodel.fit(train_x,train_y)
        
        log(log_file,f"model  trained") 
        
        model_dir=config["artifacts"]["model_dir"]
        model_filename=config["artifacts"]["model_filename"]

        model_dir= os.path.join(artifacts_dir,model_dir)
        create_directory([model_dir])
        model_path = os.path.join(model_dir,model_filename)


        #save model
        joblib.dump(logmodel,model_path)
                
    except Exception as e:
        log(log_file,str(e))


if __name__ == '__main__':
    args = argparse.ArgumentParser()

    args.add_argument("--config", "-c", default="config/config.yaml")
    
    parsed_args = args.parse_args()
    parameter_tuning(clean_data_path=parsed_args.config)