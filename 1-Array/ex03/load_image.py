import PIL.Image
import os
import numpy as np


def ft_load(path: str) -> np.array:
    
    try:
        if not path.lower().endswith(('.jpg', '.jpeg')):
            raise AssertionError("The file must be a jpg or jpeg file.")
        if not os.path.exists(path):
            raise FileNotFoundError("The file does not exist.")
        img = PIL.Image.open(path)
        print(f"The shape of image is: {img.size[1]}, {img.size[0]}, {len(img.split())}")
        return np.array(img)

    except AssertionError as e:
        print(e)
        return ""
