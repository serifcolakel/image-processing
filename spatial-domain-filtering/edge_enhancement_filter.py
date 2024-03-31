import cv2
import numpy as np
from matplotlib import pyplot as plt
import os as os
os.chdir(os.path.dirname(__file__))

# Edge Enhancement Filtering: Kenar geliştirme filtreleme, bir görüntüdeki 
# kenarları vurgulamak için kullanılan bir filtreleme türüdür.

# Örnek bir görüntü yükle
image = cv2.imread('./images/lena.png', 0)  # Load as grayscale

# Kenar geliştirme filtreleme işlevi (örnek olarak Laplacian filtreleme kullanılacak)
def edge_enhancement_filter(image):
    laplacian_kernel = np.array([[0, 1, 0],
                                 [1, -4, 1],
                                 [0, 1, 0]])
    return cv2.filter2D(image, -1, laplacian_kernel)

# Kenar geliştirme filtreleme uygula
filtered_image_edge_enhancement = edge_enhancement_filter(image)

# Sonuçları göster
plt.figure(figsize=(8, 4))
plt.subplot(121), plt.imshow(image, cmap='gray'), plt.title('Orijinal Görüntü')
plt.subplot(122), plt.imshow(filtered_image_edge_enhancement, cmap='gray'), plt.title('Kenar Geliştirme Filtreleme')
plt.show()