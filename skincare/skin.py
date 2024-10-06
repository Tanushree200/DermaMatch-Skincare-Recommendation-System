import cv2

# Function to capture image from camera
def capture_image():
    # Initialize the camera
    cap = cv2.VideoCapture(0)

    # Capture frame-by-frame
    ret, frame = cap.read()

    # Release the camera
    cap.release()

    return frame

# Function to analyze skin type from image
def analyze_skin_type(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Thresholding to separate skin region from background
    _, skin_mask = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Find contours in the skin mask
    contours, _ = cv2.findContours(skin_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Assuming the largest contour represents the skin region
    if contours:
        skin_contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(skin_contour)

        # Calculate skin area ratio
        skin_area_ratio = cv2.contourArea(skin_contour) / (w * h)

        # Divide the face into two regions: upper (forehead and cheeks) and lower (nose and chin)
        upper_face_y = y + h // 2

        # Calculate the skin area ratios for upper and lower face regions
        upper_face_skin_area = 0
        lower_face_skin_area = 0
        for contour in contours:
            _, _, w, h = cv2.boundingRect(contour)
            area = cv2.contourArea(contour)
            if y + h < upper_face_y:
                upper_face_skin_area += area
            else:
                lower_face_skin_area += area

        upper_face_skin_area_ratio = upper_face_skin_area / (w * h)
        lower_face_skin_area_ratio = lower_face_skin_area / (w * h)

        # Classify skin type based on skin area ratios
        if upper_face_skin_area_ratio < 0.1:
            upper_skin_type = "Dry"
        elif upper_face_skin_area_ratio > 0.2:
            upper_skin_type = "Oily"
        else:
            upper_skin_type = "Normal"

        if lower_face_skin_area_ratio < 0.1:
            lower_skin_type = "Dry"
        elif lower_face_skin_area_ratio > 0.2:
            lower_skin_type = "Oily"
        else:
            lower_skin_type = "Normal"

        # Determine overall skin type based on combination of upper and lower face
        if upper_skin_type == lower_skin_type:
            return upper_skin_type
        else:
            return "Combination"
    else:
        return "Unknown"

# Main function
def main():
    # Capture image from camera
    image = capture_image()

    # Analyze skin type from image
    skin_type = analyze_skin_type(image)
    print("Detected skin type:", skin_type)

    # Display the captured image
    cv2.imshow('Captured Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
