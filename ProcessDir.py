import os
from tkinter import filedialog
from tkinter import Tk
#open a geving Dir path and go throw the photos , process them one by one
def ProcessDir(FullDirName=None):
    if FullDirName is None:
        root = Tk()
        root.withdraw()
        FullDirName = filedialog.askdirectory(title='Select Directory')

        if not FullDirName:
            return

    samplesDir = os.listdir(FullDirName)

    for sampleInd, fileName in enumerate(samplesDir[:50], start=1):
        filePath = os.path.join(FullDirName, fileName)
        if os.path.isfile(filePath):
            Open_Process_Image(21, filePath)
