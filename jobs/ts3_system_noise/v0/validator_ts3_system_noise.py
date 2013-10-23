#!/usr/bin/env python
import glob
import lcatr.schema

my_schema = lcatr.schema.get('ts3_system_noise')
results = [lcatr.schema.valid(my_schema)]

files = sorted(glob.glob('noise_*.fits'))
data_products = [lcatr.schema.fileref.make(item) for item in files]

results.extend(data_products)
lcatr.schema.write_file(results)
lcatr.schema.validate_file()
