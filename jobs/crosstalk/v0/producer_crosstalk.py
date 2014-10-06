#!/usr/bin/env python
import os
import lsst.eotest.sensor as sensorTest
from lcatr.harness.helpers import dependency_glob

spot_files = dependency_glob('*_spot_*.fits', jobname='ts3_spot')
mask_files = dependency_glob('*_mask.fits')

# Infer the sensor_id from the first dark filename as per LCA-10140.
sensor_id = os.path.basename(spot_files[0]).split('_')[0]

task = sensorTest.CrosstalkTask()
task.run(sensor_id, spot_files, mask_files)
