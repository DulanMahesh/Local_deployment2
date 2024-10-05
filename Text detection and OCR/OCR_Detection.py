import cv2
import numpy as np
import matplotlib.pyplot as plt
import time

# Set grayscale as the default colormap for displaying images in matplotlib
plt.rcParams['image.cmap'] = 'gray'


# Function to align bounding boxes into a standard rectangle shape
def fourPointsTransform(frame, vertices):
    """Extracts and transforms the region of interest (ROI) defined by vertices into a rectangle."""
    # Convert vertices to float32 data type for precise calculations
    vertices = np.asarray(vertices).astype(np.float32)

    # Define the target output size (width=100, height=32)
    outputSize = (100, 32)

    # Define target rectangle vertices for transformation
    targetVertices = np.array([
        [0, outputSize[1] - 1],
        [0, 0],
        [outputSize[0] - 1, 0],
        [outputSize[0] - 1, outputSize[1] - 1]], dtype="float32")

    # Compute the perspective transformation matrix
    rotationMatrix = cv2.getPerspectiveTransform(vertices, targetVertices)

    # Apply perspective warp to transform the image
    result = cv2.warpPerspective(frame, rotationMatrix, outputSize)
    return result


# Function to detect and recognize text from an image
def recognizeText(image, debug=False):
    """Detects, recognizes, and outputs text from a natural image scene."""

    # Create a blank canvas (white) to display output text
    outputCanvas = np.full(image.shape[:3], 255, dtype=np.uint8)

    # Detect text using the pre-initialized DB text detector
    boxes, confs = textDetector.detect(image)

    print("Recognized Text:")

    # Iterate over each bounding box (detected text region)
    for box in boxes:
        # Apply transformation to get a straightened image of the text
        croppedRoi = fourPointsTransform(image, box)

        if debug:
            # Optionally display the cropped region (detected text area)
            cv2.imshow('Output', croppedRoi)

        # Use the CRNN model to recognize the text within the cropped region
        recResult = textRecognizer.recognize(croppedRoi)
        print(recResult)

        # Calculate the height of the bounding box to scale the font size for display
        boxHeight = int(abs(box[0, 1] - box[1, 1]))

        # Calculate the appropriate font scale based on box height
        fontScale = cv2.getFontScaleFromHeight(
            cv2.FONT_HERSHEY_SIMPLEX, boxHeight - 10, 1)

        # Get the coordinates to place the recognized text on the canvas
        placement = (int(box[0, 0]), int(box[0, 1]))

        # Write the recognized text on the output canvas
        cv2.putText(outputCanvas, recResult, placement,
                    cv2.FONT_HERSHEY_SIMPLEX, fontScale, (255, 0, 0), 1, 5)

    # Draw the bounding boxes around the detected text regions
    cv2.polylines(image, boxes, True, (255, 0, 255), 4)

    # Combine the input image and output canvas side by side for display
    combinedResult = cv2.hconcat([image, outputCanvas])

    # Show the final combined result with detected and recognized text
    cv2.imshow('Result', combinedResult)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":

    # Load the input image for text detection and recognition
    image = cv2.imread('./visuals/dutch_signboard.jpg')
    cv2.imshow('Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Initialize an empty list to store the vocabulary (recognizable characters)
    vocabulary = []

    # Open and read the vocabulary file containing characters
    with open("./resources/alphabet_94.txt") as f:
        # Append each character to the vocabulary list
        for l in f:
            vocabulary.append(l.strip())
        f.close()

    # Display the loaded vocabulary
    print("Vocabulary:", vocabulary)
    print("Vocabulary size: ", len(vocabulary))

    # Load the DB model for text detection (based on ResNet-50)
    textDetector = cv2.dnn_TextDetectionModel_DB("./resources/DB_TD500_resnet50.onnx")

    # Set the input size for the detection model
    inputSize = (640, 640)

    # Set the thresholds for Binary Map creation and polygon detection
    binThresh = 0.3
    polyThresh = 0.5

    # Define mean pixel values for normalization
    mean = (122.67891434, 116.66876762, 104.00698793)

    # Configure the text detector with the given parameters
    textDetector.setBinaryThreshold(binThresh).setPolygonThreshold(polyThresh)
    textDetector.setInputParams(1.0 / 255, inputSize, mean, True)

    # Load the CRNN model for text recognition
    textRecognizer = cv2.dnn_TextRecognitionModel("./resources/crnn_cs.onnx")
    textRecognizer.setDecodeType("CTC-greedy")
    textRecognizer.setVocabulary(vocabulary)

    # Configure the recognizer with input parameters for normalization
    textRecognizer.setInputParams(1 / 127.5, (100, 32), (127.5, 127.5, 127.5), True)

    # Detect text boxes and draw bounding boxes on the image
    boxes, confs = textDetector.detect(image)
    cv2.polylines(image, boxes, True, (255, 0, 255), 4)

    # Display the image with detected bounding boxes
    cv2.imshow('Bounding Boxes', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Display the transformed (warped) output of the first detected text region
    warped_detection = fourPointsTransform(image, boxes[0])
    cv2.imshow('Transformed Detected Text', warped_detection)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Recognize and display the detected text on the canvas
    recognizeText(image)

    # Load additional images and apply text detection and recognition
    img2 = cv2.imread('./visuals/card.jpg')
    recognizeText(img2)

    img3 = cv2.imread('./visuals/traffic2.jpg')
    recognizeText(img3)

    img4 = cv2.imread('./visuals/car.jpg')
    recognizeText(img4)

    img5 = cv2.imread('./visuals/traffic1.jpg')
    recognizeText(img5)

    # Failure case: If text detection/recognition fails, this will be handled
    img6 = cv2.imread('./visuals/Board.jpg')
    recognizeText(img6)
