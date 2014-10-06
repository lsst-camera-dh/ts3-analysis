#!/usr/bin/env python
import glob
import numpy as np
import pyfits
import lsst.eotest.sensor as sensorTest
import lsst.eotest.image_utils as imutils
import lcatr.schema

results = []

read_noise_file = glob.glob('*_eotest_results.fits')[0]
read_noise = sensorTest.EOTestResults(read_noise_file)['READ_NOISE']
for amp in read_noise:
    results.append(lcatr.schema.valid(lcatr.schema.get('read_noise'),
                                      amp=amp, read_noise=read_noise[amp]))

files = glob.glob('*read_noise?*.fits')
files.append(read_noise_file)
data_products = [lcatr.schema.fileref.make(item) for item in files]
results.extend(data_products)

lcatr.schema.write_file(results)
lcatr.schema.validate_file()
