# -*- coding: utf-8 -*-
"""lung_cancer.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18FsLFv3RgL9ul6jyz5Ro0QDI-ZxRElIP
"""

from google.colab import drive
drive.mount('/content/drive')

!pip install --upgrade scikit-learn

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, auc
from sklearn.metrics import accuracy_score, mean_absolute_error , mean_squared_error, confusion_matrix, median_absolute_error,classification_report, f1_score,recall_score,precision_score

lung_cancer = pd.read_csv("/content/drive/MyDrive/Multiple_disease_prediction/lung cancer.csv")

lung_cancer.head()

lung_cancer.shape

lung_cancer.info()

lung_cancer.isnull().sum()

lung_cancer.describe()

print(lung_cancer.GENDER.value_counts())

lung_cancer.replace({"GENDER": {"M": 0, "F": 1}}, inplace = True)

lung_cancer.replace({"LUNG_CANCER": {"NO": 0, "YES": 1}}, inplace = True)

lung_cancer.head()

lung_cancer = lung_cancer[["GENDER", "SMOKING", "YELLOW_FINGERS", "ANXIETY",
       "PEER_PRESSURE", "CHRONIC DISEASE", "FATIGUE ", "ALLERGY ", "WHEEZING",
       "ALCOHOL CONSUMING", "COUGHING", "SHORTNESS OF BREATH",
       "SWALLOWING DIFFICULTY", "CHEST PAIN", "LUNG_CANCER"]]

for i in lung_cancer.columns:

    plt.figure(figsize = (8,5))

    sns.countplot(x = lung_cancer[i], data = lung_cancer, palette = "hls")
    plt.xticks(rotation = 90)

plt.show()

for i in lung_cancer.columns:

    lung_cancer[i].value_counts().plot(kind = "pie", figsize = (5,5), autopct = "%1.1f%%")
    plt.xticks(rotation = 45)
    plt.show()

plt.figure(figsize=(10,5))
plt.hist(x = "AGE", data = lung_cancer)
plt.xticks(rotation = 90)
plt.show()

plt.figure(figsize=(8,5))
sns.countplot(x = "GENDER", data = lung_cancer, hue = "LUNG_CANCER", palette = "hls")
plt.xticks(rotation = 90)
plt.show()

plt.figure(figsize=(8,5))
sns.countplot(x = "COUGHING", data = lung_cancer, hue = "LUNG_CANCER", palette = "hls")
plt.legend(["Cancer", "Not Cancer"])
plt.xticks(rotation = 90)
plt.show()

plt.figure(figsize=(8,5))
sns.countplot(x = "YELLOW_FINGERS", data = lung_cancer, hue = "LUNG_CANCER", palette = "hls")
plt.legend(["Cancer", "Not Cancer"])
plt.xticks(rotation = 90)
plt.show()

plt.figure(figsize=(8,5))
sns.countplot(x = "SHORTNESS OF BREATH", data = lung_cancer, hue = "LUNG_CANCER", palette = "hls")
plt.legend(["Cancer", "Not Cancer"])
plt.xticks(rotation = 90)
plt.show()

plt.figure(figsize=(8,5))
sns.countplot(x = "ANXIETY", data = lung_cancer, hue = "SHORTNESS OF BREATH", palette = "hls")
plt.legend(["Cancer", "Not Cancer"])
plt.xticks(rotation = 90)
plt.show()

plt.figure(figsize = (15,15))
sns.heatmap(lung_cancer.corr(), annot = True, cmap = "RdYlGn")
plt.show()

X = lung_cancer.drop(columns = "LUNG_CANCER", axis = 1)
Y = lung_cancer["LUNG_CANCER"]

print(X)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 3, stratify = Y)

print(X.shape, X_train.shape, X_test.shape)

model = LogisticRegression()

model.fit(X_train, Y_train)

ypred = model.predict(X_test)
accuracy = accuracy_score(ypred,Y_test)
print(accuracy)

from sklearn.metrics import confusion_matrix
conf_matrix= confusion_matrix(ypred,Y_test)
print(conf_matrix)

# Create a heatmap
sns.heatmap(conf_matrix, annot=True, fmt='g', cmap='rainbow', cbar=False,
            xticklabels=['Predicted Negative', 'Predicted Positive'],
            yticklabels=['Actual Negative', 'Actual Positive'])

# Add labels and title
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.title('Confusion Matrix Heatmap')

# Show the plot
plt.show()

X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

print("Accuracy on Training Data: ", training_data_accuracy)

X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

print("Accuracy on Test Data: ", test_data_accuracy)

test_data_accuracy = round(accuracy_score(X_test_prediction, Y_test)*100,2)

print("Accuracy on Test Data: ", test_data_accuracy)

from sklearn.metrics import confusion_matrix
conf_matrix= confusion_matrix(X_test_prediction,Y_test)
print(conf_matrix)

from sklearn.metrics import classification_report
target_names = ['class 0', 'class 1']
print(classification_report(X_test_prediction,Y_test, target_names=target_names))

input_values =(56,2,2,2,1,1,1,1,1,1,1,2,2,1)
#input_values = (61,2,2,2,1,1,2,2,1,2,1,2,2,2)

input_values_as_numpy_array = np.asarray(input_values)
input_values_reshaped = input_values_as_numpy_array.reshape(1,-1)

prediction = model.predict(input_values_reshaped)
print(prediction)

if (prediction[0] == 0):
    print("This Person has not Lung Cancer.")
else:
    print("This Preson has Lung Cancer.")

print(Y)

import pickle

filename = "lung_cancer_model.sav"
pickle.dump(model, open(filename, "wb"))

loaded_model = pickle.load(open("lung_cancer_model.sav", "rb"))

#input_values =(56,2,2,2,1,1,1,1,1,1,1,2,2,1)
input_values = (61,2,2,2,1,1,2,2,1,2,1,2,2,2)

input_values_as_numpy_array = np.asarray(input_values)
input_values_reshaped = input_values_as_numpy_array.reshape(1,-1)

prediction = model.predict(input_values_reshaped)
print(prediction)

if (prediction[0] == 0):
    print("This Person has not Lung Cancer.")
else:
    print("This Preson has Lung Cancer.")