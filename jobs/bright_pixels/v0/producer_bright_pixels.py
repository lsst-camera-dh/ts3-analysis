#!/usr/bin/env python
import os
import pyfits
import lsst.eotest.image_utils as imutils
import lsst.eotest.sensor as sensorTest
from lcatr.harness.helpers import dependency_glob

dark_files = dependency_glob('*_dark_dark_*.fits')
mask_files = dependency_glob('*_mask.fits')

print dark_files
print mask_files

print dependency_glob('*_gains.fits')
def segment_gains():
    gain_file = pyfits.open(dependency_glob('*_gains.fits')[0])
    gains = {}
    for amp in imutils.allAmps:
        gains[amp] = gain_file[0].header['GAIN%s' % imutils.channelIds[amp]]
    return gains

gains = segment_gains()

# Infer the sensor_id from the first dark filename as per LCA-10140.
sensor_id = os.path.basename(dark_files[0]).split('_')[0]

task = sensorTest.BrightPixelsTask()
task.run(sensor_id, dark_files, mask_files, gains)

#
# @todo: Figure out how to set
# task.config.[ethresh,colthresh,make_plane,temp_tol] in JH context.
#
