import cv2

# Read the video file
vidCap = cv2.VideoCapture("C:\\Users\\sneha\\Downloads\\solidWhiteRight.mp4")

while True:
    success, frame = vidCap.read()
    if not success:
        break

    # Preprocess the frame (e.g., convert to grayscale, edge detection)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)

    # Detect lane lines using Hough Transform
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=50, minLineLength=100, maxLineGap=10)

    # Draw the detected lines on the frame
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # Display the processed frame
    cv2.imshow('Lane Detection', frame)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close the window
vidCap.release()
cv2.destroyAllWindows()