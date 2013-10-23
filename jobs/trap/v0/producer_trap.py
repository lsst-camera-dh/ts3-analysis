#!/usr/bin/env python
import os
import pyfits
import lsst.eotest.image_utils as imutils
import lsst.eotest.sensor as sensorTest
from lcatr.harness.helpers import dependency_glob

trap_file = dependency_glob('*_trap_ppump*.fits')[0]
mask_files = dependency_glob('*_mask.fits')

def segment_gains():
    gain_file = pyfits.open(dependency_glob('*_gains.fits')[0])
    gains = {}
    for amp in imutils.allAmps:
        gains[amp] = gain_file[0].header['GAIN%s' % imutils.channelIds[amp]]
    return gains

gains = segment_gains()

# Infer the sensor_id from the first dark filename as per LCA-10140.
sensor_id = os.path.basename(trap_file).split('_')[0]

task = sensorTest.TrapTask()
task.run(sensor_id, trap_file, mask_files, gains)
