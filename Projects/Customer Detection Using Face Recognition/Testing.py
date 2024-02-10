import tkinter as tk
from tkinter import ttk
import cv2
import face_recognition
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

class CustomerPredictionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer Prediction App")

        # Input Fields
        self.label_name = ttk.Label(root, text="Customer Name:")
        self.label_name.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        self.entry_name = ttk.Entry(root)
        self.entry_name.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

        # Prediction Result
        self.label_result = ttk.Label(root, text="")
        self.label_result.grid(row=1, column=0, columnspan=2, pady=10)

        # Predict Button
        self.predict_button = ttk.Button(root, text="Predict", command=self.predict)
        self.predict_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Load Sample Data and Train Model
        self.load_data()
        self.train_model()

    def load_data(self):
        # Example: Load your face data and labels
        # Replace this with your data loading logic
        # For simplicity, I'm creating a dummy dataset here
        self.known_faces = []
        self.labels = []
        self.labels_encoder = LabelEncoder()

        # Add known faces and labels
        # You should replace this with your actual face data and labels
        known_face_image = face_recognition.load_image_file("known_face.jpg")
        known_face_encoding = face_recognition.face_encodings(known_face_image)[0]
        self.known_faces.append(known_face_encoding)
        self.labels.append('Yes')

    def train_model(self):
        # Convert labels to numerical values
        y = self.labels_encoder.fit_transform(self.labels)

        # Train a simple RandomForestClassifier (you can replace this with your preferred model)
        self.model = RandomForestClassifier()
        self.model.fit(self.known_faces, y)

    def predict(self):
        # Capture image from webcam
        video_capture = cv2.VideoCapture(0)
        ret, frame = video_capture.read()

        # Find faces in the frame
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        if len(face_encodings) == 0:
            self.label_result.config(text="No face detected!")
        else:
            # Predict using the trained model
            prediction = self.model.predict(face_encodings)

            # Convert prediction back to original class labels
            prediction_label = self.labels_encoder.inverse_transform(prediction)[0]

            # Display the result
            self.label_result.config(text=f"Prediction: {prediction_label}")

        video_capture.release()

if __name__ == "__main__":
    root = tk.Tk()
    app = CustomerPredictionApp(root)
    root.mainloop()
