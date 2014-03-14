#!/usr/bin/env python
import glob
import lcatr.schema

xtalk_file = glob.glob('*xtalk_matrix.fits')[0]

results = [lcatr.schema.fileref.make(xtalk_file)]

lcatr.schema.write_file(results)
lcatr.schema.validate_file()
