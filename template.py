import os
from pathlib import Path
import logging  # for generating information at the run time.
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(messages)s')

project_name = "textSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py", #github for CI/CD deployment --> if you do commit, it will directly do deployment from github to cloud, gitkeep keep the github folder filled
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]
for filepath in list_of_files:
    filepath = Path(filepath) # Path will first detect the system specification for giving paths, then in that format it will return the path
    filedir, filename = os.path.split(filepath) # split the filepath into its components of directory and file
    if filedir != '':
        os.makedirs(filedir, exist_ok=True) # if the directory doesn't exist, it will be created
        logging.info(f"Creating directory: {filedir} for the file: {filename}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"creating empty file: {filepath}")
    else:
        logging.info(f"{filename} is already exists")
        
    