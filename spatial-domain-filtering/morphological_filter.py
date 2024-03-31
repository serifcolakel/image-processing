import cv2
import numpy as np
from matplotlib import pyplot as plt
import os as os
os.chdir(os.path.dirname(__file__))

# Morphological Filtering: Morfolojik filtreleme, bir görüntüdeki şekil ve yapıları geliştirmek için kullanılan bir filtreleme türüdür.

# Örnek bir görüntü yükle
image = cv2.imread('./images/lena.png', 0)  # Load as grayscale

# Morfolojik filtreleme işlevi (örnek olarak açma işlemi kullanılacak)
def morphological_filter(image, kernel_size):
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

# Morfolojik filtreleme uygula
filtered_image_morphological = morphological_filter(image, 5)  # 5x5 kernel boyutu kullanılarak açma işlemi

# Sonuçları göster
plt.figure(figsize=(8, 4))
plt.subplot(121), plt.imshow(image, cmap='gray'), plt.title('Orijinal Görüntü')
plt.subplot(122), plt.imshow(filtered_image_morphological, cmap='gray'), plt.title('Morfolojik Filtreleme')
plt.show()