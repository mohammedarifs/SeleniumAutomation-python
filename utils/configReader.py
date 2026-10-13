from configparser import ConfigParser
import os
from pathlib import Path

def readconfig(section, key):
    config = ConfigParser()
    # 1. Get the absolute directory path of THIS configReader.py file
    current_dir = Path(__file__).resolve().absolute().parent.parent

    # 2. Join it with your ini filename to get the exact absolute path
    config_path = os.path.join(current_dir,"firstproject/testdata", 'conf.ini')
    config.read(config_path)
    return config.get(section, key)

print(readconfig('cart', 'checkout'))