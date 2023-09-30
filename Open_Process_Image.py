import cv2
import numpy as np
from tkinter import filedialog
from tkinter import Tk

#uplod the photo , make it gray if she is not already , resize the image to [600,600] and start
#to ExtractLines
def Open_Process_Image(FilterSize=None, FullPathName=None):
    if FullPathName is None:
        root = Tk()
        root.withdraw()
        FullPathName = filedialog.askopenfilename(title='Select Image', filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff *.tif *.gif *.jp2 *.webp *.pbm *.pgm *.ppm")])

        if not FullPathName:
            return None

    im = cv2.imread(FullPathName)
    dim = im.shape[-1]

    if dim > 1:
        imG = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    else:
        imG = im

    imG = cv2.resize(imG, (600, 600))
    SeamsImg = ExtractLines(imG, FilterSize)

    return SeamsImg
