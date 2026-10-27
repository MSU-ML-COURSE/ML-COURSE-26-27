import numpy as np

from numpy.testing import assert_allclose
from scalers import StandardScaler, MinMaxScaler


def test_scalers_0():
	with open('scalers.py', 'r') as file:
		lines = ' '.join(file.readlines())
		assert 'import numpy' in lines
		assert 'import typing' in lines
		assert lines.count('import') == 2
		assert 'sklearn' not in lines

def test_scalers_1():
	X_1 = np.random.uniform(-10, 20, (10, 20))

	scaler = StandardScaler()
	scaler.fit(X_1)
	X_2 = scaler.transform(X_1)

	assert type(X_2) == np.ndarray
	assert_allclose(np.mean(X_2, axis=0), np.zeros(20), rtol=1e-05, atol=1e-08)
	assert_allclose(np.std(X_2, axis=0), np.ones(20), rtol=1e-05, atol=1e-08)

def test_scalers_2():
	X_1 = np.random.uniform(-10, 20, (10, 20))

	scaler = MinMaxScaler()
	scaler.fit(X_1)
	X_2 = scaler.transform(X_1)

	assert type(X_2) == np.ndarray
	assert_allclose(np.min(X_2, axis=0), np.zeros(20), rtol=1e-05, atol=1e-08)
	assert_allclose(np.max(X_2, axis=0), np.ones(20), rtol=1e-05, atol=1e-08)

def test_scalers_3():
	X_1 = np.array([[0, 1, 0], [1, 1, 1], [0.3, 0.25, 0.5], [-0.5, -1, 4]])
	X_2 = np.array([[0, 1, 0], [1, 1, 1], [0.3, 0.25, 0.5], [-0.5, -1, 4], [0, 0, 0], [2, -1, 0.5]])

	scaler = StandardScaler()
	scaler.fit(X_1)
	X_3 = scaler.transform(X_2)
	answer = np.array([[-0.36822985,  0.84119102, -0.88354126],
					   [ 1.47291939,  0.84119102, -0.2409658 ],
					   [ 0.18411492, -0.07647191, -0.56225353],
					   [-1.28880447, -1.60591014,  1.68676059],
					   [-0.36822985, -0.38235956, -0.88354126],
					   [ 3.31406862, -1.60591014, -0.56225353]])
	assert type(X_3) == np.ndarray
	assert_allclose(X_3, answer, rtol=1e-05, atol=1e-08)

def test_scalers_4():
	X_1 = np.array([[0, 1, 0], [1, 1, 1], [0.3, 0.25, 0.5], [-0.5, -1, 4]])
	X_2 = np.array([[0, 1, 0], [1, 1, 1], [0.3, 0.25, 0.5], [-0.5, -1, 4], [0, 0, 0], [2, -1, 0.5]])

	scaler = MinMaxScaler()
	scaler.fit(X_1)
	X_3 = scaler.transform(X_2)
	answer = np.array([[0.33333333, 1.        , 0.        ],
					   [1.        , 1.        , 0.25      ],
					   [0.53333333, 0.625     , 0.125     ],
					   [0.        , 0.        , 1.        ],
					   [0.33333333, 0.5       , 0.        ],
					   [1.66666667, 0.        , 0.125     ]])
	assert type(X_3) == np.ndarray
	assert_allclose(X_3, answer, rtol=1e-05, atol=1e-08)
