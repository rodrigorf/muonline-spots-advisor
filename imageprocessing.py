import pytesseract
import numpy as np
from PIL import Image, ImageOps

class ImageUtils:
    def crop_upper_left(self, image_obj=None, image_path=None, save_path=None):
        """
        Crops the upper left corner of an image and optionally saves the cropped image to a file.

        Args:
        - image_path: string, path to the input image file.
        - save_path: string or None (default). If a string is provided, the cropped image is saved to that location. If None, the cropped image is not saved.

        Returns:
        - cropped_image: PIL Image object, the cropped image.

        """

        # Load the image
        if image_path is not None:
            image = Image.open(image_path)
        elif image_obj is not None:
            image = image_obj
        else:
            raise ValueError("Either image_path or image_obj must be provided.")
        
        # Convert the image to a numpy array
        image_array = np.array(image)

        # Define the coordinates to crop the upper left corner
        crop_coords = (0, 0, 160, 30) # (left, upper, right, lower)

        # Crop the image array
        cropped_array = image_array[crop_coords[1]:crop_coords[3], crop_coords[0]:crop_coords[2]]

        # Convert the cropped array back to an image
        cropped_image = Image.fromarray(cropped_array)

        # Save or display the cropped image
        if save_path:
            cropped_image.save(save_path)

        return cropped_image

    def preprocess_image(self, image_path):
        """
        Takes image path as input and returns the pre-processed text extracted from it
        """
        # Open and read the image file
        image = Image.open(image_path).convert('L') 

        # Apply thresholding to binarize the image
        threshold_value = 150
        image = image.point(lambda pixel: pixel < threshold_value and 255)

        # Apply dilation to fill gaps in between letters
        dilation_size = 1
        structure_elem = Image.new('RGB', (dilation_size, dilation_size), (255, 255, 255))
        imagemod = ImageOps.expand(image, border=(structure_elem.height, structure_elem.width))

        # Extract text using pytesseract
        text = pytesseract.image_to_string(imagemod)

        # Return the extracted text
        return text

    def zoom_in_image(self, image, zoom_factor):
        """
        Zooms in an image by a zoom factor.

        Args:
        - image: PIL Image object, the image to be zoomed.
        - zoom_factor: int, the factor by which to zoom the image.

        Returns:
        - zoomed_image: PIL Image object, the zoomed image.
        """

        # Get the size of the original image
        original_size = image.size

        # Calculate the new size of the image after zooming
        new_size = tuple([i * zoom_factor for i in original_size])

        # Resize the image to the new size
        zoomed_image = image.resize(new_size)

        return zoomed_image