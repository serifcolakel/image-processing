import cv2
from matplotlib import pyplot as plt
import os as os
os.chdir(os.path.dirname(__file__))

# Gaussian Filtering: Gaussian filtreleme, bir görüntüyü yumuşatmak için kullanılan bir filtreleme türüdür.

# Örnek bir görüntü yükle
image = cv2.imread('./images/lena.png', 0)  # Load as grayscale

# Gaussian filtreleme işlevi
def gaussian_filter(image, kernel_size):
    return cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)

# Gaussian filtreleme uygula
filtered_image_gaussian = gaussian_filter(image, 5)  # 5x5 kernel boyutu kullanılarak Gaussian filtreleme

# Sonuçları göster
plt.figure(figsize=(8, 4))
plt.subplot(121), plt.imshow(image, cmap='gray'), plt.title('Orijinal Görüntü')
plt.subplot(122), plt.imshow(filtered_image_gaussian, cmap='gray'), plt.title('Gaussian Filtreleme')
plt.show()
