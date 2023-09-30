import os
import numpy as np
from PIL import Image

def LoadCombineTrain():
    Num = 0
    TempimG = np.zeros((600, 620), dtype=np.uint8)
    TempSeamMat = np.zeros((600, 620), dtype=np.uint8)
    LabelSeam = np.zeros((600, 600), dtype=np.uint8)

    PathName = 'E:\\ExtractLines'

    for i in range(1, 601):
        FullPathNameImg = os.path.join(PathName, 'Img', f'{i}.jpeg')
        FullPathNameSeamImg = os.path.join(PathName, 'SeamImg', f'{i}.jpeg')
        FullPathNameLabel = os.path.join(PathName, 'Lbl', f'{i}.jpeg')

        NextsliceImg = np.array(Image.open(FullPathNameImg))
        NextsliceImgSeam = np.array(Image.open(FullPathNameSeamImg))
        NextLabel = np.array(Image.open(FullPathNameLabel))

        TempimG[:, i + 10] = NextsliceImg[:, 0]
        TempSeamMat[:, i + 10] = NextsliceImgSeam[:, 0]
        LabelSeam[:, i - 1] = NextLabel[:, 0]

    return TempimG, TempSeamMat, LabelSeam
