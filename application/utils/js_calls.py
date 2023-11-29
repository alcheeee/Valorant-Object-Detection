import eel
import os
from config import *
from utils.settings import settings, model_switch
from utils.picture_predict import picture_detection
from utils.video_predict import video_detection

#Settings
@eel.expose
def setup_settings(width_, height_, frame_rate_, conf_):
    settings.update(width_, height_, frame_rate_, conf_)
    eel.updateSettingsMessage('Settings Applied')

#Reset Settings
@eel.expose
def reset_settings():
    settings.reset()
    eel.updateSettingsMessage('Settings Reset')

#Predictions Folder
@eel.expose
def open_predictions():
    path = 'predictions'
    path = os.path.realpath(path)
    os.startfile(path)

#Uplaod Folder
@eel.expose
def open_upload():
    path = 'upload'
    path = os.path.realpath(path)
    os.startfile(path)

#Switch to v8n model 
@eel.expose
def switch_v8n():
    model_switch.switch_model('v8n')
    eel.updateMessage('Switched to YOLOv8n')

#Switch to v8x model
@eel.expose
def switch_v8x():
    model_switch.switch_model('v8x')
    eel.updateMessage('Switched to YOLOv8x')

#Upload Function
@eel.expose
def upload_file(file_name):
    
    #Get the file path and make sure its in upload
    original_file_path = os.path.join(upload_folder, file_name)
    if not os.path.exists(original_file_path):
        eel.updateMessage('Make sure file is in: ' + original_file_path)
    
    #File type check
    _, ext = os.path.splitext(original_file_path)
    
    #Image Predict
    if ext in image_extensions:
        return picture_detection(original_file_path)
    
    #Video Predict
    elif ext in video_extensions:
        return video_detection(original_file_path)

    #Invalid YOLO file type
    else: 
        eel.updateMessage(f'Error!\nFor an Image Prediction use one of these extensions:\n{image_extensions}\n\n\nFor a Video Prediction use one of these extensions:\n{video_extensions}\n')

