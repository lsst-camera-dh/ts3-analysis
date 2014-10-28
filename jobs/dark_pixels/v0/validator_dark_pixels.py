#!/usr/bin/env python
import glob
import pyfits
import lsst.eotest.image_utils as imutils
import lcatr.schema

eotest_results = glob.glob('*eotest_results.fits')[0]

mask_file = glob.glob('*dark_pixel_mask.fits')[0]
mask = pyfits.open(mask_file)
results = []
for amp in imutils.allAmps:
    results.append(lcatr.schema.valid(lcatr.schema.get('dark_pixels'),
                                      amp=amp,
                                      dark_pixels=mask[amp].header['NDARKPIX'],
                                      dark_columns=mask[amp].header['NDARKCOL']))

results.append(lcatr.schema.fileref.make(mask_file))
results.append(lcatr.schema.fileref.make(eotest_results))

lcatr.schema.write_file(results)
lcatr.schema.validate_file()
