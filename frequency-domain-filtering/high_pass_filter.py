import numpy as np
import cv2
from matplotlib import pyplot as plt
import os as os
os.chdir(os.path.dirname(__file__))

# High Pass Filtering: Yüksek geçiş filtresi, bir görüntüdeki düşük frekanslı bileşenleri bastırmak için kullanılır. Bu, kenar tespiti gibi işlemler için yararlıdır.

def high_pass_filter(image, kernel_size=3):
    kernel = np.array([[-1, -1, -1],
                       [-1,  8, -1],
                       [-1, -1, -1]])
    return cv2.filter2D(image, -1, kernel)

image = cv2.imread('./images/lena.png', 0)  # Load as grayscale

filtered_image = high_pass_filter(image)

plt.subplot(121),plt.imshow(image, cmap='gray'),plt.title('Original Image')
plt.subplot(122),plt.imshow(filtered_image, cmap='gray'),plt.title('High Pass Filtered Image')
plt.show()