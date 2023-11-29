from ultralytics import YOLO

class Settings:
    #Default settings
    def __init__(self):
        self.width = None
        self.height = None
        self.frame_rate = None
        self.conf = 0.4
    
    #Settings handling for custom settings
    def update(self, width, height, frame_rate, conf):
        self.width = int(width) if width not in (None, '') else None
        self.height = int(height) if height not in (None, '') else None
        self.frame_rate = int(frame_rate) if frame_rate not in (None, '') else None
        self.conf = float(conf) if conf not in (None, '') else 0.4

    #Reset back to default settings
    def reset(self):
        self.width = None
        self.height = None
        self.frame_rate = None
        self.conf = 0.4
    
#Switch model
class ModelSwitch:
    #Default model is v8n
    def __init__(self):
        self.model_path = 'model/bestv8n.engine'
        self.load_model()
    
    #Loading models
    def load_model(self):
        self.model = YOLO(self.model_path, task='detect')
    
    #Model switch & load model
    def switch_model(self, name):
        if name == 'v8n':
            self.model_path = 'model/bestv8n.engine'
        
        elif name == 'v8x':
            self.model_path = 'model/bestv8x.engine' 
            
        self.load_model()
        
settings = Settings()
model_switch = ModelSwitch()