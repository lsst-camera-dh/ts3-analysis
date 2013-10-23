#!/usr/bin/env python
import glob
import numpy as np
import pyfits
import lsst.eotest.image_utils as imutils
import lcatr.schema

read_noise_results = glob.glob('*_read_noise_results.txt')[0]
rn = {}
for line in open(read_noise_results):
    data = line.strip().split()
    amp, read_noise = int(data[0]), float(data[1])
    rn['AMP%02i_READ_NOISE' % amp] = read_noise
    
results = [lcatr.schema.valid(lcatr.schema.get('read_noise'), **rn)]

files = glob.glob('*read_noise*.fits')
files.append(read_noise_results)
data_products = [lcatr.schema.fileref.make(item) for item in files]
results.extend(data_products)

lcatr.schema.write_file(results)
lcatr.schema.validate_file()
