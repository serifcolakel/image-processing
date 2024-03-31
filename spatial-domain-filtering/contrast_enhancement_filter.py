import cv2
import numpy as np
from matplotlib import pyplot as plt
import os as os
os.chdir(os.path.dirname(__file__))
# Contrast Enhancement Filtering: Kontrast artırma filtreleme, bir görüntüdeki kontrastı artırmak için kullanılan bir filtreleme türüdür.

# Örnek bir görüntü yükle
image = cv2.imread('./images/lena.png', 0)  # Load as grayscale

# Kontrast artırma filtreleme işlevi (örnek olarak CLAHE kullanılacak)
def contrast_enhancement_filter(image):
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    return clahe.apply(image)

# Kontrast artırma filtreleme uygula
filtered_image_contrast_enhancement = contrast_enhancement_filter(image)

# Sonuçları göster
plt.figure(figsize=(8, 4))
plt.subplot(121), plt.imshow(image, cmap='gray'), plt.title('Orijinal Görüntü')
plt.subplot(122), plt.imshow(filtered_image_contrast_enhancement, cmap='gray'), plt.title('Kontrast Artırma Filtreleme')
plt.show()