#!/usr/bin/env python
import glob
import pyfits
import lsst.eotest.image_utils as imutils
import lcatr.schema

dc_map_file = glob.glob('*dark_current_map.fits')[0]
dc_map = pyfits.open(dc_map_file)
results = []
for amp in imutils.allAmps:
    dark_current_95CL = dc_map[0].header['DARK95%s' % imutils.channelIds[amp]]
    results.append(lcatr.schema.valid(lcatr.schema.get('dark_current'),
                                      amp=amp,
                                      dark_current_95CL=dark_current_95CL))

results.append(lcatr.schema.fileref.make(dc_map_file))

lcatr.schema.write_file(results)
lcatr.schema.validate_file()
