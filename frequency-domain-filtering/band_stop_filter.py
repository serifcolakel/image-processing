import numpy as np
import cv2
from matplotlib import pyplot as plt
import os as os
os.chdir(os.path.dirname(__file__))

# Band Pass Filtering: Band geçiren filtreler, belirli bir frekans aralığını 
# korurken diğer frekans bileşenlerini bastırmak için kullanılır. 
# Bu, belirli özelliklerin vurgulanması için kullanışlıdır.

image = cv2.imread('./images/noise_reduction_filter.png', 0)  # Load as grayscale

def band_stop_filter(image, lowcut, highcut):
    fft = np.fft.fft2(image)
    fft_shifted = np.fft.fftshift(fft)

    rows, cols = image.shape
    crow, ccol = rows // 2 , cols // 2
    
    mask = np.ones((rows, cols), np.uint8)
    mask[crow-lowcut:crow+lowcut, ccol-lowcut:ccol+lowcut] = 0
    mask[crow-highcut:crow+highcut, ccol-highcut:ccol+highcut] = 1
    
    fft_shifted *= mask
    fft = np.fft.ifftshift(fft_shifted)
    filtered_image = np.fft.ifft2(fft)
    filtered_image = np.abs(filtered_image)
    
    return filtered_image

filtered_image = band_stop_filter(image, 10, 50)

plt.subplot(121),plt.imshow(image, cmap='gray'),plt.title('Original Image')
plt.subplot(122),plt.imshow(filtered_image, cmap='gray'),plt.title('Band Stop Filtered Image')
plt.show()