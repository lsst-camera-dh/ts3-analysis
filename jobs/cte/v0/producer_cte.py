#!/usr/bin/env python
import os
import sys
import shutil
import lsst.eotest.sensor as sensorTest
from lcatr.harness.helpers import dependency_glob

superflat_files = dependency_glob('*_superflat*.fits', jobname='ts3_superflat')
mask_files = dependency_glob('*_mask.fits')

print superflat_files
sys.stdout.flush()

# Infer the sensor_id from the first dark filename as per LCA-10140.
sensor_id = os.path.basename(superflat_files[0]).split('_')[0]

dc_results = dependency_glob('%s_eotest_results.fits' % sensor_id,
                             jobname='dark_current')[0]

# Make a local copy to fill with task results.
shutil.copy(dc_results, os.path.basename(dc_results))
task = sensorTest.CteTask()
task.run(sensor_id, superflat_files, mask_files)
