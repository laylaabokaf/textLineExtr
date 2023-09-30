import matplotlib.pyplot as plt

def SeamPlot(x, SeamVector, Col):
    plt.figure()
    plt.imshow(x, cmap='gray')
    plt.hold(True)

    if Col == 0:
        plt.plot(SeamVector, '-r')
    elif Col == 1:
        plt.plot(SeamVector, '-b')
    else:
        plt.plot(SeamVector, '-g')

    plt.show()
