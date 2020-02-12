import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Training set
X_train = [[1], [2.5], [5], [10], [12.5]] #maize size
y_train = [[12], [20], [30], [45], [52]] #prices of maize

# Testing set
X_test = [[1], [2.5], [5], [25]] #maize size
y_test = [[10], [21], [29], [65]] #prices of maize

# Train the Linear Regression model and plot a prediction
regressor = LinearRegression()
regressor.fit(X_train, y_train)
xx = np.linspace(0, 30,100)
yy = regressor.predict(xx.reshape(xx.shape[0],1 ))
plt.plot(xx, yy)

# Set the degree of the Polynomial Regression model
quadratic_featurizer = PolynomialFeatures(degree=2)

# This preprocessor transforms an input data matrix into a new data matrix of a given degree
X_train_quadratic = quadratic_featurizer.fit_transform(X_train)
X_test_quadratic = quadratic_featurizer.transform(X_test)

# Train and test the regressor_quadratic model
regressor_quadratic = LinearRegression()
regressor_quadratic.fit(X_train_quadratic, y_train)
xx_quadratic = quadratic_featurizer.transform(xx.reshape(xx.shape[0], 1))

# Plot the graph
plt.plot(xx, regressor_quadratic.predict(xx_quadratic), c='m', linestyle='--')
plt.title('Maize price regressed on kilograms')
plt.xlabel('Size in kilograms')
plt.ylabel('Price in rands')
plt.axis([0, 100, 0, 100])
plt.grid(True)
plt.scatter(X_train, y_train)
plt.show()
print (X_train)
print (X_train_quadratic)
print (X_test)
print (X_test_quadratic)
