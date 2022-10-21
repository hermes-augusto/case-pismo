import os
import glob

directory_tmp = "../data/tmp"

def ajust_file_tmp(file):
    """
      Make ajust in files input and move for tmp folder to use in process
    """
    with open(file) as f:
      f_final = f.read().replace('{"timestamp":',',{"timestamp":')
    f_final = "["+f_final+"]"
    f_final = f_final.replace("[,{","[{")
    with open(f"{directory_tmp}/{os.path.basename(file)}", "w") as outfile:
      outfile.writelines(f_final)
    return f"{os.path.basename(file)}, Ajustado com sucesso!"

def create_dir(directory_tmp,input_data):
  """
    Create a dir tmp for files after ajust 
    and generete a list of files input
  """
  os.makedirs(directory_tmp,exist_ok = True)
  return glob.glob(f"{input_data}*")