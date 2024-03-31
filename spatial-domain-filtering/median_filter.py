import cv2
from matplotlib import pyplot as plt
import os as os
os.chdir(os.path.dirname(__file__))


# Median Filtering: Median filtreleme, bir görüntüden gürültüyü kaldırmak için kullanılan bir filtreleme türüdür.

# Örnek bir görüntü yükle
image = cv2.imread('./images/lena.png', 0)  # Load as grayscale

# Median filtreleme işlevi
def median_filter(image, kernel_size):
    return cv2.medianBlur(image, kernel_size)

# Median filtreleme uygula
filtered_image_median = median_filter(image, 5)  # 5x5 kernel boyutu kullanılarak median filtreleme

# Sonuçları göster
plt.figure(figsize=(8, 4))
plt.subplot(121), plt.imshow(image, cmap='gray'), plt.title('Orijinal Görüntü')
plt.subplot(122), plt.imshow(filtered_image_median, cmap='gray'), plt.title('Median Filtreleme')
plt.show()