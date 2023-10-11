import cv2
import webbrowser

image = cv2.imread('qr.png')
detector = cv2.QRCodeDetector()

url, coords, pixels = detector.detectAndDecode(image)

print(url)

webbrowser.open(url)

