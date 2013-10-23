#!/usr/bin/env python
import os
import pyfits
import lsst.eotest.image_utils as imutils
import lsst.eotest.sensor as sensorTest
from lcatr.harness.helpers import dependency_glob

lambda_files = dependency_glob('*_lambda_*.fits')
correction_image = dependency_glob('*_correction*.fits')[0]
mask_files = dependency_glob('*_mask.fits')

print correction_image

def segment_gains():
    gain_file = pyfits.open(dependency_glob('*_gains.fits')[0])
    gains = {}
    for amp in imutils.allAmps:
        gains[amp] = gain_file[0].header['GAIN%s' % imutils.channelIds[amp]]
    return gains

gains = segment_gains()

# Infer the sensor_id from the first input filename as per LCA-10140.
sensor_id = os.path.basename(lambda_files[0]).split('_')[0]

task = sensorTest.PrnuTask()
task.run(sensor_id, lambda_files, mask_files, gains, correction_image)
