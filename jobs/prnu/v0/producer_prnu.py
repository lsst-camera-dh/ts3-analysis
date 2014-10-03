#!/usr/bin/env python
import os
import sys
import pyfits
import lsst.eotest.image_utils as imutils
import lsst.eotest.sensor as sensorTest
from lcatr.harness.helpers import dependency_glob

lambda_files = dependency_glob('*_lambda_*.fits')
correction_image = dependency_glob('*_correction*.fits')[0]
mask_files = dependency_glob('*_mask.fits')

print lambda_files
print correction_image
print mask_files

# Infer the sensor_id from the first input filename as per LCA-10140.
sensor_id = os.path.basename(lambda_files[0]).split('_')[0]

my_glob = dependency_glob('%s_eotest_results_cte.fits' % sensor_id)
print my_glob
sys.stdout.flush()
gain_file = my_glob[0]
gains = sensorTest.EOTestResults(gain_file)['GAIN']

# Handle annoying off-by-one issue in amplifier numbering:
gains = dict([(amp, gains[amp-1]) for amp in range(1, 17)])

task = sensorTest.PrnuTask()
task.run(sensor_id, lambda_files, mask_files, gains, correction_image)
