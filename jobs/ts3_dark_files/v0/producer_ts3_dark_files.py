#!/usr/bin/env python
import os
import shutil
import glob

def copy_files(pattern, rootdir, dest='.', nfiles=2):
    files = sorted(glob.glob(os.path.join(rootdir, pattern)))[:nfiles]
    for item in files:
        print item
        shutil.copy(item, '.')

if __name__ == '__main__':
    datadir='/nfs/farm/g/lsst/u1/testData/SIMData/sensorData/000-00/dark/debug'
    copy_files('*_dark_dark*', datadir, nfiles=5)
