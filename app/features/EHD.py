import unittest
import numpy as np
import cv2
import os
from SimpleCV import Image, np, EdgeHistogramFeatureExtractor

def EHDFeatures(image):
    """
    Function that calculate the edge histogram of an image.

    Coded by An Li
    """

    img1 = Image(image)

    edgeFeats = EdgeHistogramFeatureExtractor(bins=20)

    results = np.array(edgeFeats.extract(img1))
    #results = edgeFeats.getFieldNames()
    #results = edgeFeats.getNumFields()

    return results

################################################################################
# TESTS
################################################################################

# The unittest module provides nice utilities for testing
# Check out docs at https://docs.python.org/3/library/unittest.html !!!
class TestEHDFeatures(unittest.TestCase):

    def test_EHDFeatures(self):
        """Should output the designated features of EHD"""
        thispath = os.path.dirname(__file__)
        impath1 = os.path.join("test", "1240.jpg")
        img1 = cv2.imread(os.path.join(thispath, impath1))
        a = EHDFeatures(img1)
        impath2 = os.path.join("test", "1239.jpg")
        img2 = cv2.imread(os.path.join(thispath, impath2))
        b = EHDFeatures(img2)
        impath3 = os.path.join("test", "1238.jpg")
        img3 = cv2.imread(os.path.join(thispath, impath3))
        c = EHDFeatures(img3)
        AandB = np.sum(np.square(a-b))
        AandC = np.sum(np.square(a-c))
        print a
        print
        print AandB
        print AandC

# This if statement gets executed when you run this file, so > python color.py
if __name__ == '__main__':
    # It's a convenient way of running unittests!
    unittest.main()
