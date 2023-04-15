import time, os
import configparser
from engine import WindowsEngine
from imageprocessing import ImageUtils
from headergenerator import HeaderGenerator

my_header = HeaderGenerator("ChatGPT partially generated code", 50)
my_header.generate_header()

# Declare the necessary file paths
settings_file = "settings.ini"

# Load the settings file or create new settings
config = configparser.ConfigParser()
if os.path.exists(settings_file):
    config.read(settings_file)

amplified_path = config["PATHS"]["amplified"]
screenshot_path = config["PATHS"]["screenshot"]
cropped_img_path = config["PATHS"]["cropped_img"]

win = WindowsEngine()
imageUtils = ImageUtils()

while(True):
    # Get the screen executable and save it
    win.get_screen_executable('MU', screenshot_path)

    # Crop the upper-left part of the saved screenshot image and save it
    cropped_image_obj = imageUtils.crop_upper_left(None, screenshot_path, cropped_img_path)

    # Amplify the cropped image using the zoom_in_image function and save it
    amplified_image_obj = imageUtils.zoom_in_image(cropped_image_obj, zoom_factor=8)
    amplified_image_obj.save(amplified_path)

    # Preprocess the amplified image and get the text from it
    result = imageUtils.preprocess_image(amplified_path)
    cleanArray = [x for x in result.split('\n') if x.strip() != '']
    name = cleanArray[0]
    coord = cleanArray[1]
    print(f'Text collected: {name} -- Coordinates: {coord}')
    
    time.sleep(int(config["SETTINGS"]["wait_interval"]))


