from PIL import Image, ImageEnhance
import numpy as np

'''
Takes a png path or local filename and converts the
image to a numpy array with values from 0 to 1
'''
def pngToArr(file_name):
    # Load the image
    img = Image.open(file_name)
    # Check that the image is in RGB mode
    if img.mode != 'RGB':
        img = img.convert('RGB')
    # Enhance contrast
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.8) # adjust the enhancement factor as needed
    # Convert the image to grayscale
    img = img.convert('L')
    
    # Convert grayscale image to array.
    img_array = np.asarray(img)
    # Reshape the array dimensions (to pass to keras)
    img_array = img_array.reshape((img_array.shape[0], img_array.shape[1], 1))
    # Change values to be from 0 to 1
    img_array = img_array / 255.0
    return img_array

'''
Takes a RAW (.dng) path or local filename and converts the
image to a numpy array with values from 0 to 1
'''
def rawToArr(file_name):
    # Load the DNG image using rawpy
    with rawpy.imread(file_name) as raw:
        # Get the image data as a numpy array
        img_array = raw.postprocess()
    
    # Convert the image to grayscale
    img_array = np.dot(img_array[..., :3], [0.2989, 0.5870, 0.1140])
    
    # Scale the pixel values to be between 0 and 1
    img_array = img_array / 65535.0 # Pixel depth of Samsung S20+ dng images
    
    # Reshape the array dimensions (to pass to keras)
    img_array = img_array.reshape((img_array.shape[0], img_array.shape[1], 1))
    
    return img_array

    
if __name__ == "__main__":
    arr = pngToArr("test.png");
    print(arr)