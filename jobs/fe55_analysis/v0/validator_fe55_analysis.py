#!/usr/bin/env python
import glob
import numpy as np
import pyfits
import lsst.eotest.image_utils as imutils
import lcatr.schema

#
# glob the output files from producer script. (If the sensor_id were
# available, then the output filenames could be used explicitly.)
#
gain_file = glob.glob('*_gains.fits')[0]
psf_results = glob.glob('*_psf_results.fits')[0]

results = []
foo = pyfits.open(gain_file)
for amp in imutils.allAmps:
    gain_value = foo[0].header['GAIN%s' % imutils.channelIds[amp]]
    results.append(lcatr.schema.valid(lcatr.schema.get('fe55_analysis'),
                                      amp=amp, gain=gain_value))

results.extend([lcatr.schema.fileref.make(x) for x in (psf_results,
                                                       gain_file)])

lcatr.schema.write_file(results)
lcatr.schema.validate_file()
