#!/usr/bin/env python
import os
import shutil
import pyfits
import lsst.eotest.image_utils as imutils
import lsst.eotest.sensor as sensorTest
from lcatr.harness.helpers import dependency_glob

dark_files = dependency_glob('*_dark_dark_*.fits')
mask_files = dependency_glob('*_mask.fits')

print dark_files
print mask_files

# Infer the sensor_id from the first dark filename as per LCA-10140.
sensor_id = os.path.basename(dark_files[0]).split('_')[0]

gain_file = dependency_glob('%s_eotest_results_fe55.fits' % sensor_id)[0]
gains = sensorTest.EOTestResults(gain_file)['GAIN']

# Handle annoying off-by-one issue in amplifier numbering:
gains = dict([(amp, gains[amp-1]) for amp in range(1, 17)])

results_file = '%s_eotest_results_bp.fits' % sensor_id
shutil.copy(gain_file, results_file)
task = sensorTest.BrightPixelsTask()
task.config.eotest_results_file = results_file
task.run(sensor_id, dark_files, mask_files, gains)

#
# @todo: Figure out how to set
# task.config.[ethresh,colthresh,make_plane,temp_tol] in JH context.
#
