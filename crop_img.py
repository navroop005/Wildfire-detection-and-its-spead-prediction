import numpy as np
from PIL import Image

def crop_img(img, num, save_prefix='', ret_numpy=False):
    size = img.size
    crop_sizes = []
    for i in range(num):
        for j in range(num):
            x1 = i * size[0]//num
            x2 = x1 + size[0]//num
            y1 = j * size[1]//num
            y2 = y1 + size[1]//num
            crop_sizes.append((x1, y1, x2, y2))

    imgs = []
    for i, s in enumerate(crop_sizes):
        cropped = img.crop(s)
        if ret_numpy:
            imgs.append( np.array(cropped))
        else:
            cropped.save(save_prefix + f'{i}.png')
    if ret_numpy:
        return np.stack(imgs, axis=0)

def get_bands_arr(tile_name, file_no, bands, crop_num, img_size):
    arr = []
    for b in bands:
        file_path = f'./cropped/{tile_name}_{b}_{file_no}.png'
        img = Image.open(file_path).resize(img_size)
        arr.append(crop_img(img, crop_num, ret_numpy=True))
    return np.stack(arr, axis=3)