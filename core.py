# core.py

import cv2  # OpenCV for camera handling
import numpy as np
from eye_tracking import EyeTracker
from mouse_control import MouseController
import configparser

"""
class EyeDriveCore:
    def __init__(self, config_path='config/app_config.yml'):
        self.config = self.load_config(config_path)
        self.eye_tracker = EyeTracker()
        self.mouse_controller = MouseController()
        self.setup_eye_tracking()

    def load_config(self, path):
        # Load configuration settings from a YAML file
        import yaml
        with open(path, 'r') as file:
            config = yaml.safe_load(file)
        return config

    def setup_eye_tracking(self):
        # Initialize the eye tracker based on configuration settings
        if not self.eye_tracker.initialize(self.config['eye_tracking']):
            print("Failed to initialize eye tracker.")
            exit(1)
        print("Eye tracker initialized successfully.")

    def process_frame(self):
        # Capture a frame from the camera and process it
        ret, frame = self.eye_tracker.capture_frame()
        if not ret:
            print("Failed to capture frame.")
            return

        eye_position = self.eye_tracker.detect_eye_position(frame)
        if eye_position:
            self.mouse_controller.move_cursor(eye_position)
        else:
            print("Failed to detect eye position.")

    def run(self):
        # Main loop to continuously process frames
        print("Starting EyeDrive...")
        while True:
            self.process_frame()

if __name__ == '__main__':
    core = EyeDriveCore()
    core.run()
"""