import cv2
import numpy as np
from matplotlib import pyplot as plt
import os as os
os.chdir(os.path.dirname(__file__))

# Noise Reduction Filtering: Gürültü azaltma filtreleme, bir görüntüdeki gürültüyü azaltmak için kullanılan bir filtreleme türüdür.

# Örnek bir görüntü yükle
image = cv2.imread('./images/noise_reduction_filter.png', 0)  # Gri tonlamalı olarak yükle

# Gürültü azaltma filtreleme işlevi (örnek olarak Gaussian filtreleme kullanılacak)
def noise_reduction_filter(image, kernel_size):
    return cv2.GaussianBlur(image, (kernel_size, kernel_size), 500)

# Gürültü azaltma filtreleme uygula
filtered_image_noise_reduction = noise_reduction_filter(image, 5)  # 5x5 Gaussian filtreleme

# Sonuçları göster
plt.figure(figsize=(8, 4))
plt.subplot(121), plt.imshow(image, cmap='gray'), plt.title('Orijinal Görüntü')
plt.subplot(122), plt.imshow(filtered_image_noise_reduction, cmap='gray'), plt.title('Gürültü Azaltma Filtreleme')
plt.show()