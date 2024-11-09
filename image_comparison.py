import numpy as np
from PIL import Image

def calculate_image_difference(img_path1, img_path2):
    # Open images and convert them to grayscale
    img1 = Image.open(img_path1).convert("L")
    img2 = Image.open(img_path2).convert("L")
    
    '''
    # Resize images to the same size if they differ
    if img1.size != img2.size:
        img2 = img2.resize(img1.size)
    '''
    
    # Convert images to NumPy arrays
    arr1 = np.array(img1, dtype=np.float32)
    arr2 = np.array(img2, dtype=np.float32)

    print(arr1)

    # Calculate the absolute difference between the images
    diff = np.abs(arr1 - arr2)
    
    # Calculate the percentage difference
    percentage_diff = (np.sum(diff) / np.sum(arr1)) * 100
    
    return percentage_diff

# Example usage
img_path1 = "img1.jpg"
img_path2 = "img3.jpg"
difference = calculate_image_difference(img_path1, img_path2)
print(f"Percentage Difference: {difference:.2f}%")

