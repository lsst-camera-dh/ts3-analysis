#!/usr/bin/env python
import os
import lsst.eotest.sensor as sensorTest
from lcatr.harness.helpers import dependency_glob

superflat_files = dependency_glob('*_superflat*.fits')
mask_files = dependency_glob('*_mask.fits')

print superflat_files
# Infer the sensor_id from the first dark filename as per LCA-10140.
sensor_id = os.path.basename(superflat_files[0]).split('_')[0]

task = sensorTest.CteTask()
task.run(sensor_id, superflat_files, mask_files)
