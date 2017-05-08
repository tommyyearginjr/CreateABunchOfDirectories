# The following touches files into directories.

from pathlib import Path

for i in range(1, 67):
    pathForDummyFile = './bible/' + str(i) + '/DeleteThisFile.txt'
    Path(pathForDummyFile).touch()
