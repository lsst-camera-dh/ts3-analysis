#!/usr/bin/env python
import glob
import lcatr.schema

prnu_file = glob.glob('*prnu_values.txt')[0]

results = [lcatr.schema.fileref.make(prnu_file)]

lcatr.schema.write_file(results)
lcatr.schema.validate_file()
