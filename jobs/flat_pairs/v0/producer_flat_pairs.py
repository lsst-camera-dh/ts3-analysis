#!/usr/bin/env python
import os
import shutil
import pyfits
import lsst.eotest.image_utils as imutils
import lsst.eotest.sensor as sensorTest
from lcatr.harness.helpers import dependency_glob

flat_files = dependency_glob('*_flat*flat?_*.fits')
mask_files = dependency_glob('*_mask.fits')

# Infer the sensor_id from the first dark filename as per LCA-10140.
sensor_id = os.path.basename(flat_files[0]).split('_')[0]

gain_file = dependency_glob('%s_eotest_results_trap.fits' % sensor_id)[0]
gains = sensorTest.EOTestResults(gain_file)['GAIN']

# Handle annoying off-by-one issue in amplifier numbering:
gains = dict([(amp, gains[amp-1]) for amp in range(1, 17)])

results_file = '%s_eotest_results_flat_pairs.fits' % sensor_id
shutil.copy(gain_file, results_file)
task = sensorTest.FlatPairTask()
task.config.eotest_results_file = results_file
task.run(sensor_id, flat_files, mask_files, gains)
