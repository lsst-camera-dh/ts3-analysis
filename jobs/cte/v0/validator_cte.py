#!/usr/bin/env python
import glob
import lcatr.schema

cte_file = glob.glob('*eotest_results.fits')[0]

results = [lcatr.schema.fileref.make(cte_file)]

lcatr.schema.write_file(results)
lcatr.schema.validate_file()
