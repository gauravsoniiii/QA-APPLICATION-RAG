import os
from pathlib import Path

list_of_files=[
    "QA_SYSTEM-E2E/__init__.py",
    "QA_SYSTEM-E2E/data_ingestion.py",
    "QA_SYSTEM-E2E/embedding.py",
    "QA_SYSTEM-E2E/model_api.py",
    "Experiments/experiment.ipynb",
    "StreamlitApp.py",
    "logger.py",
    "exception.py"
    "setup.py"
]
for filepath in list_of_files:
   filepath = Path(filepath)
   filedir, filename = os.path.split(filepath)

   if filedir !="":
      os.makedirs(filedir, exist_ok=True)

   if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
      with open(filepath, 'w') as f:
         pass