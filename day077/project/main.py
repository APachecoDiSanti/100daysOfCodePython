import numpy as np

import matplotlib.pyplot as plt
from scipy import misc # contains an image of a racoon!
from PIL import Image # for reading image files

my_array = np.array([1.1, 9.2, 8.1, 4.7])
my_array.shape
my_array.ndim

array_2d = np.array([[1, 2, 3, 9],
                     [5, 6, 7, 8]])
print(f'array_2d has {array_2d.ndim} dimensions')
print(f'Its shape is {array_2d.shape}')
print(f'It has {array_2d.shape[0]} rows and {array_2d.shape[1]} columns')
print(array_2d)

mystery_array = np.array([[[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[7, 86, 6, 98],
                           [5, 1, 0, 4]],

                          [[5, 36, 32, 48],
                           [97, 0, 27, 18]]])

# Note all the square brackets!
mystery_array.ndim
mystery_array.shape
mystery_array[2][1][3]
mystery_array[2][1]
mystery_array[2][1]
mystery_array[:, :, 0]


# Challenge 1: Use .arange()to createa a vector a with values ranging from 10 to 29. You should get this:
a = np.arange(10, 30)
print(a)

# Challenge 2: Use Python slicing techniques on a to:
# Create an array containing only the last 3 values of a
a[-3:]
# Create a subset with only the 4th, 5th, and 6th values
a[3:6]
# Create a subset of a containing all the values except for the first 12 (i.e., [22, 23, 24, 25, 26, 27, 28, 29])
a[12:]
# Create a subset that only contains the even numbers (i.e, every second number)
a[::2]

# Challenge 3:Reverse the order of the values in a, so that the first element comes last:
np.flip(a)

# Challenge 4: Print out all the indices of the non-zero elements in this array: [6,0,9,0,0,5,0]
b = [6,0,9,0,0,5,0]
for i in range(0, len(b)):
  if b[i] == 0:
    print(i)

# Challenge 5: Use NumPy to generate a 3x3x3 array with random numbers
np.random.rand(3,3,3)

# Challenge 6: Use .linspace() to create a vector x of size 9 with values spaced out evenly between 0 to 100 (both included).
x = np.linspace(0, 100, 9)
x

# Challenge 7: Use .linspace() to create another vector y of size 9 with values between -3 to 3 (both included). Then plot x and y on a line chart using Matplotlib.
y = np.linspace(-3, 3, 9)
y
plt.plot(x, y)
plt.show()

# Challenge 8: Use NumPy to generate an array called noise with shape 128x128x3 that has random values. Then use Matplotlib's .imshow() to display the array as an image.
noise = np.random.rand(128, 128, 3)
print(noise.shape)
plt.imshow(noise)


# Linear Algebra with Vectors
v1 = np.array([4, 5, 2, 7])
v2 = np.array([2, 1, 3, 3])
# Python Lists vs ndarrays
list1 = [4, 5, 2, 7]
list2 = [2, 1, 3, 3]
v1 + v2
v1 * v2

# Broadcasting and Scalars
array_2d = np.array([[1, 2, 3, 4],
                      [5, 6, 7, 8]])
array_2d + 10
array_2d * 5

# Matrix Multiplication with @ and .matmul()
a1 = np.array([[1, 3],
               [0, 1],
               [6, 2],
               [9, 7]])

b1 = np.array([[4, 1, 3],
               [5, 8, 5]])

print(f'{a1.shape}: a has {a1.shape[0]} rows and {a1.shape[1]} columns.')
print(f'{b1.shape}: b has {b1.shape[0]} rows and {b1.shape[1]} columns.')
print('Dimensions of result: (4x2)*(2x3)=(4x3)')
a1 @ b1


# Manipulating Images as ndarrays
img = misc.face()
plt.imshow(img)
type(img)
img.shape
img.ndim


# Challenge: Convert the image to black and white. The values in our img range from 0 to 255.
# Divide all the values by 255 to convert them to sRGB, where all the values are between 0 and 1.
# Next, multiply the sRGB array by the grey_vals to convert the image to grey scale.
# Finally use Matplotlib's .imshow() together with the colormap parameter set to gray cmap=gray to look at the results.
grey_vals = np.array([0.2126, 0.7152, 0.0722])
img_255 = img / 255
img_gray = img_255 @ grey_vals
plt.imshow(img_gray, cmap='gray')

# Challenge: Can you manipulate the images by doing some operations on the underlying ndarrays? See if you can change the values in the ndarray so that:
# 1) You flip the grayscale image upside down
img_flip = np.flip(img_gray)
plt.imshow(img_gray, cmap='gray')

# 2) Rotate the colour image
img_rotated = np.rot90(img)
plt.imshow(img_rotated)

# 3) Invert (i.e., solarize) the colour image. To do this you need to converting all the pixels to their "opposite" value, so black (0) becomes white (255).
solar_img = 255 - img
plt.imshow(solar_img)
