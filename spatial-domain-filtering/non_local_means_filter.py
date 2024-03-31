import cv2
from matplotlib import pyplot as plt
import os as os
os.chdir(os.path.dirname(__file__))

# Non-local Means Filtering: Non-local means filtreleme, bir görüntüdeki gürültüyü kaldırmak için kullanılan bir filtreleme türüdür.

# Örnek bir görüntü yükle
image = cv2.imread('./images/lena.png', 0)  # Load as grayscale

# Non-local means filtreleme işlevi
def non_local_means_filter(image):
    return cv2.fastNlMeansDenoising(image, None, 10, 10, 7)

# Non-local means filtreleme uygula
filtered_image_non_local_means = non_local_means_filter(image)

# Sonuçları göster
plt.figure(figsize=(8, 4))
plt.subplot(121), plt.imshow(image, cmap='gray'), plt.title('Orijinal Görüntü')
plt.subplot(122), plt.imshow(filtered_image_non_local_means, cmap='gray'), plt.title('Non-local Means Filtreleme')
plt.show()
