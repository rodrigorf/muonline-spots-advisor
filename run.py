import time, os
import configparser
from engine import WindowsEngine
from imageprocessing import ImageUtils
from headergenerator import HeaderGenerator
from common import MapLocations
from colorama import Fore, Style

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

mapHandle = MapLocations()
while(True):
    start_time = time.time()
    # Get the screen executable and save it
    win.get_screen_executable('MU', screenshot_path)

    # Crop the upper-left part of the saved screenshot image and save it
    cropped_image_obj = imageUtils.crop_upper_left(None, screenshot_path, cropped_img_path)

    # Amplify the cropped image using the zoom_in_image function and save it
    amplified_image_obj = imageUtils.zoom_in_image(cropped_image_obj, zoom_factor=12)
    amplified_image_obj.save(amplified_path)

    # Preprocess the amplified image and get the text from it
    result = imageUtils.preprocess_image(amplified_path)
    cleanArray = [x for x in result.split('\n') if x.strip() != '']
    if(len(cleanArray) > 0):
        joinArray = ' '.join(cleanArray).strip()
        name = joinArray.split(' ')[0]
        coord = joinArray.split(' ')[1]
        print(f'{Fore.GREEN}Text collected: {name} -- Coordinates: {coord}{Style.RESET_ALL}')
        print(f'{Fore.YELLOW}Map spots image: {mapHandle.get_location(name.lower())}{Style.RESET_ALL}')
    else:
        print(f'{Fore.RED}No map name visible.{Style.RESET_ALL}')

    time.sleep(int(config["SETTINGS"]["wait_interval"]))

    elapsed_time = time.time() - start_time
    print(f'{Fore.BLUE}Elapsed time: {elapsed_time:.2f} seconds{Style.RESET_ALL}\n')

