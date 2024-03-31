import cv2
import numpy as np
from matplotlib import pyplot as plt
import os as os
os.chdir(os.path.dirname(__file__))

# Blurring Filtering: Bulanıklık azaltma filtreleme, bir görüntüdeki bulanıklığı azaltmak için kullanılan bir filtreleme türüdür.

# Örnek bir görüntü yükle
image = cv2.imread('./images/lena.png', 0)  # Load as grayscale

# Bulanıklık azaltma filtreleme işlevi (örnek olarak Gaussian filtreleme kullanılacak)
def blur_filter(image, kernel_size):
    return cv2.GaussianBlur(image, (kernel_size, kernel_size), 5)

# Bulanıklık azaltma filtreleme uygula
filtered_image_blur = blur_filter(image, 5)  # 5x5 Gaussian filtreleme

# Sonuçları göster
plt.figure(figsize=(8, 4))
plt.subplot(121), plt.imshow(image, cmap='gray'), plt.title('Orijinal Görüntü')
plt.subplot(122), plt.imshow(filtered_image_blur, cmap='gray'), plt.title('Bulanıklık Azaltma Filtreleme')
plt.show()