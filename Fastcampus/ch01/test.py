import cv2
import numpy as np

x = np.array([[[0], [1], [2]]])
print(x)
print(np.squeeze(x))
print(np.squeeze(x, axis=2))