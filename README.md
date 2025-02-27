Sistema de Registro de Visitantes
Este sistema permite registrar y gestionar visitantes utilizando la cédula de identidad. Implementa reconocimiento óptico de caracteres (OCR) para extraer la información de la cédula y almacenarla en un registro.
Requisitos de Instalación
Para ejecutar correctamente este sistema, es necesario instalar las siguientes dependencias:
1. Instalar Tesseract OCR y Pytesseract
Tesseract es un motor de reconocimiento óptico de caracteres que se utilizará para extraer información de las cédulas de identidad.
En Windows:
1.	Descarga e instala Tesseract desde: https://github.com/UB-Mannheim/tesseract/wiki
2.	Asegúrate de agregar Tesseract al PATH del sistema.
En Linux:
sudo apt update && sudo apt install tesseract-ocr
En macOS:
brew install tesseract
Luego, instala la biblioteca pytesseract para interactuar con Tesseract desde Python:
pip install pytesseract
2. Instalar Pillow
Pillow es una biblioteca de procesamiento de imágenes en Python:
pip install pillow
3. Instalar OpenPyXL
Esta biblioteca permite la manipulación de archivos de Excel en Python:
pip install openpyxl
4. Instalar OpenCV
OpenCV se usa para el procesamiento y manipulación de imágenes:
pip install opencv-python

