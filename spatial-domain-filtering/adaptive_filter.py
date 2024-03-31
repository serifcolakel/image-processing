import cv2
import numpy as np
from matplotlib import pyplot as plt
import os as os
os.chdir(os.path.dirname(__file__))

# Adaptive Filtering: Adaptif filtreleme, bir görüntüdeki filtre çekirdeğini 
# otomatik olarak ayarlamak için kullanılan bir filtreleme türüdür.

# Örnek bir görüntü yükle
image = cv2.imread('./images/lena.png', 0)  # Load as grayscale

# Adaptif filtreleme işlevi (örnek olarak adaptif ortalama filtreleme kullanılacak)
def adaptive_filter(image, kernel_size):
    return cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, kernel_size, 2)

# Adaptif filtreleme uygula
filtered_image_adaptive = adaptive_filter(image, 11)  # 11x11 pencere boyutu kullanılarak adaptif ortalama filtreleme

# Sonuçları göster
plt.figure(figsize=(8, 4))
plt.subplot(121), plt.imshow(image, cmap='gray'), plt.title('Orijinal Görüntü')
plt.subplot(122), plt.imshow(filtered_image_adaptive, cmap='gray'), plt.title('Adaptif Filtreleme')
plt.show()