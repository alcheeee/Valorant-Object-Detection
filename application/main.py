import eel
from config import *
from utils.js_calls import *

#Initialize GUI
eel.init('gui')

#Start the app
if __name__ == '__main__':
    eel.start('main.html', 
              size=(566, 639), 
              mode='brave', 
              cmdline_args=['--app'])
    
