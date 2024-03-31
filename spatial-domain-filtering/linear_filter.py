import cv2
import numpy as np
from matplotlib import pyplot as plt
import os as os
os.chdir(os.path.dirname(__file__))

# Linear Filtering: Lineer filtreleme, bir görüntüdeki her pikselin değerini, bir çekirdek matrisi ile konvolüsyon yaparak değiştirmek için kullanılan bir filtreleme türüdür.

# Örnek bir görüntü yükle
image = cv2.imread('./images/lena.png', 0)  # Load as grayscale

# Lineer filtreleme işlevi
def linear_filter(image, kernel):
    return cv2.filter2D(image, -1, kernel)

# Örnek bir çekirdek matrisi tanımla
kernel = np.ones((3,3), np.float32) / 9  # 3x3 ortalamalama filtresi

# Lineer filtreleme uygula
filtered_image_linear = linear_filter(image, kernel)

# Sonuçları göster
plt.figure(figsize=(8, 4))
plt.subplot(121), plt.imshow(image, cmap='gray'), plt.title('Orijinal Görüntü')
plt.subplot(122), plt.imshow(filtered_image_linear, cmap='gray'), plt.title('Lineer Filtreleme')
plt.show()