# extracting_text_using_tesseract
**OCR-Based Medicine Box Recognition**

This Python script utilizes Optical Character Recognition (OCR) techniques to recognize and extract text information from an image containing a medicine box. Here's a brief description of the code:

1. **Image Processing:**
   - Reads an input image of a medicine box using OpenCV.
   - Converts the image to grayscale for further processing.
   - Applies thresholding to create a binary image, facilitating contour detection.

2. **Contour Detection:**
   - Identifies contours in the binary image, assuming each contour represents a distinct object or region.

3. **Bounding Box Extraction:**
   - Finds the largest contour, assumed to correspond to the medicine box.
   - Extracts the bounding box coordinates (x, y, width, height) around the medicine box.

4. **Region of Interest (ROI) Cropping:**
   - Crops the original image using the computed bounding box, isolating the medicine box as a region of interest (ROI).

5. **Display Cropped Medicine Box:**
   - Utilizes matplotlib to display the cropped medicine box for visual inspection.

6. **Text Extraction Using OCR:**
   - Utilizes Tesseract OCR (configured via pytesseract) to extract text from the cropped medicine box image.
   - Prints the extracted text, providing information about the medicine, dosage, or any relevant details.

This script can be useful for automating the extraction of textual information from medicine boxes, aiding in tasks such as inventory management or digitizing medication details. Adjustments can be made based on specific use cases or additional image processing techniques for improved accuracy.

![Image of the codes output](https://github.com/harshith-rw/extracting_text_using_tesseract/blob/main/text%20output%20after%20performing%20tesseract%20ocr.jpg)
