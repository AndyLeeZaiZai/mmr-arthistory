import unittest
import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from scipy.misc import imread
from skimage.feature import greycomatrix, greycoprops
def GLCMFeatures(image):
    """
    Function that calculate the gray level co-occurrence matrix of an image.

    Coded by An Li
    """
    edges = cv2.Canny(image, 100, 200)
    EdgeImg = plt.imshow(edges, cmap = 'gray')
    plt.subplot(111), plt.imshow(edges, cmap = 'gray')
    plt.xticks([]), plt.yticks([])
    plt.savefig('test\Cannyedge.png', transparent = True, bbox_inches = 'tight')
    img = cv2.imread('test\Cannyedge.png')
    GrayImg = rgb2gray(img)
    #g = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    glcms = greycomatrix(GrayImg, [1], [0, np.pi/4, np.pi/2, 3*np.pi/4], levels=4, normed=True)
    os.remove("test/Cannyedge.png")
    results = greycoprops(glcms, 'contrast')
    results = np.concatenate((results, greycoprops(glcms, 'dissimilarity')))
    results = np.concatenate((results, greycoprops(glcms, 'homogeneity')))
    results = np.concatenate((results, greycoprops(glcms, 'energy')))
    results = np.concatenate((results, greycoprops(glcms, 'correlation')))
    return results

################################################################################
# TESTS
################################################################################

# The unittest module provides nice utilities for testing
# Check out docs at https://docs.python.org/3/library/unittest.html !!!
class TestGLCMFeatures(unittest.TestCase):

    def test_GLCMFeatures(self):
        """Should output the designated features of GCLM"""
        thispath = os.path.dirname(__file__)
        impath = os.path.join("test", "703.jpg")
        img = cv2.imread(os.path.join(thispath, impath))
        features = GLCMFeatures(img)
        print features

# This if statement gets executed when you run this file, so > python color.py
if __name__ == '__main__':
    # It's a convenient way of running unittests!
    unittest.main()
