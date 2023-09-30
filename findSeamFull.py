import numpy as np

def findSeamFull(x, Mins, ind):
    val = 0
    rows, cols = x.shape
    SeamVector = np.zeros(cols, dtype=int)

    for i in range(cols - 1, -1, -1):
        if i == cols - 1:
            j = Mins[ind]
        else:
            if SeamVector[i + 1] == 0:
                Vector = [np.inf, x[SeamVector[i + 1], i], x[SeamVector[i + 1] + 1, i]]
            elif SeamVector[i + 1] == rows - 1:
                Vector = [x[SeamVector[i + 1] - 1, i], x[SeamVector[i + 1], i], np.inf]
            else:
                Vector = [x[SeamVector[i + 1] - 1, i], x[SeamVector[i + 1], i], x[SeamVector[i + 1] + 1, i]]

            v, Index = min((v, Index) for Index, v in enumerate(Vector))
            val += v
            IndexIncrement = Index - 1
            j = SeamVector[i + 1] + IndexIncrement

        SeamVector[i] = j

    return SeamVector, val
