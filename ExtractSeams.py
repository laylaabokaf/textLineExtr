import numpy as np
import matplotlib.pyplot as plt

def ExtractSeams(imG, SeamMat, verbos):
    if verbos == 1:
        plt.figure()
        plt.imshow(np.mat2gray(SeamMat))
        plt.title('Energy Map - Distance Transform')
        plt.show()

    Ncols = SeamMat.shape[1]
    LinePeaks = SeamMat[:, 0]

    for i in range(1, 11):
        LinePeaks += SeamMat[:, int(i * Ncols / 21)]

    LinePeaks += np.sum(SeamMat, axis=1)

    if verbos == 1:
        plt.figure()
        plt.plot(LinePeaks)
        plt.title('Line Peaks')
        plt.show()

    min_peak_prominence = 2.5
    _, MinVals1 = findpeaks(LinePeaks, min_peak_prominence, 'extents')
    _, MinVals2 = findpeaks(-LinePeaks, min_peak_prominence, 'extents')

    SeamsImg = np.zeros(imG.shape)

    for ind in range(MinVals1.shape[0]):
        if ind < MinVals1.shape[0] and MinVals1[ind] > 10:
            SeamVector1, _ = findSeamSeed(1 - SeamMat, MinVals1, ind)
            for i in range(SeamVector1.shape[1]):
                SeamsImg[int(SeamVector1[0, i]), i] = 250
            SeamPlot(imG, SeamVector1, 0)

        if ind < MinVals2.shape[0] and MinVals2[ind] > 10:
            SeamVector2, _ = findSeamSeed(SeamMat, MinVals2, ind)
            for i in range(SeamVector2.shape[1]):
                SeamsImg[int(SeamVector2[0, i]), i] = 50
            SeamPlot(imG, SeamVector2, 1)

    plt.figure()
    plt.imshow(np.mat2gray(SeamsImg))
    plt.title('Seams Image')
    plt.show()

# You would need to implement or replace the findpeaks, findSeamSeed, and SeamPlot functions
