from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import numpy as np

# ... (code for loading and cleaning data)

# Train Test Split
x_train, x_test, y_train, y_test = train_test_split(X, lab, test_size=0.2, random_state=0)

# Building Model
classifier = SVC(kernel='rbf', C=10, probability=True)
classifier.fit(x_train, y_train)

# Save the Model
with open('intelligent_album_sni.pickle', 'wb') as handle:
    pickle.dump(classifier, handle)
