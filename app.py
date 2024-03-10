from flask import Flask, request, jsonify
from sklearn.datasets import load_iris
import numpy as np
from sklearn import tree
from iris_decision_tree_classifier import decode as dt_decode
from iris_selfmade_KNN import KNN, euclidean_distance

app = Flask(__name__)

# Load Iris dataset
iris = load_iris()

# Prepare training data excluding test data points
test_ids = [i for i in range(20)] + [i for i in range(50, 70)] + [i for i in range(100, 120)]
train_data = np.delete(iris.data, test_ids, axis=0)
train_target = np.delete(iris.target, test_ids)

# Train Decision Tree Classifier
dt_clf = tree.DecisionTreeClassifier()
dt_clf.fit(train_data, train_target)

# Train KNN Classifier
knn_clf = KNN()
knn_clf.fit(train_data, train_target)

# Connect to SQLite database (if needed)
# Add necessary database operations if you want to store predictions

# Prediction route for Decision Tree Classifier
@app.route('/C:\Users\HP\Desktop\New folder (10)\iris_decision_tree_classifier.py', methods=['POST'])
def predict_decision_tree():
    data = request.json['data']
    prediction = dt_clf.predict([data])[0]
    predicted_species = dt_decode([prediction])[0]  # Decode the predicted number to iris species
    return jsonify({'prediction': predicted_species})

# Prediction route for KNN Classifier
@app.route('/C:\Users\HP\Desktop\New folder (10)\iris_selfmade_KNN.py', methods=['POST'])
def predict_knn():
    data = request.json['data']
    prediction = knn_clf.predict([data])[0]
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)
