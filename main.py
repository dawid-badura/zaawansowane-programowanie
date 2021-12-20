import cv2
import pytesseract
from PIL import Image

text1 = pytesseract.image_to_string(Image.open('home.jpg'))
text2 = pytesseract.image_to_string(Image.open('justdance.jpg'))
text3 = pytesseract.image_to_string(Image.open('hello.jpg'))
text4 = pytesseract.image_to_string(Image.open('queen.jpg'))
text5 = pytesseract.image_to_string(Image.open('yourtext.jpg'))
print(text1, text2, text3, text4, text5)
