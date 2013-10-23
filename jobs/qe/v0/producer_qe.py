#!/usr/bin/env python
import os
import pyfits
import lsst.eotest.image_utils as imutils
import lsst.eotest.sensor as sensorTest
from lcatr.harness.helpers import dependency_glob

sensorTestDir = os.path.split(sensorTest.__file__)[0]
ccd_cal_file = os.path.join(sensorTestDir, 'qe', 'OD142.csv')
sph_cal_file = os.path.join(sensorTestDir, 'qe', 'OD143.csv')
wlscan_file = os.path.join(sensorTestDir, 'qe', 'WLscan.txt')

lambda_files = dependency_glob('*_lambda_*.fits')
mask_files = dependency_glob('*_mask.fits')

def segment_gains():
    gain_file = pyfits.open(dependency_glob('*_gains.fits')[0])
    gains = {}
    for amp in imutils.allAmps:
        gains[amp] = gain_file[0].header['GAIN%s' % imutils.channelIds[amp]]
    return gains

gains = segment_gains()

# Infer the sensor_id from the first input filename as per LCA-10140.
sensor_id = os.path.basename(lambda_files[0]).split('_')[0]

task = sensorTest.QeTask()
task.run(sensor_id, lambda_files, ccd_cal_file, sph_cal_file,
         wlscan_file, mask_files, gains)
