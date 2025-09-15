import os
from pathlib import Path

project_name='PratikDemoProject'

list_of_files={
  #f is used for formatted String Literal. required Python > 3.6
  f"{project_name}/__init__.py",
  f"{project_name}/requirements.txt",
  f"{project_name}/components/__init__.py",
  f"{project_name}/components/data_ingestion/__init__.py",
  f"{project_name}/components/data_validation/__init__.py",
  f"{project_name}/components/data_transformation/__init__.py",
  f"{project_name}/components/model_trainer/__init__.py",
  f"{project_name}/utils/__init__.py",
}

for path in list_of_files:
  #convert String path to a Path Object
  filepath=Path(path)
  #Split it into directory and file_name
  filedir,filename=os.path.split(path)
  if(filedir!=""):
    #Create a directory if it doesnt exist
    os.makedirs(filedir,exist_ok=True)

    if(not os.path.exists(filepath) or (os.path.getsize(filepath)==0)):
      with open(filepath,"w") as f:
        #Create an empty file 
        #"pass" keyword is like placeholder(when block does nothing we can use this)
        pass