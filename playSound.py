import vlc
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
    init = vlc.MediaPlayer("sound/sound6.mp3")
    phone = vlc.MediaPlayer("sound/sound1.mp3")
    ex = vlc.MediaPlayer("sound/sound7.mp3")
    while running:
        files = os.listdir(path)
        if "init" in files:
            init = vlc.MediaPlayer("sound/sound6.mp3")
            init.play()
            os.remove(path+"init")
        if "read" in files:
            phone = vlc.MediaPlayer("sound/sound1.mp3")
            phone.play()
            os.remove(path+"read")
        if "quit" in files:
            ex = vlc.MediaPlayer("sound/sound7.mp3")
            ex.play()
            time.sleep(5)
            os.remove(path+"quit")
            running = False

if __name__ == "__main__":
    preprocess_files()
    read()