import cv2
import matplotlib.pyplot as plt
import easyocr

# Specify the OCR language
reader = easyocr.Reader(['en'])

img = cv2.imread("20231110_112100.jpg", cv2.IMREAD_COLOR)

# Assume the largest contour represents the medicine box
largest_contour = max(contours, key=cv2.contourArea)

# Extract the bounding box of the largest contour
x, y, w, h = cv2.boundingRect(largest_contour)

# Crop the region of interest (ROI)
medicine_box = img[y:y+h, x:x+w]

# Display the cropped medicine box
plt.imshow(cv2.cvtColor(medicine_box, cv2.COLOR_BGR2RGB))
plt.title('Medicine Box')
plt.show()

# Use EasyOCR to extract text from the cropped image
results = reader.readtext(cv2.cvtColor(medicine_box, cv2.COLOR_BGR2RGB))

# Assuming the medicine name is the first result, you can access it like this
medicine_name = results[0][1]

# Print the extracted medicine name
print("Medicine Name:", medicine_name)
