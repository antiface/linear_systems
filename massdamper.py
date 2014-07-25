# we define first the continuous time mass-damper system and
# then discretize it using transitions from Hartmut's course

from LS import *
from scipy import linalg
from scipy import integrate

#     [0   1]
# A = [-1  d] corresponds to periodic motion altered by damping d

# first we shall observe the velocity of the object and use 
# output feedback control
md_velocity_feedback = LS([[0, 1],[-1, 1]], [[0],[1]], [0, 1], [0])
D1 = md_velocity_feedback.discretize(0.01)

# now we observe the position of the object in what would seem a much
# trickier control problem
md_position_feedback = LS([[0, 1],[-1, 1]], [[0],[1]], [1, 0], [0])
D2 = md_position_feedback.discretize(0.01)

