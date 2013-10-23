#!/usr/bin/env python
import glob
import lcatr.schema

my_schema = lcatr.schema.get('ts3_ppump')
results = [lcatr.schema.valid(my_schema)]

files = sorted(glob.glob('*_trap_*.fits'))
data_products = [lcatr.schema.fileref.make(item) for item in files]

results.extend(data_products)
lcatr.schema.write_file(results)
lcatr.schema.validate_file()
