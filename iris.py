from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import pickle

iris = load_iris()
X = iris.data
y = iris.target

std = StandardScaler()
X_std = std.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_std, y, 
                                                    train_size=0.7,
                                                    stratify=y,
                                                    random_state=42)
print('Training the model ...')
model = LogisticRegression()
model.fit(X_train, y_train)
print('Train Score: ', model.score(X_train, y_train))
print('Test Score: ', model.score(X_test, y_test))

print('Saving the model ...')
model.fit(X_std, y) # training on the complete data

f = open('pickles/model.pkl', 'wb')
pickle.dump(model,f)
f.close()

print('Saving the transformers ...')
f = open('pickles/scaler.pkl', 'wb')
pickle.dump(std,f)
f.close()



