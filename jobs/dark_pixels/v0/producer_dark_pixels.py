#!/usr/bin/env python
import os
import sys
import shutil
import pyfits
import lsst.eotest.image_utils as imutils
import lsst.eotest.sensor as sensorTest
from lcatr.harness.helpers import dependency_glob

sflat_files = dependency_glob('*_superflat_500_*.fits', jobname='ts3_superflat')
mask_files = dependency_glob('*_mask.fits', jobname='fe55_analysis')
mask_files.extend(dependency_glob('*_mask.fits', jobname='bright_pixels'))

print sflat_files
print mask_files
sys.stdout.flush()

# Infer the sensor_id from the first superflat filename as per LCA-10140.
sensor_id = os.path.basename(sflat_files[0]).split('_')[0]

# Make a local copy of previous task's results to fill with this
# task's results.
results_file = dependency_glob('%s_eotest_results.fits' % sensor_id,
                               jobname='bright_pixels')[0]
shutil.copy(results_file, os.path.basename(results_file))

task = sensorTest.DarkPixelsTask()
task.run(sensor_id, sflat_files, mask_files)

#
# @todo: Figure out how to set
# task.config.[thresh,colthresh,mask_plane] in JH context.
#
