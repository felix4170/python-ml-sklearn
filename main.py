import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# Load dataset
data = pd.read_csv('customer_churn.csv')


# Encode categorical variables
Labelencoder = LabelEncoder()
data['Gender'] = Labelencoder.fit_transfrom(data['Gender'])
data['Geography'] = Labelencoder.fit_transform(data['Geography'])


# Feature selection
X = data.drop('Exited', axis=1)
y = data['Exited']

# Train/Test split