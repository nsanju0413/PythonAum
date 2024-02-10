import glob
import dlib
import cv2
import pickle
import random
import face_vector
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
import requests

# Gamma Correction Function
def adjust_gamma(input_image, gamma=1.0):
    table = np.array([((iteration / 255.0) ** (1.0 / gamma)) * 255 for iteration in np.arange(0, 256)]).astype("uint8")
    return cv2.LUT(input_image, table)

# Image Reading and Face Vector Extraction
def read_image(path, gamma=0.75):
    output = cv2.imread(path)
    return adjust_gamma(output, gamma=gamma)

def face_vector(input_image):
    faces = facevec.detector(input_image, 1)
    if not faces:
        return None
    f = faces[0]
    shape = facevec.predictor(input_image, f)
    face_descriptor = facevec.face_model.compute_face_descriptor(input_image, shape)
    return face_descriptor

# Data Retrieval and Preparation
s1 = 0
s2 = 1
s3 = 2

print("Retrieving Subject-1 images ...")
nitya = glob.glob(r"C:\Users\Nitya\Downloads\Customer Recommendation systm\Customer Recommendation systm\dataset\nitya\*.jpg")
print("Retrieved {} faces !".format(len(nitya)))

print("Retrieving Subject-2 images ...")
lavanya = glob.glob(r"C:\Users\Nitya\Downloads\Customer Recommendation systm\Customer Recommendation systm\dataset\lavanya\*.jpg")
print("Retrieved {} faces !".format(len(lavanya)))

print("Retrieving Subject-3 images ...")
rahul = glob.glob(r"C:\Users\Nitya\Downloads\Customer Recommendation systm\Customer Recommendation systm\dataset\rahul\*.jpg")
print("Retrieved {} faces !".format(len(rahul)))

vectors = dlib.vectors()
labels = dlib.array()

print("Reading Subject-1 images ...")
for i, sub in enumerate(nitya):
    print("Reading {} of {}\r".format(i, len(nitya)))
    face_vectors = face_vector(read_image(sub))
    if face_vectors is None:
        continue
    vectors.append(dlib.vector(face_vectors))
    labels.append(s1)

print("Reading Subject-2 images ...")
for i, sub in enumerate(lavanya):
    print("Reading {} of {}\r".format(i, len(lavanya)))
    face_vectors = face_vector(read_image(sub))
    if face_vectors is None:
        continue
    vectors.append(dlib.vector(face_vectors))
    labels.append(s2)

print("Reading Unknown images ...")
for i, sub in enumerate(rahul):
    print("Reading {} of {}\r".format(i, len(rahul)))
    face_vectors = face_vector(read_image(sub))
    if face_vectors is None:
        continue
    vectors.append(dlib.vector(face_vectors))
    labels.append(s3)

# Training
vec = np.array(vectors)
lab = np.array(labels)
np.savez('Intelligent_album', vec, lab)

# Data Cleaning
onehotencoder = OneHotEncoder()
lab = lab.reshape(-1, 1)
lab = np.maximum(lab, 0)
y = onehotencoder.fit_transform(lab).toarray()
X = vec

# Train Test Split
x_train, x_test, y_train, y_test = train_test_split(X, lab, test_size=0.2, random_state=0)

# Building Model
classifier = SVC(kernel='rbf', C=10, probability=True)
classifier.fit(x_train, y_train)

# Save the Model
with open('intelligent_album_sni.pickle', 'wb') as handle:
    pickle.dump(classifier, handle)

# Face Detection and Customer Recommendation
pickle_in = open("intelligent_album_sni.pickle", "rb")
classifier = pickle.load(pickle_in)

name = ['nitya', 'lavanya', 'rahul']
font = cv2.FONT_HERSHEY_DUPLEX
cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    if not ret:
        break

    img = cv2.resize(img, (0, 0), fx=2.0, fy=2.0)
    faces = facevec.detector(img, 1)

    if len(faces) > 0:
        for i in range(len(faces)):
            f = faces[i]
            shapes = facevec.predictor(img, f)
            face_descriptor = facevec.face_model.compute_face_descriptor(img, shapes)
            face_descriptor = np.array(face_descriptor)

            descriptor = face_descriptor.reshape(1, -1)
            gender = classifier.predict_proba(descriptor)

            if int(gender[0][gender.argmax()] * 100) >= 85:
                person = name[gender.argmax()]
                if person == "nitya":
                    requests.get("https://customer-recommend.eu-gb.cf.appdomain.cloud/data?name="+person+
                                 "! Here are your recommendations:\n colgate toothpaste- 7pc, dove soap- 20pc, tata salt- 9pc")
                elif person == "rahul":
                    requests.get("https://customer-recommend.eu-gb.cf.appdomain.cloud/data?name="+person+
                                 "! Here are your recommendations:\n Butterflies wallet- 25pc, Aashirvaad salt- 13pc, Red Bull- 16pc")
                elif person == "lavanya":
                    requests.get("https://customer-recommend.eu-gb.cf.appdomain.cloud/data?name="+person+
                                 "! Here are your recommendations:\n Dark fantasy biscuit- 5pc, nike shoes- 30pc")
                print("active")
                album = gender.argmax()
            else:
                person = 'Unknown'
                album = 2
                requests.get("https://customer-recommend.eu-gb.cf.appdomain.cloud/data?name=new customer! Here are your recommendations:\n Branded Jeans- 50pc, Bata Footware- 43pc")

            cv2.rectangle(img, (f.left(), f.top()), (f.right(), f.top() - 20), (0, 255, 0), -1)
            cv2.rectangle(img, (f.left(), f.top()), (f.right(), f.bottom()), (0, 255, 0), 1)
            cv2.putText(img, person + str(int(gender[0][gender.argmax()] * 100)) + '%', (f.left(), f.top()), font, 0.6,
                        (255, 255, 255), 0)
            cv2.imshow('image', img)

    if cv2.waitKey(41) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
