import sympy
import math
import numpy
from scipy import linalg
from scipy import integrate
import matplotlib.pyplot as pylab
from mpl_toolkits.mplot3d import Axes3D

class ctsLS(LS):
    """ 
    Continuous-time Linear Systems class;
    """
    # this will be the complex variable throughout
    z = sympy.Symbol("z")

    def isControllable(self):
        """
        Returns true if the system is controllable
        and false if it is not.
        """
        controllabilityMatrix = numpy.matrix
