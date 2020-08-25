from PIL import Image
from numpy import asarray, array2string
from skimage.transform import resize
from skimage.filters import threshold_otsu
from skimage.color import rgb2gray
import os

with open('output-lorenz.vonlanthen-dana.shmaria.csv', 'w+') as csvfile:

    for file in os.listdir('images'):
        if not file.endswith('.png'):
            continue

        image = Image.open('images/' + file)
        data = asarray(image)
        data_resized = resize(data, (10,10))
        data_resized_grey = rgb2gray(data_resized)
        threshold = threshold_otsu(data_resized_grey)
        data_resized_binary_bool = data_resized_grey > threshold
        data_resized_binary = data_resized_binary_bool.astype(int)

        row = file + ',' + ','.join(map(str, data_resized_binary.flatten()))
        csvfile.write(row + "\n")
