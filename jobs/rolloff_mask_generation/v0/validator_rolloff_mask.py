#!/usr/bin/env python
import lcatr.schema

my_schema = lcatr.schema.get('ccd250_mask_generation')
result_summary = [lcatr.schema.valid(my_schema)]

data_products = [lcatr.schema.fileref.make('ccd250_defects_mask.fits')]
result_summary.extend(data_products)

lcatr.schema.write_file(result_summary)
lcatr.schema.validate_file()
