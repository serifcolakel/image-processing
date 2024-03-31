# Image Processing - Filtering

## Filtreleme

Filtreleme, bir görüntüyü değiştirmek veya geliştirmek için kullanılan bir tekniktir. Filtrelemenin en yaygın formu, görüntünün bir çekirdek ile konvolüsyonu olan lineer filtrelemedir. Çekirdek, görüntünün her pikseline uygulanan küçük bir matristir. Çekirdek genellikle tek boyutlu (örneğin 3x3, 5x5, 7x7 vb.) bir kare matristir. Çekirdek, görüntünün her pikseline uygulanır ve sonuç, çekirdek tarafından değiştirilmiş yeni bir görüntüdür.

Bir görüntüye uygulanabilecek birçok farklı filtre vardır. Bazı yaygın filtreler şunlardır:

- **Gaussian filtresi**: Bir Gaussian filtresi, bir görüntüyü Gaussian çekirdek ile konvolüsyon yaparak bulanıklaştırmak için kullanılır.

- **Median filtresi**: Bir Median filtresi, bir görüntüden gürültüyü kaldırmak için her pikseli komşulukta bulunan piksel değerlerinin ortanca değeriyle değiştirir.

- **Bilateral filtresi**: Bir Bilateral filtresi, kenarları koruyarak bir görüntüyü yumuşatmak için hem mekansal uzaklık hem de renk uzaklığına dayanarak komşulukta bulunan piksel değerlerini ortalamayla bulanıklaştırır.

- **Anisotropic diffusion filtresi**: Bir Anisotropic diffusion filtresi, bir görüntüden gürültüyü kaldırmak için piksel değerlerini görüntünün gradyanına dayanarak komşulukta yayarak yayma işlemi yapar.

- **Non-local means filtresi**: Bir Non-local means filtresi, bir görüntüden gürültüyü kaldırmak için benzer yamaların piksel değerlerini komşulukta bulunan piksel değerlerinin benzerliğine dayanarak ortalamayla bulanıklaştırır.

- **Adaptive filtresi**: Bir Adaptive filtresi, yerel görüntü istatistiklerine dayanarak filtre çekirdeğini ayarlayarak bir görüntüdeki kenarları geliştirmek için kullanılır.

- **Unsharp mask filtresi**: Bir Unsharp mask filtresi, bir görüntüdeki kenarları geliştirmek için orijinal görüntüden bulanık bir versiyonunu çıkartarak kullanılır.

- **High-pass filtresi**: Bir High-pass filtresi, bir görüntüdeki yüksek frekans bileşenlerini orijinal görüntüden düşük frekans bileşenlerini çıkartarak geliştirmek için kullanılır.

- **Low-pass filtresi**: Bir Low-pass filtresi, bir görüntüdeki düşük frekans bileşenlerini komşulukta bulunan piksel değerlerini ortalamayla geliştirmek için kullanılır.

- **Band-pass filtresi**: Bir Band-pass filtresi, bir görüntüdeki frekans bandını geliştirmek için düşük ve yüksek frekansları filtreleyerek kullanılır.

- **Butterworth filtresi**: Bir Butterworth filtresi, bir görüntünün Fourier dönüşümüne Butterworth filtresi uygulayarak frekans bandını geliştirmek için kullanılır.

- **Chebyshev filtresi**: Bir Chebyshev filtresi, bir görüntünün Fourier dönüşümüne Chebyshev filtresi uygulayarak frekans bandını geliştirmek için kullanılır.

- **Elliptic filtresi**: Bir Elliptic filtresi, bir görüntünün Fourier dönüşümüne Elliptic filtresi uygulayarak frekans bandını geliştirmek için kullanılır.

- **Ideal filtresi**: Bir Ideal filtresi, bir görüntünün Fourier dönüşümüne Ideal filtresi uygulayarak frekans bandını geliştirmek için kullanılır.

- **Wiener filtresi**: Bir Wiener filtresi, bir görüntünün Fourier dönüşümüne Wiener filtresi uygulayarak sinyal-gürültü oranını geliştirmek için kullanılır.

- **Kalman filtresi**: Bir Kalman filtresi, bir görüntünün Fourier dönüşümüne Kalman filtresi uygulayarak sinyal-gürültü oranını geliştirmek için kullanılır.

- **Particle filtresi**: Bir Particle filtresi, bir görüntünün Fourier dönüşümüne Particle filtresi uygulayarak sinyal-gürültü oranını geliştirmek için kullanılır.

- **Wavelet filtresi**: Bir Wavelet filtresi, bir görüntünün Fourier dönüşümüne Wavelet filtresi uygulayarak sinyal-gürültü oranını geliştirmek için kullanılır.

- **Haar filtresi**: Bir Haar filtresi, bir görüntünün Fourier dönüşümüne Haar filtresi uygulayarak sinyal-gürültü oranını geliştirmek için kullanılır.

- **Daubechies filtresi**: Bir Daubechies filtresi, bir görüntünün Fourier dönüşümüne Daubechies filtresi uygulayarak sinyal-gürültü oranını geliştirmek için kullanılır.

- **Symlet filtresi**: Bir Symlet filtresi, bir görüntünün Fourier dönüşümüne Symlet filtresi uygulayarak sinyal-gürültü oranını geliştirmek için kullanılır.

- **Coiflet filtresi**: Bir Coiflet filtresi, bir görüntünün Fourier dönüşümüne Coiflet filtresi uygulayarak sinyal-gürültü oranını geliştirmek için kullanılır.

- **Biorthogonal filtresi**: Bir Biorthogonal filtresi, bir görüntünün Fourier dönüşümüne Biorthogonal filtresi uygulayarak sinyal-gürültü oranını geliştirmek için kullanılır.

- **Reverse filtresi**: Bir Reverse filtresi, bir görüntünün Fourier dönüşümüne Reverse filtresi uygulayarak sinyal-gürültü oranını geliştirmek için kullanılır.

- **Inverse filtresi**: Bir Inverse filtresi, bir görüntünün Fourier dönüşümüne Inverse filtresi uygulayarak sinyal-gürültü oranını geliştirmek için kullanılır.

- **Wiener dekonvolüsyon filtresi**: Bir Wiener dekonvolüsyon filtresi, bir görüntünün Fourier dönüşümüne Wiener dekonvolüsyon filtresi uygulayarak sinyal-gürültü oranını geliştirmek için kullanılır.

- **Richardson-Lucy dekonvolüsyon filtresi**: Bir Richardson-Lucy dekonvolüsyon filtresi, bir görüntünün Fourier dönüşümüne Richardson-Lucy dekonvolüsyon filtresi uygulayarak sinyal-gürültü oranını geliştirmek için kullanılır.

- **Maximum likelihood dekonvolüsyon filtresi**: Bir Maximum likelihood dekonvolüsyon filtresi, bir görüntünün Fourier dönüşümüne Maximum likelihood dekonvolüsyon filtresi uygulayarak sinyal-gürültü oranını geliştirmek için kullanılır.

- **Tikhonov regularization filtresi**: Bir Tikhonov regularization filtresi, bir görüntünün Fourier dönüşümüne Tikhonov regularization filtresi uygulayarak sinyal-gürültü oranını geliştirmek için kullanılır.

- **Total variation regularization filtresi**: Bir Total variation regularization filtresi, bir görüntünün Fourier dönüşümüne Total variation regularization filtresi uygulayarak sinyal-gürültü oranını geliştirmek için kullanılır.

- **Non-negative matrix factorization filtresi**: Bir Non-negative matrix factorization filtresi, bir görüntünün Fourier dönüşümüne Non-negative matrix factorization filtresi uygulayarak sinyal-gürültü oranını geliştirmek için kullanılır.

- **Independent component analysis filtresi**: Bir Independent component analysis filtresi, bir görüntünün Fourier dönüşümüne Independent component analysis filtresi uygulayarak sinyal-gürültü oranını geliştirmek için kullanılır.

- **Principal component analysis filtresi**: Bir Principal component analysis filtresi, bir görüntünün Fourier dönüşümüne Principal component analysis filtresi uygulayarak sinyal-gürültü oranını geliştirmek için kullanılır.

- **Linear discriminant analysis filtresi**: Bir Linear discriminant analysis filtresi, bir görüntünün Fourier dönüşümüne Linear discriminant analysis filtresi uygulayarak sinyal-gürültü oranını geliştirmek için kullanılır.

- **Quadratic discriminant analysis filtresi**: Bir Quadratic discriminant analysis filtresi, bir görüntünün Fourier dönüşümüne Quadratic discriminant analysis filtresi uygulayarak sinyal-gürültü oranını geliştirmek için kullanılır.

- **Fisher's linear discriminant filtresi**: Bir Fisher's linear discriminant filtresi, bir görüntünün Fourier dönüşümüne Fisher's linear discriminant filtresi uygulayarak sinyal-gürültü oranını geliştirmek için kullanılır.

- **Kernel discriminant analysis filtresi**: Bir Kernel discriminant analysis filtresi, bir görüntünün Fourier dönüşümüne Kernel discriminant analysis filtresi uygulayarak sinyal-gürültü oranını geliştirmek için kullanılır.

- **Support vector machine filtresi**: Bir Support vector machine filtresi, bir görüntünün Fourier dönüşümüne Support vector machine filtresi uygulayarak sinyal-gürültü oranını geliştirmek için kullanılır.

- **K-nearest neighbors filtresi**: Bir K-nearest neighbors filtresi, bir görüntünün Fourier dönüşümüne K-nearest neighbors filtresi uygulayarak sinyal-gürültü oranını geliştirmek için kullanılır.

- **Decision tree filtresi**: Bir Decision tree filtresi, bir görüntünün Fourier dönüşümüne Decision tree filtresi uygulayarak sinyal-gürültü oranını geliştirmek için kullanılır.

- **Random forest filtresi**: Bir Random forest filtresi, bir görüntünün Fourier dönüşümüne Random forest filtresi uygulayarak sinyal-gürültü oranını geliştirmek için kullanılır.

- **Gradient boosting filtresi**: Bir Gradient boosting filtresi, bir görüntünün Fourier dönüşümüne Gradient boosting filtresi uygulayarak sinyal-gürültü oranını geliştirmek için kullanılır.

- **AdaBoost filtresi**: Bir AdaBoost filtresi, bir görüntünün Fourier dönüşümüne AdaBoost filtresi uygulayarak sinyal-gürültü oranını geliştirmek için kullanılır.

- **XGBoost filtresi**: Bir XGBoost filtresi, bir görüntünün Fourier dönüşümüne XGBoost filtresi uygulayarak sinyal-gürültü oranını geliştirmek için kullanılır.

- **LightGBM filtresi**: Bir LightGBM filtresi, bir görüntünün Fourier dönüşümüne LightGBM filtresi uygulayarak sinyal-gürültü oranını geliştirmek için kullanılır.

- **CatBoost filtresi**: Bir CatBoost filtresi, bir görüntünün Fourier dönüşümüne CatBoost filtresi uygulayarak sinyal-gürültü oranını geliştirmek için kullanılır.

- **Deep learning filtresi**: Bir Deep learning filtresi, bir görüntünün Fourier dönüşümüne Deep learning filtresi uygulayarak sinyal-gürültü oranını geliştirmek için kullanılır.

- **Convolutional neural network filtresi**: Bir Convolutional neural network filtresi, bir görüntünün Fourier dönüşümüne Convolutional neural network filtresi uygulayarak sinyal-gürültü oranını geliştirmek için kullanılır.

- **Recurrent neural network filtresi**: Bir Recurrent neural network filtresi, bir görüntünün Fourier dönüşümüne Recurrent neural network filtresi uygulayarak sinyal-gürültü oranını geliştirmek için kullanılır.

- **Generative adversarial network filtresi**: Bir Generative adversarial network filtresi, bir görüntünün Fourier dönüşümüne Generative adversarial network filtresi uygulayarak sinyal-gürültü oranını geliştirmek için kullanılır.

## Görüntü Filtreleme Türleri

Görüntü Filtreleme, iki ana kategoriye ayrılabilir:

- **Spatiyal Domain Filtering**: Görüntü filtreleme işleminin doğrudan görüntü pikselleri üzerinde gerçekleştirildiği bir filtreleme türüdür.

- **Frequency Domain Filtering**: Görüntü filtreleme işleminin Fourier dönüşümü kullanılarak frekans alanında gerçekleştirildiği bir filtreleme türüdür.

### Spatial Domain Filtering (Uzaysal Alan Filtreleme)

Spatiyal Domain Filtering, bir görüntüdeki her pikselin değerini değiştirmek için doğrudan görüntü pikselleri üzerinde gerçekleştirilen bir filtreleme türüdür. Bu tür filtreleme işlemleri, görüntüdeki her pikselin değerini, komşulukta bulunan piksel değerlerine dayanarak değiştirmek için kullanılır. Spatiyal alan filtreleme işlemleri, görüntüdeki kenarları geliştirmek, gürültüyü kaldırmak, bulanıklığı azaltmak ve diğer görüntü iyileştirme işlemleri için kullanılabilir.

Spatiyal Filtreleme Türleri şunlardır:

- **Linear Filtering**: Lineer filtreleme, bir görüntüdeki her pikselin değerini, bir çekirdek matrisi ile konvolüsyon yaparak değiştirmek için kullanılan bir filtreleme türüdür.

- **Non-linear Filtering**: Non-lineer filtreleme, bir görüntüdeki her pikselin değerini, komşulukta bulunan piksel değerlerine dayanarak değiştirmek için kullanılan bir filtreleme türüdür.

- **Edge Enhancement Filtering**: Kenar geliştirme filtreleme, bir görüntüdeki kenarları geliştirmek için kullanılan bir filtreleme türüdür.

- **Noise Reduction Filtering**: Gürültü azaltma filtreleme, bir görüntüdeki gürültüyü kaldırmak için kullanılan bir filtreleme türüdür.

- **Blurring Filtering**: Bulanıklık filtreleme, bir görüntüdeki bulanıklığı azaltmak için kullanılan bir filtreleme türüdür.

- **Sharpening Filtering**: Keskinleştirme filtreleme, bir görüntüdeki keskinliği artırmak için kullanılan bir filtreleme türüdür.

- **Contrast Enhancement Filtering**: Kontrast artırma filtreleme, bir görüntüdeki kontrastı artırmak için kullanılan bir filtreleme türüdür.

- **Histogram Equalization Filtering**: Histogram eşitleme filtreleme, bir görüntüdeki parlaklık dağılımını düzeltmek için kullanılan bir filtreleme türüdür.

- **Morphological Filtering**: Morfolojik filtreleme, bir görüntüdeki şekil ve yapıları geliştirmek için kullanılan bir filtreleme türüdür.

- **Adaptive Filtering**: Uyarlamalı filtreleme, bir görüntüdeki filtre çekirdeğini otomatik olarak ayarlamak için kullanılan bir filtreleme türüdür.

- **Anisotropic Diffusion Filtering**: Anizotropik difüzyon filtreleme, bir görüntüdeki gürültüyü kaldırmak için kullanılan bir filtreleme türüdür.

- **Non-local Means Filtering**: Non-local means filtreleme, bir görüntüdeki gürültüyü kaldırmak için kullanılan bir filtreleme türüdür.

- **Bilateral Filtering**: Bilateral filtreleme, bir görüntüyü yumuşatmak için kullanılan bir filtreleme türüdür.

- **Median Filtering**: Median filtreleme, bir görüntüden gürültüyü kaldırmak için kullanılan bir filtreleme türüdür.

- **Gaussian Filtering**: Gaussian filtreleme, bir görüntüyü yumuşatmak için kullanılan bir filtreleme türüdür.

### Frequency Domain Filtering (Frekans Alanı Filtreleme)

Frekans Alanı Filtreleme, bir görüntüdeki her pikselin değerini değiştirmek için Fourier dönüşümü kullanılarak frekans alanında gerçekleştirilen bir filtreleme türüdür. Bu tür filtreleme işlemleri, görüntüdeki frekans bileşenlerini değiştirmek için kullanılır. Frekans alanı filtreleme işlemleri, görüntüdeki düşük ve yüksek frekans bileşenlerini geliştirmek, sinyal-gürültü oranını iyileştirmek ve diğer görüntü iyileştirme işlemleri için kullanılabilir.

En çok kullanılan Frekans Alanı Filtreleme Türleri şunlardır:

- **Low-pass Filtering**: Düşük geçişli filtreleme, bir görüntüdeki düşük frekans bileşenlerini geliştirmek için kullanılan bir filtreleme türüdür.

- **High-pass Filtering**: Yüksek geçişli filtreleme, bir görüntüdeki yüksek frekans bileşenlerini geliştirmek için kullanılan bir filtreleme türüdür.

- **Band-pass Filtering**: Band geçişli filtreleme, bir görüntüdeki belirli bir frekans bandını geliştirmek için kullanılan bir filtreleme türüdür.

- **Butterworth Filtering**: Butterworth filtreleme, bir görüntünün Fourier dönüşümüne Butterworth filtresi uygulayarak frekans bandını geliştirmek için kullanılan bir filtreleme türüdür.

- **Chebyshev Filtering**: Chebyshev filtreleme, bir görüntünün Fourier dönüşümüne Chebyshev filtresi uygulayarak frekans bandını geliştirmek için kullanılan bir filtreleme türüdür.

- **Elliptic Filtering**: Elliptic filtreleme, bir görüntünün Fourier dönüşümüne Elliptic filtresi uygulayarak frekans bandını geliştirmek için kullanılan bir filtreleme türüdür.

- **Ideal Filtering**: Ideal filtreleme, bir görüntünün Fourier dönüşümüne Ideal filtresi uygulayarak frekans bandını geliştirmek için kullanılan bir filtreleme türüdür.

- **Wiener Filtering**: Wiener filtreleme, bir görüntünün Fourier dönüşümüne Wiener filtresi uygulayarak sinyal-gürültü oranını geliştirmek için kullanılan bir filtreleme türüdür.

- **Kalman Filtering**: Kalman filtreleme, bir görüntünün Fourier dönüşümüne Kalman filtresi uygulayarak sinyal-gürültü oranını geliştirmek için kullanılan bir filtreleme türüdür.

- **Particle Filtering**: Particle filtreleme, bir görüntünün Fourier dönüşümüne Particle filtresi uygulayarak sinyal-gürültü oranını geliştirmek için kullanılan bir filtreleme türüdür.

- **Wavelet Filtering**: Wavelet filtreleme, bir görüntünün Fourier dönüşümüne Wavelet filtresi uygulayarak sinyal-gürültü oranını geliştirmek için kullanılan bir filtreleme türüdür.

- **Haar Filtering**: Haar filtreleme, bir görüntünün Fourier dönüşümüne Haar filtresi uygulayarak sinyal-gürültü oranını geliştirmek için kullanılan bir filtreleme türüdür.

- **Daubechies Filtering**: Daubechies filtreleme, bir görüntünün Fourier dönüşümüne Daubechies filtresi uygulayarak sinyal-gürültü oranını geliştirmek için kullanılan bir filtreleme türüdür.

- **Symlet Filtering**: Symlet filtreleme, bir görüntünün Fourier dönüşümüne Symlet filtresi uygulayarak sinyal-gürültü oranını geliştirmek için kullanılan bir filtreleme türüdür.

- **Coiflet Filtering**: Coiflet filtreleme, bir görüntünün Fourier dönüşümüne Coiflet filtresi uygulayarak sinyal-gürültü oranını geliştirmek için kullanılan bir filtreleme türüdür.

- **Biorthogonal Filtering**: Biorthogonal filtreleme, bir görüntünün Fourier dönüşümüne Biorthogonal filtresi uygulayarak sinyal-gürültü oranını geliştirmek için kullanılan bir filtreleme türüdür.

- **Reverse Filtering**: Reverse filtreleme, bir görüntünün Fourier dönüşümüne Reverse filtresi uygulayarak sinyal-gürültü oranını geliştirmek için kullanılan bir filtreleme türüdür.

- **Inverse Filtering**: Inverse filtreleme, bir görüntünün Fourier dönüşümüne Inverse filtresi uygulayarak sinyal-gürültü oranını geliştirmek için kullanılan bir filtreleme türüdür.

- **Wiener Deconvolution Filtering**: Wiener dekonvolüsyon filtreleme, bir görüntünün Fourier dönüşümüne Wiener dekonvolüsyon filtresi uygulayarak sinyal-gürültü oranını geliştirmek için kullanılan bir filtreleme türüdür.

- **Richardson-Lucy Deconvolution Filtering**: Richardson-Lucy dekonvolüsyon filtreleme, bir görüntünün Fourier dönüşümüne Richardson-Lucy dekonvolüsyon filtresi uygulayarak sinyal-gürültü oranını geliştirmek için kullanılan bir filtreleme türüdür.

- **Maximum Likelihood Deconvolution Filtering**: Maximum likelihood dekonvolüsyon filtreleme, bir görüntünün Fourier dönüşümüne Maximum likelihood dekonvolüsyon filtresi uygulayarak sinyal-gürültü oranını geliştirmek için kullanılan bir filtreleme türüdür.

- **Tikhonov Regularization Filtering**: Tikhonov regularization filtreleme, bir görüntünün Fourier dönüşümüne Tikhonov regularization filtresi uygulayarak sinyal-gürültü oranını geliştirmek için kullanılan bir filtreleme türüdür.

- **Total Variation Regularization Filtering**: Total variation regularization filtreleme, bir görüntünün Fourier dönüşümüne Total variation regularization filtresi uygulayarak sinyal-gürültü oranını geliştirmek için kullanılan bir filtreleme türüdür.

- **Non-negative Matrix Factorization Filtering**: Non-negative matrix factorization filtreleme, bir görüntünün Fourier dönüşümüne Non-negative matrix factorization filtresi uygulayarak sinyal-gürültü oranını geliştirmek için kullanılan bir filtreleme türüdür.

## Kaynaklar

- [Image Filtering](<https://en.wikipedia.org/wiki/Filter_(signal_processing)>)

- [Image Processing](https://en.wikipedia.org/wiki/Digital_image_processing)
- [Image Processing - Filtering](https://en.wikipedia.org/wiki/Filtering)

- [Image Filtering](https://en.wikipedia.org/wiki/Image_filter)

- [Image Filtering - Gaussian filter](https://en.wikipedia.org/wiki/Gaussian_filter)

- [Image Filtering - Median filter](https://en.wikipedia.org/wiki/Median_filter)

- [Image Filtering - Bilateral filter](https://en.wikipedia.org/wiki/Bilateral_filter)

- [Image Filtering - Anisotropic diffusion filter](https://en.wikipedia.org/wiki/Anisotropic_diffusion)

- [Image Filtering - Non-local means filter](https://en.wikipedia.org/wiki/Non-local_means)

- [Image Filtering - Adaptive filter](https://en.wikipedia.org/wiki/Adaptive_filter)

- [Image Filtering - Unsharp mask filter](https://en.wikipedia.org/wiki/Unsharp_masking)

- [Image Filtering - High-pass filter](https://en.wikipedia.org/wiki/High-pass_filter)

- [Image Filtering - Low-pass filter](https://en.wikipedia.org/wiki/Low-pass_filter)

- [Image Filtering - Band-pass filter](https://en.wikipedia.org/wiki/Band-pass_filter)

- [Image Filtering - Butterworth filter](https://en.wikipedia.org/wiki/Butterworth_filter)

- [Image Filtering - Chebyshev filter](https://en.wikipedia.org/wiki/Chebyshev_filter)

- [Image Filtering - Elliptic filter](https://en.wikipedia.org/wiki/Elliptic_filter)

- [Image Filtering - Ideal filter](https://en.wikipedia.org/wiki/Ideal_filter)

- [Image Filtering - Wiener filter](https://en.wikipedia.org/wiki/Wiener_filter)

- [Image Filtering - Kalman filter](https://en.wikipedia.org/wiki/Kalman_filter)

- [Image Filtering - Particle filter](https://en.wikipedia.org/wiki/Particle_filter)

- [Image Filtering - Wavelet filter](https://en.wikipedia.org/wiki/Wavelet_filter)

- [Image Filtering - Haar filter](https://en.wikipedia.org/wiki/Haar_wavelet)

- [Image Filtering - Daubechies filter](https://en.wikipedia.org/wiki/Daubechies_wavelet)

- [Image Filtering - Symlet filter](https://en.wikipedia.org/wiki/Symlet)

- [Image Filtering - Coiflet filter](https://en.wikipedia.org/wiki/Coiflet)

- [Image Filtering - Biorthogonal filter](https://en.wikipedia.org/wiki/Biorthogonal_wavelet)

- [Image Filtering - Reverse filter](https://en.wikipedia.org/wiki/Reverse_wavelet)

- [Image Filtering - Inverse filter](https://en.wikipedia.org/wiki/Inverse_wavelet)

- [Image Filtering - Wiener deconvolution filter](https://en.wikipedia.org/wiki/Wiener_deconvolution)

- [Image Filtering - Richardson-Lucy deconvolution filter](https://en.wikipedia.org/wiki/Richardson%E2%80%93Lucy_deconvolution)

- [Image Filtering - Maximum likelihood deconvolution filter](https://en.wikipedia.org/wiki/Maximum_likelihood_deconvolution)

- [Image Filtering - Tikhonov regularization filter](https://en.wikipedia.org/wiki/Tikhonov_regularization)

- [Image Filtering - Total variation regularization filter](https://en.wikipedia.org/wiki/Total_variation_regularization)

- [Image Filtering - Non-negative matrix factorization filter](https://en.wikipedia.org/wiki/Non-negative_matrix_factorization)

- [Image Filtering - Independent component analysis filter](https://en.wikipedia.org/wiki/Independent_component_analysis)

- [Image Filtering - Principal component analysis filter](https://en.wikipedia.org/wiki/Principal_component_analysis)

- [Image Filtering - Linear discriminant analysis filter](https://en.wikipedia.org/wiki/Linear_discriminant_analysis)

- [Image Filtering - Quadratic discriminant analysis filter](https://en.wikipedia.org/wiki/Quadratic_discriminant_analysis)

- [Image Filtering - Fisher's linear discriminant filter](https://en.wikipedia.org/wiki/Fisher%27s_linear_discriminant)

- [Image Filtering - Kernel discriminant analysis filter](https://en.wikipedia.org/wiki/Kernel_discriminant_analysis)

- [Image Filtering - Support vector machine filter](https://en.wikipedia.org/wiki/Support_vector_machine)

- [Image Filtering - K-nearest neighbors filter](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm)

- [Image Filtering - Decision tree filter](https://en.wikipedia.org/wiki/Decision_tree)

- [Image Filtering - Random forest filter](https://en.wikipedia.org/wiki/Random_forest)

- [Image Filtering - Gradient boosting filter](https://en.wikipedia.org/wiki/Gradient_boosting)

- [Image Filtering - AdaBoost filter](https://en.wikipedia.org/wiki/AdaBoost)

- [Image Filtering - XGBoost filter](https://en.wikipedia.org/wiki/XGBoost)

- [Image Filtering - LightGBM filter](https://en.wikipedia.org/wiki/LightGBM)

- [Image Filtering - CatBoost filter](https://en.wikipedia.org/wiki/CatBoost)

- [Image Filtering - Deep learning filter](https://en.wikipedia.org/wiki/Deep_learning)

- [Image Filtering - Convolutional neural network filter](https://en.wikipedia.org/wiki/Convolutional_neural_network)

- [Image Filtering - Recurrent neural network filter](https://en.wikipedia.org/wiki/Recurrent_neural_network)

- [Image Filtering - Generative adversarial network filter](https://en.wikipedia.org/wiki/Generative_adversarial_network)

- [Image Filtering - Image Processing](https://en.wikipedia.org/wiki/Image_processing)
