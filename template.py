import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

package_name = "MLJenkins-1"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/data_ingestion.py",
    f"src/{package_name}/data_preprocessing.py",
    f"src/{package_name}/training.py",
    f"src/{package_name}/evaluation.py",
    f"src/{package_name}/pipeline.py",
    f"src/{package_name}/utils.py",
    f"src/{package_name}/logging.py",
    "configs/config.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "init_setup.sh"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"creating {filedir} for {filename}")
    
    if (not os.path.exists(filepath)):
        with open(filepath, "w") as f:
            pass
        logging.info(f"creating empty file {filename}")
    else:
        logging.info(f"file {filename} successfully created")
