# Compulsory this library or code import all project
import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "datapipeline" # this name mention as your wish don't required any where its just for this module project package 

list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/database/mongodb.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/generic.py",# this code have new additions
    f"src/{project_name}/kafka_config/__init__.py",
    f"src/{project_name}/kafka_consumer/__init__.py",
    f"src/{project_name}/kafka_consumer/json_consumer.py",
    f"src/{project_name}/kafka_logger/__init__.py",
    f"src/{project_name}/kafka_producer/__init__.py",
    f"src/{project_name}/kafka_producer/json_producer.py",
    f"src/{project_name}/exception.py",
    
    #".env",
    #".dockerignore"
    "consumer_main.py",
    "producer_main.py",
   # "Dockerfile", # this code have new additions, but this file you have created manually project
    "requirements.txt",
    "setup.py",
    "test.py",
    "experiment.ipynb"
]


for filepath in list_of_files:
    # Sometimes getting a issue for backslashes because normally computer use the forward slashes so that above file use / forward slashes, below code help
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")