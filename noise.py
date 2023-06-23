import cv2

def analyze_noise_artifacts(image):
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Calculate the absolute difference between the grayscale image and its median blur
    median_blur = cv2.medianBlur(gray, 5)
    diff = cv2.absdiff(gray, median_blur)

    # Apply thresholding to the difference image
    _, threshold = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

    # Find contours in the thresholded image
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Analyze each contour
    for contour in contours:
        # Calculate the contour area
        area = cv2.contourArea(contour)

        # Ignore small contours
        if area < 100:
            continue

        # Calculate the contour perimeter
        perimeter = cv2.arcLength(contour, True)

        # Calculate the compactness ratio
        compactness = (perimeter ** 2) / (4 * 3.1415 * area)

        # Print the compactness ratio and draw the contour on the image
        print("Contour Compactness:", compactness)
        cv2.drawContours(image, [contour], -1, (0, 0, 255), 2)

    # Display the image with detected contours
    cv2.imshow("Noise and Artifacts Analysis", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Load the pay slip image
image = cv2.imread("pay_slip.jpg")

# Perform noise and artifacts analysis
analyze_noise_artifacts(image)
