![Capture](https://user-images.githubusercontent.com/6570848/227750960-774112d2-0a5e-49d3-8cc8-f5c200b239ec.JPG)


# How to Use


Clone the repository git clone [repository url].

Navigate to the directory where you want the repository to be saved.

Create a settings.ini file or modify the existing one.

Run python3 main.py in the terminal to start the program.

The program runs indefinitely, so you'll need to cancel it manually when you're done.


# Configuration

The settings.ini file contains the following settings:

wait_interval - how many seconds to wait before taking a new screenshot and extracting text

amplified - path where the amplified image will be saved

screenshot - path where the screenshot will be saved

cropped_img - path where the cropped image will be saved


# How it Works


The necessary modules are imported: configparser, os, WindowsEngine, ImageUtils, and HeaderGenerator.

A HeaderGenerator object is created to generate a header for the output.

File paths are declared for saving cropped and amplified images.

The settings file is loaded from "settings.ini" or a new settings object is created.

The WindowsEngine and ImageUtils objects are initialized.

The code enters a while loop that runs indefinitely.

The get_screen_executable method of the WindowsEngine object is invoked to get a screenshot and save it.

The upper-left part of the saved screenshot image is cropped using the crop_upper_left method of the ImageUtils object and saved.

The cropped image is amplified using the zoom_in_image function of the ImageUtils object and saved as an amplified image.

The amplified image is preprocessed and text is extracted from it using the preprocess_image method of the ImageUtils object.

The extracted text is printed and the program waits for the number of seconds specified in the wait_interval setting in the settings file.
