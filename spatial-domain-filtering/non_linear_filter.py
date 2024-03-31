import cv2
import numpy as np
from matplotlib import pyplot as plt
import os as os
os.chdir(os.path.dirname(__file__))

# Non-linear Filtering: Non-lineer filtreleme, bir görüntüdeki her pikselin değerini, komşulukta bulunan piksel değerlerine dayanarak değiştirmek için kullanılan bir filtreleme türüdür.

# Örnek bir görüntü yükle
image = cv2.imread('./images/lena.png', 0)  # Load as grayscale

# Non-lineer filtreleme işlevi (örnek olarak median filtreleme kullanılacak)
def non_linear_filter(image, kernel_size):
    return cv2.medianBlur(image, kernel_size)

# Non-lineer filtreleme uygula
filtered_image_non_linear = non_linear_filter(image, 5)  # 5x5 median filtreleme

# Sonuçları göster
plt.figure(figsize=(8, 4))
plt.subplot(121), plt.imshow(image, cmap='gray'), plt.title('Orijinal Görüntü')
plt.subplot(122), plt.imshow(filtered_image_non_linear, cmap='gray'), plt.title('Non-lineer Filtreleme')
plt.show()