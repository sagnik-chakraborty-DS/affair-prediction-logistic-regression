import yaml
import json
import os
from datetime import datetime
import sys


def read_yaml(path_to_yaml:str)->dict:
        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)
        return content    
    

def create_directory(dirs:list):
        for directory_path in dirs:
            os.makedirs(directory_path, exist_ok=True)
            print(f"directory is saved at {directory_path}")

def save_local_df(data,data_path,index_status=False):
    #to save test train file
    data.to_csv(data_path,index=index_status)
    print(f"data is saved at {data_path}")

    
    
def log(file_object,log_message):
     file_object.write(str(datetime.now().date())+"/"+str(datetime.now().strftime("%H:%M:%S"))+"\t\t"+log_message+"\n")    


def save_report(report,report_path:str):
    with open(report_path,"w+") as i:
        i.write(report)
    
         

            
        