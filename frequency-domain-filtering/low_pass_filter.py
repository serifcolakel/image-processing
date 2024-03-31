import numpy as np
import cv2
from matplotlib import pyplot as plt
import os as os
os.chdir(os.path.dirname(__file__))

# Low Pass Filtering: Düşük geçiş filtresi, bir görüntüdeki yüksek frekans bileşenlerini bastırmak için kullanılır. Bu, görüntünün düzleştirilmesine ve pürüzsüzleştirilmesine yardımcı olabilir. Örneğin, bir Gaussian düşük geçiş filtresi uygulayarak yumuşak bir etki elde edebiliriz.

def low_pass_filter(image, kernel_size=3):
    return cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)

image = cv2.imread('./images/lena.png', 0)  # Load as grayscale
filtered_image = low_pass_filter(image)

plt.subplot(121),plt.imshow(image, cmap='gray'),plt.title('Original Image')
plt.subplot(122),plt.imshow(filtered_image, cmap='gray'),plt.title('Low Pass Filtered Image')
plt.show()