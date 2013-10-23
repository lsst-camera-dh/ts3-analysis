#!/usr/bin/env python
import os
import lsst.eotest.sensor as sensorTest
from lcatr.harness.helpers import dependency_glob

fe55_files = dependency_glob('*fe55_fe55*.fits')
mask_files = dependency_glob('*_mask.fits')

print fe55_files
print mask_files

# Infer the sensor_id from the first Fe55 filename as per LCA-10140.
sensor_id = os.path.basename(fe55_files[0]).split('_')[0]

task = sensorTest.Fe55Task()
task.run(sensor_id, fe55_files, mask_files)

#
# @todo: figure out how to set task.config.chiprob_min in JH context.
#
