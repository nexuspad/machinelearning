import numpy as np

class Perceptron (object):
	def __init__(self, eta=0.01, n_iter=10):
		self.eta = eta
		self.n_iter = n_iter

	def fit(self, X, y):
		self._w = np.zeros(1 + X.shape[1])
		self.errors_ = []

		for _ in range(self.n_iter):
			errors = 0
			for xi, target in zip(X, y):
				update = self.eta * (target - self.predict(xi))
				self.W_[1:] += update * xi
				self.W_[0] += update
				errors += int(update != 0.0)
			self.errors_.append(errors)

		return self

	def net_input(self, X):
		return np.doc(X, self.W_[1:]) + self.W_[0]

	def predict(self, X):
		return np.where(self.net_input(X) >= 0.0, 1, -1)