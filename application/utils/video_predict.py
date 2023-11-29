from config import *
import cv2
import eel
import time
from utils.general import generate_number

@eel.expose
def video_detection(vid):
    
    #Settings
    width = settings.width
    height = settings.height
    frame_rate = settings.frame_rate
    conf = settings.conf
    
    #Video Capture & Output
    cap = cv2.VideoCapture(vid)
    output_path = f'predictions/{generate_number()}.mp4'
    
    #Checking Settings and applying defaults if None
    if frame_rate is None:
        frame_rate = int(cap.get(5))
    if width is None:
        width = int(cap.get(3))
    if height is None:
        height = int(cap.get(4))
    
    #Converts the video frames back to mp4
    video_writer = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), 
                               frame_rate, (width, height))
    
    start_time = time.time()
    frame_count = 0
    
    #While theres still frames, continue
    while cap.isOpened():
        success, frame = cap.read()
        frame_count += 1
        
        #If frame, resize to width/height & predict
        if success:
            resize_frame = cv2.resize(frame, (width, height))
            results = model_switch.model.track(resize_frame, 
                                persist=True, 
                                conf=conf, 
                                verbose=False,
                                tracker=tracker)
            
            #Draw box on frame & add it to .mp4
            annotated_frame = results[0].plot()
            video_writer.write(annotated_frame)
            
            #Update HTML every half second
            if time.time() - start_time > 0.5:
                eel.updateMessage(f'Processed {frame_count} frames.')
                start_time = time.time()
        else:
            break #No more frames
    
    #Unloads the video capture/writer once finished
    video_writer.release()
    cap.release()
    eel.updateMessage('Video Processing Completed')