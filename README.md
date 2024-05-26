# QR Code Generator, QR Scanner, and Image-to-Text Converter GUI Application
Overview
This Python GUI application allows users to generate QR codes, scan existing QR codes, and convert images to text. It’s built using the Tkinter framework, providing an intuitive and user-friendly interface.

Features
QR Code Generator:
Users can input a link or text.
The program generates a QR code image in PNG format.
The generated QR code can be saved or shared.

QR Scanner:
Users can scan existing QR codes using their device’s camera.
The application decodes the QR code and displays the content (e.g., a link or text).

Image-to-Text Converter:
Users can upload an image containing text (e.g., a photo of a document).
The application extracts the text from the image using optical character recognition (OCR).
The extracted text is displayed in a text box.

Installation
Install Python (if not already installed).
Install the required libraries:
Tkinter (for GUI): Tkinter is included with Python, so no additional installation is needed.
qrcode (for QR code generation): Install using pip install qrcode.
opencv-python (for QR code scanning): Install using pip install opencv-python.
pytesseract (for image-to-text conversion): Install using pip install pytesseract.
