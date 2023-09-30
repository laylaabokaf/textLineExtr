import numpy as np
from filterDocument import filterDocument  # Assuming you have a Python equivalent function for filterDocument
from MyProjP import MyProjP  # Assuming you have a Python equivalent function for MyProjP

def PreProcessImage(imG, FilterSize):
    _, _, imG1 = filterDocument(imG, FilterSize)
    _, _, imG2 = filterDocument(imG, int(0.5 * FilterSize) + 1)
    _, _, imG3 = filterDocument(imG, int(0.25 * FilterSize) + 1)

    imG = 0.3 * (255 - imG) + imG1 + imG2 + imG3
    imG = 255 - imG
    DTimB = MyProjP(imG[0:, :], 80, 0)

    for i in range(1, 11):
        DTimB += MyProjP(imG[0:, :], 20 * i, 1)

    SeamMat = DTimB / np.max(DTimB)

    return SeamMat
