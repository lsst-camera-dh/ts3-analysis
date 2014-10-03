#!/usr/bin/env python
import os
import sys
import shutil
import lsst.eotest.sensor as sensorTest
from lcatr.harness.helpers import dependency_glob

superflat_files = dependency_glob('*_superflat*.fits')
mask_files = dependency_glob('*_mask.fits')

print superflat_files
sys.stdout.flush()

# Infer the sensor_id from the first dark filename as per LCA-10140.
sensor_id = os.path.basename(superflat_files[0]).split('_')[0]

dc_results = dependency_glob('%s_eotest_results_dark_current.fits' 
                             % sensor_id)[0]

results_file = '%s_eotest_results_cte.fits' % sensor_id
shutil.copy(dc_results, results_file)
task = sensorTest.CteTask()
task.config.eotest_results_file = results_file
task.run(sensor_id, superflat_files, mask_files)
