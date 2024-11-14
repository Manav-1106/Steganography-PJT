import cv2
import os

def extract_frames_from_video(video_path, output_folder, frame_interval=1):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Capture the video
    cap = cv2.VideoCapture(video_path)

    # Check if video opened successfully
    if not cap.isOpened():
        print("Error: Could not open video file.")
        return

    frame_count = 0
    saved_frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Save every nth frame according to the frame_interval
        if frame_count % frame_interval == 0:
            frame_path = os.path.join(output_folder, f"frame_{saved_frame_count:04d}.jpg")  # Zero-padded frame filename
            cv2.imwrite(frame_path, frame)
            print(f"Extracted frame {frame_count} and saved as {frame_path}.")
            saved_frame_count += 1
        
        frame_count += 1

    cap.release()
    print(f"Total {saved_frame_count} frames extracted and saved in {output_folder}.")

video_path = '/Users/manavguduguntla/Documents/Steganography/Bali.MOV'  # Input video file
output_folder = '/Users/manavguduguntla/Documents/Steganography/output_frames'  # Folder to save extracted frames

# Extract frames from the video, saving every frame (frame_interval=1)
extract_frames_from_video(video_path, output_folder) 