import argparse
from PIL import Image
import pytesseract
from googletrans import Translator

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Windows

# Set up argument parser
parser = argparse.ArgumentParser(description='Extract text from an image and translate it.')
parser.add_argument('image_path', help='Path to the image file')
args = parser.parse_args()

# Open the image containing text
image = Image.open(args.image_path)

# Extract text from the image using pytesseract
text = pytesseract.image_to_string(image)

# Initialize the translator
translator = Translator()

# Translate the text to the desired language (e.g. Spanish)
translated_text = translator.translate(text, dest='en').text

# Print the translated text
print(translated_text)
