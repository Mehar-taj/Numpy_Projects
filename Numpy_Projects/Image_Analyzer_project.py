import numpy as np

image = np.array([
    [10, 50, 200],
    [30, 255, 100],
    [0, 80, 150]
])

print("Original Image:\n", image)

# Shape
print("\nImage Shape:", image.shape)

# Brightest pixel
print("\nMax Pixel Value:", image.max())

# Darkest pixel
print("\nMin Pixel Value:", image.min())

# Average brightness
print("\nAverage Brightness:", image.mean())

# Increase brightness
bright_image = np.clip(image + 25, 0, 255)
print("\nIncreased Brightness:\n", bright_image)

# Flip horizontally
print("\nFlip Image Horizontally:\n", np.fliplr(image))

# Flip vertically
print("\nFlip Image Vertically:\n", np.flipud(image))

# Rotate image
print("\nRotate Image 90°:\n", np.rot90(image))

# Detect bright pixels
print("\nDetect Bright Pixels:", image[image > 200])

# Count dark pixels
print("\nCount Dark Pixels:", np.count_nonzero(image < 50))

# Threshold image
threshold = np.where(image > 128, 255, 0)
print("\nThreshold Image:\n", threshold)