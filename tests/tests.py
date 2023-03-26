
# Import necessary modules
import unittest
from io import StringIO

# Import function to test
from engine import preprocess_image


class TestPreprocessImageFunction(unittest.TestCase):

    def setUp(self):
        """
        Setting up the test environment
        """
        # Create a test image file
        self.img_file = 'images\game_menu_mapName.jpg'

    def test_process_small_area_name_image(self):
        """
        Test case to check the functionality of the preprocess_image function
        """
        # Expected Output
        expected_text = 'Lorencia'

        # Call function
        result = preprocess_image(self.img_file)

        # Assert output
        self.assertEqual(result.strip(), expected_text)

    def test_process_full_screen_area_name_success(self):
        # TODO document why this method is empty
        pass

if __name__ == '__main__':
    unittest.main()