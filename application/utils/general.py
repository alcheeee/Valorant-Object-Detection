import random
import shutil
import os
from config import *

def generate_number():
    return random.randint(1000000000, 9999999999)

#Renaming and moving file function
def rename_move_file(file_path, target):
    
    #Get base name of file
    base_name = os.path.basename(file_path)
    name, ext = os.path.splitext(base_name)
    
    new_name = f'{name}{generate_number()}{ext}' #apply the new name with correct .ext
    new_path = os.path.join(target, new_name) #New file path
    
    shutil.move(file_path, new_path) #Move file to correct directory