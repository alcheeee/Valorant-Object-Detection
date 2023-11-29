from glob import glob
import os
import shutil
from utils.general import rename_move_file
from config import *
import eel
import cv2

@eel.expose
def picture_detection(img):
    
    #Get Width/Height from settings class
    width = settings.width
    height = settings.height
    
    #Handling sizing
    if width is None and height is None:
        use_image = img
    else:
        #use_image = resize_image(img)
        image = cv2.imread(img) #image to array
        use_image = cv2.resize(image, (width, height))
    
    #Resize Image and predict
    results = model_switch.model.predict(use_image, 
                            save=True,
                            save_conf=True,
                            project='predictions',
                            name='img')
    
    #From source to target directory
    source_dir = os.path.join('predictions', 'img')
    end_dir = 'predictions'
    
    #Grabs the file(s) from /img
    for file_path in glob(os.path.join(source_dir, '*')):
        rename_move_file(file_path, end_dir) #Moves the file from predictions/img to predictions/

    #Remove /img directory for next prediction
    shutil.rmtree(source_dir)
    eel.updateMessage('Image Processing Completed')