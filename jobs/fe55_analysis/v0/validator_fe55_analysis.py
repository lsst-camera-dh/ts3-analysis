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

gain_results = {}
foo = pyfits.open(gain_file)
for amp in imutils.allAmps:
    gain_value = foo[0].header['GAIN%s' % imutils.channelIds[amp]]
    gain_results['AMP%02i_GAIN' % amp] = gain_value

results = [lcatr.schema.valid(lcatr.schema.get('fe55_analysis'),
                              **gain_results)]

results.extend([lcatr.schema.fileref.make(x) for x in (psf_results,
                                                       gain_file)])

lcatr.schema.write_file(results)
lcatr.schema.validate_file()
