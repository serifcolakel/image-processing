import numpy as np
import cv2
from matplotlib import pyplot as plt
import os as os
os.chdir(os.path.dirname(__file__))

# Band Pass Filtering: Butterworth Filtresi, frekans alanında Butterworth 
# fonksiyonu kullanarak belirli frekans bileşenlerini bastırmak veya korumak için kullanılır.

image = cv2.imread('./images/noise_reduction_filter.png', 0)  # Load as grayscale

def butterworth_low_pass_filter(image, cutoff_frequency, order):
    rows, cols = image.shape
    crow, ccol = rows // 2 , cols // 2

    mask = np.zeros((rows, cols), np.uint8)
    for i in range(rows):
        for j in range(cols):
            distance = np.sqrt((i - crow) ** 2 + (j - ccol) ** 2)
            mask[i, j] = 1 / (1 + (distance / cutoff_frequency) ** (2 * order))
    
    fft = np.fft.fft2(image)
    fft_shifted = np.fft.fftshift(fft)
    fft_shifted *= mask
    fft = np.fft.ifftshift(fft_shifted)
    filtered_image = np.fft.ifft2(fft)
    filtered_image = np.abs(filtered_image)

    return filtered_image

filtered_image = butterworth_low_pass_filter(image, 50, 2)

plt.subplot(121),plt.imshow(image, cmap='gray'),plt.title('Original Image')
plt.subplot(122),plt.imshow(filtered_image, cmap='gray'),plt.title('Butterworth Low Pass Filtered Image')
plt.show()