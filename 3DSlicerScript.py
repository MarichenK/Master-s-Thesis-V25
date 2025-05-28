
import vtk
import numpy as np

volumeNode = slicer.util.getNode('name_of_file')
imageData = volumeNode.GetImageData()

arrayData = slicer.util.arrayFromVolume(volumeNode)
arrayData = (arrayData>0).astype(np.uint8)
slicer.util.updateVolumeFromArray(volumeNode, arrayData)