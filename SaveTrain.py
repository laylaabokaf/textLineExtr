import os
import numpy as np
from PIL import Image

def SaveTrain(imG, SeamMat, SeamsImg, SliceSize):
    Num = 0
    TempimG = np.zeros((600, 620), dtype=imG.dtype)
    TempSeamMat = np.zeros((600, 620), dtype=SeamMat.dtype)

    TempimG[:, 10:-10] = imG
    TempSeamMat[:, 10:-10] = SeamMat

    PathName = 'E:\\ExtractLines'
    os.makedirs(os.path.join(PathName, 'Img'), exist_ok=True)
    os.makedirs(os.path.join(PathName, 'SeamImg'), exist_ok=True)
    os.makedirs(os.path.join(PathName, 'Lbl'), exist_ok=True)

    for i in range(1, 601):
        FullPathNameImg = os.path.join(PathName, 'Img', f'{i}.jpeg')
        FullPathNameSeamImg = os.path.join(PathName, 'SeamImg', f'{i}.jpeg')
        FullPathNameLabel = os.path.join(PathName, 'Lbl', f'{i}.jpeg')

        NextsliceImg = TempimG[:, i - 1:i + SliceSize - 1]
        NextsliceImgSeam = TempSeamMat[:, i - 1:i + SliceSize - 1]
        NextLabel = SeamsImg[:, i - 1]

        Image.fromarray(NextsliceImg).save(FullPathNameImg)
        Image.fromarray(NextsliceImgSeam).save(FullPathNameSeamImg)
        Image.fromarray(NextLabel).save(FullPathNameLabel)
