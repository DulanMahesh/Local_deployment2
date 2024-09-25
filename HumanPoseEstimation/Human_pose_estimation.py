import cv2  #
import mediapipe as mp  # Import MediaPipe for pose estimation


img = cv2.imread("cellphone_girl.jpg")

# Get the width and height of the image for further processing.
img_width = img.shape[1]
img_height = img.shape[0]

# Display the original image in a window.
cv2.imshow('Human pose', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Initialize MediaPipe Pose and Drawing utilities.
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

# Use MediaPipe's Pose functionality with static image mode.
with mp_pose.Pose(static_image_mode=True) as pose:
    # Make a copy of the original image for annotation.
    annotated_img = img.copy()

    # Process the image to find pose landmarks.
    results = pose.process(img)

    # Define the circle radius for drawing landmarks, scaled by image height.
    circle_radius = int(.007 * img_height)

    # Specify the drawing style for landmark points (color, thickness, and radius).
    point_spec = mp_drawing.DrawingSpec(color=(220, 100, 0), thickness=-1, circle_radius=circle_radius)

    # Draw landmark points on the annotated image.
    mp_drawing.draw_landmarks(annotated_img,
                              landmark_list=results.pose_landmarks,
                              landmark_drawing_spec=point_spec)

# Display the annotated image with landmarks drawn.
cv2.imshow('Landmarks drawn', annotated_img)
cv2.waitKey(0)  # Wait for a key press to proceed.
cv2.destroyAllWindows()  # Close the image window.

# Make a copy of the original image again for drawing connections.
annotated_img = img.copy()

# Specify the drawing style for connections between landmarks.
line_spec = mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2)

# Draw both landmark points and connections on the annotated image.
mp_drawing.draw_landmarks(annotated_img,
                          landmark_list=results.pose_landmarks,
                          connections=mp_pose.POSE_CONNECTIONS,
                          landmark_drawing_spec=point_spec,
                          connection_drawing_spec=line_spec)

# Display the annotated image with both landmarks and connections drawn.
cv2.imshow('Landmarks drawn', annotated_img)
cv2.waitKey(0)  # Wait for a key press to proceed.
cv2.destroyAllWindows()  # Close the image window.

# Acquire the landmark coordinates for the left and right hips.
r_hip_x = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP].x * img_width)  # X-coordinate of right hip
r_hip_y = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP].y * img_height)  # Y-coordinate of right hip

l_hip_x = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP].x * img_width)  # X-coordinate of left hip
l_hip_y = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP].y * img_height)  # Y-coordinate of left hip

# Print the coordinates of the right and left hips to the console.
print('Right hip coordinates : (', r_hip_x, ',', r_hip_y, ')')
print('Left hip coordinates  : (', l_hip_x, ',', l_hip_y, ')')
