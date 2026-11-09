
# ==========================================
# HOW TO CREATE AN ARRAY USING NUMPY
# ==========================================


# BENEFITS OF NUMPY
#
# 1) Normal Python List:
#    - Different data types store korte pare.
#    - Example: [10, 20, 30.5, 'A']
#
# 2) NumPy Array:
#    - Normally homogeneous data type maintain kore.
#    - Mane sob element same data type-er hoy.
#    - NumPy mixed data pele common data type-e convert kore.
#
# Example:
# [1, 2, 3, 4, 5, 6.5] -> Float array
# [1, 2, 3, 4, 5, 'c'] -> String array


# ==========================================
# NUMPY IMPORT OPTIONS
# ==========================================

# Option 1:
# import numpy
# val = numpy.array([1, 2, 3, 4, 5])

# Option 2 (Most popular):
# import numpy as np
# np holo numpy-er short name.
# val = np.array([1, 2, 3, 4, 5])

# Option 3:
from numpy import *

# Ei method-e numpy-r function directly use kora jay.
# Tai array() likhte hoy, np.array() likhte hoy na.


# ==========================================
# 1. CREATE A SIMPLE NUMPY ARRAY
# ==========================================

# array() function diye NumPy array create kora hoy.

# val = array([1, 2, 3, 4, 5, 6])

# print(val)

# Output:
# [1 2 3 4 5 6]


# ==========================================
# 2. ASSIGN DATA TYPE EXPLICITLY
# ==========================================

# dtype use kore array-er data type specify kora jay.

# val = array([1, 2, 3], float)

# Ekhane sob integer value float-e convert hobe.

# print(val)

# Output:
# [1.0 2.0 3.0]

# Another way:
# val = array([1, 2, 3], dtype=float)


# ==========================================
# 3. ACCESS ARRAY ELEMENTS USING LOOP
# ==========================================

# val = array([1, 2, 3, 4, 5, 6])

# for x in val:
#     print(x, end=" ")

# for loop diye array-r prottekta element access kora jay.
# end=" " use korle prottek element same line-e print hobe.

# Output:
# 1 2 3 4 5 6


# ==========================================
# 4. linspace() FUNCTION
# ==========================================

# linspace(start, stop, num)
#
# start = kotha theke value start hobe
# stop  = kothay sesh hobe
# num   = total koyta value generate hobe
#
# linspace() specified range-er moddhe equally spaced
# values generate kore.

# val = linspace(10, 20, 5)

# print(val)

# Output:
# [10.  12.5 15.  17.5 20.]

# Explanation:
# Start = 10
# Stop  = 20
# Total values = 5
#
# Generated values:
# 10, 12.5, 15, 17.5, 20


# ==========================================
# 5. PRINT ELEMENTS USING FOR LOOP
# ==========================================

# for x in val:
#     print(x, end=" ")

# Output:
# 10.0 12.5 15.0 17.5 20.0


# ==========================================
# 6. arange() FUNCTION
# ==========================================

# arange(start, stop, step)
#
# arange() function নির্দিষ্ট range-এর মধ্যে
# equally spaced values generate করে।
#
# start = কোন value থেকে শুরু হবে।
# stop  = কোন value পর্যন্ত যাবে (stop value include হবে না)।
# step  = প্রতিবার কত করে value বাড়বে বা কমবে।
#
# Example:

# val = arange(10, 20, 2)

# print(val)

# Output:
# [10 12 14 16 18]

# Explanation:
# Start = 10
# Stop  = 20
# Step  = 2
#
# Generated values:
# 10, 12, 14, 16, 18
#
# এখানে 10 থেকে শুরু হয়েছে।
# প্রতিবার 2 করে value বৃদ্ধি পেয়েছে।
# কিন্তু 20 include হয়নি।
#
# Using for loop:

# for x in val:
#     print(x, end=" ")

# Output:
# 10 12 14 16 18

## zero dymensional array
zero = array(10)
print(zero)

##one dimensional array
one = array([1,2,3,4,5,6])

##two dymensional array
two = array([[1,2,3],[4,5,6],[7,8,9]])
print(two)

## three dymensional array

three = array([[
[1,2],[3,4]
] ,[
[5,6],[7,8]
] ])
print(three)