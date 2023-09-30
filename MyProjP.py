import numpy as np

def MyProjP(imB, Sw, Direct):
    R, C = imB.shape  # Get the dimensions (rows and columns) of the input image
    DTimB = np.zeros((R, C), dtype=imB.dtype)  # Initialize an output image (projection) with zeros

    if Direct == 0:
        # Projection in the horizontal direction (left to right)
        for i in range(Sw, C):
            # For each column i, sum the pixel values in a horizontal strip of width Sw
            DTimB[:, i] = np.sum(imB[:, i - Sw + 1:i + 1], axis=1)

        # Copy the last Sw-1 columns to fill the boundary
        for i in range(Sw - 1):
            DTimB[:, i] = DTimB[:, Sw + i]
    else:
        # Projection in the reverse horizontal direction (right to left)
        for i in range(C - Sw, -1, -1):
            # For each column i, sum the pixel values in a horizontal strip of width Sw
            DTimB[:, i] = np.sum(imB[:, i:i + Sw + 1], axis=1)

        # Copy the first Sw columns to fill the boundary
        for i in range(C, C - Sw, -1):
            DTimB[:, i] = DTimB[:, i - Sw]

    return DTimB  # Return the resulting projection image
