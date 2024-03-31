import cv2
import numpy as np
from matplotlib import pyplot as plt
import os as os
os.chdir(os.path.dirname(__file__))

# Sharpening Filtering: Keskinleştirme filtreleme, bir görüntüdeki keskinliği artırmak için kullanılan bir filtreleme türüdür.

# Load an example image
image = cv2.imread('./images/lena.png', 0)  # Load as grayscale

# Apply histogram equalization
equalized_image = cv2.equalizeHist(image)

# Sharpening filter function (using Laplacian filtering as an example)
def sharpening_filter(image):
    laplacian_kernel = np.array([[0, 1, 0],
                                 [1, -4, 1],
                                 [0, 1, 0]])
    sharpened = cv2.filter2D(image, -1, laplacian_kernel)
    return image - sharpened

# Apply sharpening filter
filtered_image_sharpening = sharpening_filter(equalized_image)

# Display the results
plt.figure(figsize=(8, 4))
plt.subplot(121), plt.imshow(equalized_image, cmap='gray'), plt.title('Equalized Image')
plt.subplot(122), plt.imshow(filtered_image_sharpening, cmap='gray'), plt.title('Sharpening Filter')
plt.show()
