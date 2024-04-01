import cv2
import numpy as np
from matplotlib import pyplot as plt
import os as os
os.chdir(os.path.dirname(__file__))

# Görüntüyü yükle
image = cv2.imread('./images/lena.png', 0)  # Load as grayscale

# Gaussian kernel oluşturma
kernel_size = (3, 3)
sigma = 1.0

# Gaussian kernel tanımlama : Kenarları yumuşatmak için kullanılır, ortalama alır
gaussian_kernel = cv2.getGaussianKernel(
    kernel_size[0], sigma) * cv2.getGaussianKernel(kernel_size[1], sigma).T

# Laplacian kernel tanımlama : 4 komşu pikselin farkı alınır, kenarları belirlemek için kullanılır
laplacian_kernel = np.array([[0, 1, 0],
                             [1, -4, 1],
                             [0, 1, 0]])

# Sobel kernel tanımlama (X ve Y yönleri için) : Kenarları belirlemek için kullanılır, X yönü kenarları yatayda, Y yönü kenarları dikeyde bulur
sobel_x_kernel = np.array([[-1, 0, 1],
                           [-2, 0, 2],
                           [-1, 0, 1]])

# Sobel kernel tanımlama (X ve Y yönleri için) : Kenarları belirlemek için kullanılır, X yönü kenarları yatayda, Y yönü kenarları dikeyde bulur
sobel_y_kernel = np.array([[-1, -2, -1],
                           [0, 0, 0],
                           [1, 2, 1]])

sobel_x_kernel = sobel_x_kernel / 8.0  # Normalize

#  Ortalama filtresi tanımlama : Kenarları yumuşatmak için kullanılır, ortalama alır (3x3)
mean_filter = np.ones((3, 3)) / 9.0  # 3x3 ortalama filtresi

#  Adaptif filtre tanımlama : Kenarları yumuşatmak için kullanılır, ortalama alır (3x3)
adaptive_filter = np.array([[1, 1, 1],
                            [1, -7, 1],
                            [1, 1, 1]])

#  Adaptif filtre tanımlama : Kenarları yumuşatmak için kullanılır, ortalama alır (3x3)
adaptive_filter = adaptive_filter / 9.0  # Normalize

# Median filter tanımlama : Kenarları yumuşatmak için kullanılır, ortalama alır (3x3) ve ortanca alır
median_filter = np.array([[1, 1, 1],
                          [1, 1, 1],
                          [1, 1, 1]])

median_filter = median_filter / 9.0  # Normalize

# Bandpass ve Bandstop maskesi tanımlama : Frekans alanında filtreleme yapar, düşük frekansları geçirir, yüksek frekansları keser
rows, cols = image.shape
crow, ccol = rows // 2, cols // 2
lowcut, highcut = 10, 50
mask = np.zeros((rows, cols), np.uint8)
# Bandpass maskesi (Düşük frekansları geçirir)
mask[crow-lowcut:crow+lowcut, ccol-lowcut:ccol+lowcut] = 1
mask[crow-highcut:crow+highcut, ccol -
     highcut:ccol+highcut] = 0  # Bandstop maskesi (Yüksek frekansları keser)

# Filtreleri uygula
filtered_image_gaussian = cv2.filter2D(image, -1, gaussian_kernel)
filtered_image_laplacian = cv2.filter2D(image, -1, laplacian_kernel)
filtered_image_sobel_x = cv2.filter2D(image, -1, sobel_x_kernel)
filtered_image_sobel_y = cv2.filter2D(image, -1, sobel_y_kernel)
filtered_image_bandpass = np.fft.ifftshift(
    np.fft.ifft2(np.fft.fftshift(np.fft.fft2(image) * mask))).real
filtered_image_bandstop = np.fft.ifftshift(np.fft.ifft2(
    np.fft.fftshift(np.fft.fft2(image) * (1 - mask)))).real
filtered_image_mean = cv2.filter2D(image, -1, mean_filter)
filtered_image_median = cv2.medianBlur(image, 3)
filtered_image_adaptive = cv2.filter2D(image, -1, adaptive_filter)
filtered_image_median = cv2.filter2D(image, -1, median_filter)
filtered_image_bandpass = np.fft.ifftshift(
    np.fft.ifft2(np.fft.fftshift(np.fft.fft2(image) * mask))).real
filtered_image_bandstop = np.fft.ifftshift(np.fft.ifft2(
    np.fft.fftshift(np.fft.fft2(image) * (1 - mask)))).real

# Sonuçları göster
plt.figure(figsize=(12, 12))
plt.subplot(331), plt.imshow(image, cmap='gray'), plt.title('Orijinal Görüntü')
plt.subplot(332), plt.imshow(filtered_image_gaussian,
                             cmap='gray'), plt.title('Gaussian Filtresi')
plt.subplot(333), plt.imshow(filtered_image_laplacian,
                             cmap='gray'), plt.title('Laplacian Filtresi')
plt.subplot(334), plt.imshow(filtered_image_sobel_x,
                             cmap='gray'), plt.title('Sobel (X) Filtresi')
plt.subplot(335), plt.imshow(filtered_image_sobel_y,
                             cmap='gray'), plt.title('Sobel (Y) Filtresi')
plt.subplot(336), plt.imshow(filtered_image_bandpass,
                             cmap='gray'), plt.title('Bandpass Filtresi')
plt.subplot(337), plt.imshow(filtered_image_bandstop,
                             cmap='gray'), plt.title('Bandstop Filtresi')
plt.subplot(338), plt.imshow(filtered_image_mean,
                             cmap='gray'), plt.title('Ortalama Filtresi')
plt.subplot(339), plt.imshow(filtered_image_median,
                             cmap='gray'), plt.title('Median Filtresi')
plt.subplot(3, 3, 9), plt.imshow(filtered_image_adaptive,
                                 cmap='gray'), plt.title('Adaptif Filtresi')
plt.tight_layout()

plt.show()
