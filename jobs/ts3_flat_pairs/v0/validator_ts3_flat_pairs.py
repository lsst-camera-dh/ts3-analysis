#!/usr/bin/env python
import glob
import lcatr.schema

my_schema = lcatr.schema.get('ts3_flat_pairs')
results = [lcatr.schema.valid(my_schema)]

files = glob.glob('*_flat?*.fits')
data_products = [lcatr.schema.fileref.make(item) for item in files]

results.extend(data_products)
lcatr.schema.write_file(results)
lcatr.schema.validate_file()
