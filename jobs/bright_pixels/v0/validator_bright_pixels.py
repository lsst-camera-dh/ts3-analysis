#!/usr/bin/env python
import glob
import pyfits
import lsst.eotest.image_utils as imutils
import lcatr.schema

bp_map_file = glob.glob('*bright_pixel_map.fits')[0]
bp_map = pyfits.open(bp_map_file)
results = []
for amp in imutils.allAmps:
    results.append(lcatr.schema.valid(lcatr.schema.get('bright_pixels'),
                                      amp=amp,
                                      bright_pixels=bp_map[amp].header['NBRTPIX'],
                                      bright_columns=bp_map[amp].header['NBRTCOL']))

results.append(lcatr.schema.fileref.make(bp_map_file))

lcatr.schema.write_file(results)
lcatr.schema.validate_file()
