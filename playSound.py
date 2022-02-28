import os
import time

def preprocess_files(path = "common/"):
    """
    path :  the path were we create file with the detect phone program to read music and stop this program
    """
    # First we will remove the exit file if exist
    if os.path.exists(path+"exit"):
        os.remove(path+"exit")
    if os.path.exists(path+"read"):
        os.remove(path+"read")

def read(path = "common/"):
    running = True
    while running:
        files = os.listdir(path)
        if "init" in files:
            os.system("mpg123 sound/sound6.mp3 &")
            os.remove(path+"init")
        if "read" in files:
            os.system("mpg123 sound/sound1.mp3 &")
            os.remove(path+"read")
        if "quit" in files:
            os.system("mpg123 sound/sound7.mp3 &")            
            time.sleep(5)
            os.remove(path+"quit")
            running = False
    

if __name__ == "__main__":
    preprocess_files()
    read()