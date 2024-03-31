import cv2
from matplotlib import pyplot as plt
import os as os
os.chdir(os.path.dirname(__file__))

# Bilateral Filtering: Bilateral filtreleme, bir görüntüyü yumuşatmak için kullanılan bir filtreleme türüdür.

# Örnek bir görüntü yükle
image = cv2.imread('./images/lena.png', 0)  # Gri tonlamalı olarak yükle

# Bilateral filtreleme işlevi
def bilateral_filter(image):
    return cv2.bilateralFilter(image, 9, 75, 75)

# Bilateral filtreleme uygula
filtered_image_bilateral = bilateral_filter(image)

# Sonuçları göster
plt.figure(figsize=(8, 4))
plt.subplot(121), plt.imshow(image, cmap='gray'), plt.title('Orijinal Görüntü')
plt.subplot(122), plt.imshow(filtered_image_bilateral, cmap='gray'), plt.title('Bilateral Filtreleme')
plt.show()
