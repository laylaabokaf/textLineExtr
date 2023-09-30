import numpy as np
from scipy.ndimage import gaussian_filter

def applyFilters(in, sz, theta, scale, eta):
    responses = -np.inf((len(theta) + 1, sz[0] * sz[1]))

    for idx in range(len(theta)):
        im1 = anigauss(in, scale, eta * scale, theta[idx], 2, 0)
        responses[idx, :] = im1.flatten()

    loc = np.argmax(responses, axis=0)
    response = np.max(responses, axis=0)

    res = loc.reshape(sz[0], sz[1])
    response = response.reshape(sz[0], sz[1])

    return res, response

def anigauss(in_img, scale, eta, theta, sigma, normalize):
    # Implementation of anigauss function goes here (not provided)
    pass
