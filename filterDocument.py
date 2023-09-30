import numpy as np
import cv2

def filterDocument(im, scales):
    # Get the size (shape) of the input image
    sz = im.shape

    # Check if the image is in color (3 channels); if so, convert it to grayscale
    if len(sz) == 3:
        im = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)

    # If the input image is a boolean image, convert it to an 8-bit image
    if im.dtype == np.bool:
        im = im.astype(np.uint8) * 255

    # Convert the input image to a double-precision floating-point format
    in_img = im.astype(np.double)
    sz = im.shape

    # Set the initial orientation angle to 0
    theta = 0

    # Initialize arrays to store intermediate results
    orientation_map = np.full((sz[0], sz[1]), -np.inf)
    response_map = np.full((2, sz[0] * sz[1]), -np.inf)
    scale_res = np.full((sz[0], sz[1]), -np.inf)

    # Iterate over the provided scales
    for sc in scales:
        scale = sc
        eta = 3

        # Call a function (applyFilters) to perform filtering operations and compute orientation and response maps
        orientation, response = applyFilters(in_img, sz, theta, scale, eta)

        gamma = 2

        # Update the response map based on the computed responses
        response_map[1, :] = (scale**2 * eta)**(gamma/2) * response.flatten()

        # Find the location (index) with the maximum response for each pixel
        loc = np.argmax(response_map, axis=0)

        # Update the response_map to store the maximum responses
        response_map[0, :] = response_map[1, loc]

        # Update the orientation_map and scale_res based on the computed orientation and scale
        orientation_map[loc == 1] = orientation[loc == 1]
        scale_res[loc == 1] = scale

    # Return the computed results
    max_orientation = orientation_map
    max_response = response_map[0, :].reshape(sz)
    return max_orientation, scale_res, max_response

# You would need to implement the `applyFilters` function elsewhere in your code.
