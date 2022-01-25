import numpy as np
import cv2

# Load models to detector
detector = cv2.dnn.readNetFromCaffe("models/MobileNetSSD_deploy.prototxt", "models/MobileNetSSD_deploy.caffemodel")


def person_detection(image_path):
    image = cv2.imread(image_path)
    image_resized = cv2.resize(image, (300, 300))
    height = image.shape[0] / 300.0
    width = image.shape[1] / 300.0

    blob = cv2.dnn.blobFromImage(image_resized, 0.007843, (300, 300), 127.5)
    detector.setInput(blob)
    count_of_detected_person = 0
    detections = detector.forward()

    cols = image_resized.shape[1]
    rows = image_resized.shape[0]

    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.2:
            x_left_bottom = int(detections[0, 0, i, 3] * cols)
            y_left_bottom = int(detections[0, 0, i, 4] * rows)
            x_right_top = int(detections[0, 0, i, 5] * cols)
            y_right_top = int(detections[0, 0, i, 6] * rows)

            x_left_bottom_ = int(width * x_left_bottom)
            y_left_bottom_ = int(height * y_left_bottom)
            x_right_top_ = int(width * x_right_top)
            y_right_top = int(height * y_right_top)
            cv2.rectangle(image, (x_left_bottom_, y_left_bottom_), (x_right_top_, y_right_top),
                          (0, 0, 0), 2)
            count_of_detected_person = count_of_detected_person + 1

    print("Ilość wykrytych osób na zdjęciu: " + str(count_of_detected_person))
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
