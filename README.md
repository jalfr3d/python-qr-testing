# QR Code Generator and Detector

## Overview

This set of scripts allows you to generate and interact with QR codes. You can create QR codes from text URLs, images, or data, and also detect and open URLs from QR codes using your computer's webcam or existing images.

## Features

- **QR Code Generation**: Create QR codes from text URLs or data.
  
- **QR Code Detection**: Detect QR codes in images or using your webcam.

- **URL Opening**: Automatically open detected URLs in your default web browser.

## How to Use

### QR Code Generation (qr_generator.py)

1. Create a text file named "urls.txt" with each line containing a URL or data you want to convert into QR codes.

2. Run the script `qr_generator.py`.

3. The script will generate QR codes for each URL in "urls.txt" and save them as PNG images, e.g., `1.png`, `2.png`, etc.

### QR Code Detection from Image (qr_detector.py)

1. Place the image containing the QR code in the same directory as the script.

2. Rename the image to "qr.png" or adjust the script accordingly.

3. Run the script `qr_detector.py`.

4. The script will detect and decode the QR code and open the URL in your default web browser.

### QR Code Detection from Webcam (webcam_qr_detector.py)

1. Ensure your computer's webcam is connected and working.

2. Run the script `webcam_qr_detector.py`.

3. Point your webcam at a QR code.

4. The script will continuously capture frames and open the detected URL in your default web browser.

5. To stop the script, press 'q' while the video feed is active.

## Dependencies

- Python 3.x
- OpenCV (`cv2` module): Required for both generating and detecting QR codes.
- `webbrowser` module: Used to open URLs in the default web browser.
- `qrcode` module: Required for generating QR codes.

## Example Usage

Here's an example of how to use these scripts:

1. Use `qr_generator.py` to create QR codes from a list of URLs or data in "urls.txt".

2. Use `qr_detector.py` to decode a QR code from an image and open the URL in your browser.

3. Use `webcam_qr_detector.py` to continuously scan for QR codes using your webcam.

## Notes

- Make sure to adjust file names and paths in the scripts to match your system setup.

- To enhance the functionality, you can customize the script for different use cases, such as encoding different data into QR codes.

- These scripts are a starting point for working with QR codes and can be integrated into various applications.

With the QR Code Generator and Detector scripts, you can easily generate QR codes and interact with them using your computer's webcam or existing images. These scripts can be customized and extended to suit your specific needs.

## License

This project is licensed under the MIT License. You are free to use and modify the code for your own purposes.
