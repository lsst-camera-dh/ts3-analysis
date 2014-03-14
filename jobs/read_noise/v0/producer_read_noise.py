#!/usr/bin/env python
import os
import pyfits
import lsst.eotest.image_utils as imutils
import lsst.eotest.sensor as sensorTest
from lcatr.harness.helpers import dependency_glob

bias_files = dependency_glob('*_fe55_bias_*.fits')
system_noise_files = dependency_glob('noise_*.fits')
mask_files = dependency_glob('*_mask.fits')

# Infer the sensor_id from the first dark filename as per LCA-10140.
sensor_id = os.path.basename(bias_files[0]).split('_')[0]

gain_file = dependency_glob('%s_eotest_results.fits' % sensor_id)[0]
gains = sensorTest.EOTestResults(gain_file)['GAIN']

# Handle annoying off-by-one issue in amplifier numbering:
gains = dict([(amp, gains[amp-1]) for amp in range(1, 17)])

task = sensorTest.ReadNoiseTask()
task.run(sensor_id, bias_files, system_noise_files, mask_files, gains)
