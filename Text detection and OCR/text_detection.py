import cv2
import numpy as np
import time
import matplotlib.pyplot as plt

# Set default colormap for displaying images in grayscale
plt.rcParams['image.cmap'] = 'gray'


def detectTextAll(image):
    """Performs text detection using multiple models and displays the results side by side."""

    # Make copies of the original image for each model
    imEAST = image.copy()
    imDB18 = image.copy()
    imDB50 = image.copy()

    # Detect text using EAST and DB models (ResNet18 and ResNet50)
    boxesEAST, confsEAST = textDetectorEAST.detect(image)
    boxesDB18, confsDB18 = textDetectorDB18.detect(image)
    boxesDB50, confsDB50 = textDetectorDB50.detect(image)

    # Draw detected text bounding boxes on the respective images
    cv2.polylines(imEAST, boxesEAST, True, (255, 0, 255), 4)
    cv2.polylines(imDB18, boxesDB18, True, (255, 0, 255), 4)
    cv2.polylines(imDB50, boxesDB50, True, (255, 0, 255), 4)

    # Concatenate all images horizontally and display the result
    output = cv2.hconcat([image, imEAST, imDB18, imDB50])
    cv2.imshow('Original | EAST | DB18 | DB50', cv2.resize(output, None, fx=0.4, fy=0.4))
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # Load the input image from file
    image = cv2.imread('./visuals/dutch_signboard.jpg')

    # Display the loaded image
    cv2.imshow('Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Set the input image size for the text detection models
    inputSize = (320, 320)

    # Load the pre-trained EAST model for text detection
    textDetectorEAST = cv2.dnn_TextDetectionModel_EAST("./resources/frozen_east_text_detection.pb")

    # Set confidence and non-maximum suppression thresholds for EAST
    conf_thresh = 0.8
    nms_thresh = 0.4
    textDetectorEAST.setConfidenceThreshold(conf_thresh).setNMSThreshold(nms_thresh)
    textDetectorEAST.setInputParams(1.0, inputSize, (123.68, 116.78, 103.94), True)

    # Load DB models (based on ResNet18 and ResNet50) for text detection
    textDetectorDB50 = cv2.dnn_TextDetectionModel_DB("./resources/DB_TD500_resnet50.onnx")
    textDetectorDB18 = cv2.dnn_TextDetectionModel_DB("./resources/DB_TD500_resnet18.onnx")

    # Set binary threshold and polygon threshold for DB models
    bin_thresh = 0.3
    poly_thresh = 0.5
    mean = (122.67891434, 116.66876762, 104.00698793)  # Image mean for normalization

    # Configure input parameters for DB models (ResNet18 and ResNet50)
    textDetectorDB18.setBinaryThreshold(bin_thresh).setPolygonThreshold(poly_thresh)
    textDetectorDB18.setInputParams(1.0 / 255, inputSize, mean, True)
    textDetectorDB50.setBinaryThreshold(bin_thresh).setPolygonThreshold(poly_thresh)
    textDetectorDB50.setInputParams(1.0 / 255, inputSize, mean, True)

    # Create copies of the original image for each model's results
    imEAST = image.copy()
    imDB18 = image.copy()
    imDB50 = image.copy()

    # Detect text using EAST and DB models
    boxesEAST, confsEAST = textDetectorEAST.detect(image)
    boxesDB18, confsDB18 = textDetectorDB18.detect(image)
    boxesDB50, confsDB50 = textDetectorDB50.detect(image)

    # Print the first detected bounding box from EAST for inspection
    print(boxesEAST[0])

    # Draw bounding boxes for text detected using the EAST model
    cv2.polylines(imEAST, boxesEAST, isClosed=True, color=(255, 0, 255), thickness=4)
    cv2.imshow('Bounding boxes for EAST', imEAST)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Draw bounding boxes for text detected using the DB18 model
    cv2.polylines(imDB18, boxesDB18, True, (255, 0, 255), 4)
    cv2.imshow('Bounding boxes for DB18', imDB18)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Draw bounding boxes for text detected using the DB50 model
    cv2.polylines(imDB50, boxesDB50, True, (255, 0, 255), 4)
    cv2.imshow('Bounding boxes for DB50', imDB50)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Concatenate and save the output of all models (Original, EAST, DB18, DB50)
    output = cv2.hconcat([image, imEAST, imDB18, imDB50])
    cv2.imwrite('./visuals/english_signboard_detected.jpg', output)
    cv2.imshow('Original | EAST | DB18 | DB50', cv2.resize(output, None, fx=0.6, fy=0.6))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Process additional images with the detectTextAll function
    img1 = cv2.imread('./visuals/traffic1.jpg')
    detectTextAll(img1)

    img2 = cv2.imread('./visuals/traffic2.jpg')
    detectTextAll(img2)

    img3 = cv2.imread('./visuals/card.jpg')
    detectTextAll(img3)

    img4 = cv2.imread('./visuals/Board.jpg')
    detectTextAll(img4)

    img5 = cv2.imread('./visuals/paper.jpg')
    detectTextAll(img5)

    img6 = cv2.imread('./visuals/car.jpg')
    detectTextAll(img6)

    # Compare runtime performance of EAST vs DB models over multiple iterations
    totalEAST = 0
    totalDB18 = 0
    totalDB50 = 0

    iterations = 10  # Number of iterations for benchmarking
    for i in range(iterations):
        # Measure time taken by the EAST model
        timeEAST = time.time()
        result = textDetectorEAST.detect(img4)
        totalEAST += time.time() - timeEAST

        # Measure time taken by the DB18 model
        timeDB18 = time.time()
        result = textDetectorDB18.detect(img4)
        totalDB18 += time.time() - timeDB18

        # Measure time taken by the DB50 model
        timeDB50 = time.time()
        result = textDetectorDB50.detect(img4)
        totalDB50 += time.time() - timeDB50

    # Calculate average runtime for each model
    avgEAST = totalEAST / iterations
    avgDB18 = totalDB18 / iterations
    avgDB50 = totalDB50 / iterations

    # Display the average runtime of each model as a bar chart
    plt.bar(['EAST', 'DB18', 'DB50'], [avgEAST, avgDB18, avgDB50], color=['g', 'b', 'c'])
    plt.ylabel("seconds")
    plt.xlabel("Model")
    plt.show()
