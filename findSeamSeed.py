import numpy as np

def findSeamSeed(x, Mins, ind):
    val = 0
    rows, cols = x.shape
    SeamVector = np.zeros(cols, dtype=int)

    # Left Half
    for i in range(cols // 2 - 1, -1, -1):
        if i == cols // 2 - 1:
            j = Mins[ind]
        else:
            if SeamVector[i + 1] == 0:
                Vector = [np.inf, x[SeamVector[i + 1], i], x[SeamVector[i + 1] + 1, i]]
            elif SeamVector[i + 1] == rows:
                Vector = [x[SeamVector[i + 1] - 1, i], x[SeamVector[i + 1], i], np.inf]
            else:
                Vector = [2.5 * x[SeamVector[i + 1] - 1, i], x[SeamVector[i + 1], i], 2.5 * x[SeamVector[i + 1] + 1, i]]

            v, Index = min((v, Index) for Index, v in enumerate(Vector))
            val += v
            IndexIncrement = Index - 2
            j = SeamVector[i + 1] + IndexIncrement

        SeamVector[i] = j

    # Right Half
    for i in range(cols // 2, cols):
        if i == cols // 2:
            j = Mins[ind]
        else:
            if SeamVector[i - 1] == 0:
                Vector = [np.inf, x[SeamVector[i - 1], i], x[SeamVector[i - 1] + 1, i]]
            elif SeamVector[i - 1] == rows:
                Vector = [x[SeamVector[i - 1] - 1, i], x[SeamVector[i - 1], i], np.inf]
            else:
                Vector = [x[SeamVector[i - 1] - 1, i], x[SeamVector[i - 1], i], x[SeamVector[i - 1] + 1, i]]

            v, Index = min((v, Index) for Index, v in enumerate(Vector))
            val += v
            IndexIncrement = Index - 2
            j = SeamVector[i - 1] + IndexIncrement

        SeamVector[i] = j

    St = cols // 2 - 20
    Lt = cols // 2 + 20
    Delta = SeamVector[Lt] - SeamVector[St]

    for i in range(40):
        SeamVector[St + i] = SeamVector[St] + (i / 60) * Delta

    return SeamVector, val
