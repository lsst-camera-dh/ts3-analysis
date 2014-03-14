#!/usr/bin/env python
import glob
import lcatr.schema

trap_file = glob.glob('*_traps.fits')[0]

results = [lcatr.schema.fileref.make(trap_file)]

lcatr.schema.write_file(results)
lcatr.schema.validate_file()
