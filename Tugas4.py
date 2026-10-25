import imageio.v3 as iio
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt

# 1. Membaca citra (pastikan Anda memiliki file gambar, misal 'input.jpg' di folder yang sama)
try:
    citra_awal = iio.imread('input.jpg')
    
    # 2. Manipulasi menggunakan NumPy dan SciPy ndimage
    # Contoh: Menerapkan Gaussian Filter untuk menghaluskan citra (blur/noise reduction)
    citra_ditingkatkan = ndimage.gaussian_filter(citra_awal, sigma=3)
    
    # Menampilkan citra awal dan citra hasil dengan Matplotlib (opsional untuk screenshot hasil)
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    axes[0].imshow(citra_awal)
    axes[0].set_title('Citra Awal')
    axes[0].axis('off')
    
    axes[1].imshow(citra_ditingkatkan)
    axes[1].set_title('Citra Ditingkatkan (Gaussian Filter)')
    axes[1].axis('off')
    
    plt.tight_layout()
    plt.show()

except FileNotFoundError:
    print("Error: File gambar tidak ditemukan. Pastikan nama file dan path sudah benar.")