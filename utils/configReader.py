import csv
from configparser import ConfigParser
import os
from pathlib import Path
from typing import Dict, List

current_dir = Path(__file__).resolve().absolute().parent.parent

def readconfig(section, key):
    config = ConfigParser()
    # 1. Get the absolute directory path of THIS configReader.py file

    # 2. Join it with your ini filename to get the exact absolute path
    config_path = os.path.join(current_dir,"DemoProject/testdata", 'conf.ini')
    config.read(config_path)
    return config.get(section, key)


def read_test_data(file_path:str)->List[Dict[str, str]]:
    file = os.path.join(current_dir, "DemoProject\\testdata", file_path)
    with open(file, newline='',encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader]

