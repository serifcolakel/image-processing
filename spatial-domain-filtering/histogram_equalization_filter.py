import cv2
import numpy as np
from matplotlib import pyplot as plt
import os as os
os.chdir(os.path.dirname(__file__))

print('file', os.path.dirname(__file__))

# Örnek bir görüntü yükle
image = cv2.imread('./images/lena.png', 0)  # Gri tonlamalı olarak yükle

# Histogram eşitleme filtreleme işlevi
def histogram_equalization_filter(image):
    return cv2.equalizeHist(image)

# Histogram eşitleme filtreleme uygula
filtered_image_hist_eq = histogram_equalization_filter(image)

# Sonuçları göster
plt.figure(figsize=(8, 4))
plt.subplot(121), plt.imshow(image, cmap='gray'), plt.title('Orijinal Görüntü')
plt.subplot(122), plt.imshow(filtered_image_hist_eq, cmap='gray'), plt.title('Histogram Eşitleme Filtreleme')
plt.show()