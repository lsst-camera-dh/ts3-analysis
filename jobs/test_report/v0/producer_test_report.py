#!/usr/bin/env python
import os
import shutil
import pyfits
import pylab
import lsst.eotest.sensor as sensorTest
from lcatr.harness.helpers import dependency_glob

results_file = dependency_glob('*_eotest_results.fits',
                               jobname='flat_pairs')[0]

# Infer the sensor_id from the results filename.
sensor_id = os.path.basename(results_file).split('_')[0]

shutil.copy(results_file, os.path.basename(results_file))

plots = sensorTest.EOTestPlots(sensor_id, results_file=results_file)

fe55_file = dependency_glob('%s_psf_results*.fits' % sensor_id,
                            jobname='fe55_analysis')[0]
plots.fe55_dists(fe55_file=fe55_file)
pylab.savefig('%s_fe55_dists.png' % sensor_id)

ptc_file = dependency_glob('%s_ptc.fits' % sensor_id, jobname='ptc')[0]
plots.ptcs(ptc_file=ptc_file)
pylab.savefig('%s_ptcs.png' % sensor_id)

detresp_file = dependency_glob('%s_det_response.fits' % sensor_id,
                               jobname='flat_pairs')[0]
plots.linearity(ptc_file=ptc_file, detresp_file=detresp_file)
pylab.savefig('%s_linearity.png' % sensor_id)

plots.gains()
pylab.savefig('%s_gains.png' % sensor_id)

plots.noise()
pylab.savefig('%s_noise.png' % sensor_id)

qe_file = dependency_glob('*%s_QE.fits' % sensor_id, jobname='qe')[0]
plots.qe(qe_file=qe_file)
pylab.savefig('%s_qe.png' % sensor_id)

xtalk_file = dependency_glob('*%s_xtalk_matrix.fits' % sensor_id,
                             jobname='crosstalk')[0]
plots.crosstalk_matrix(xtalk_file=xtalk_file)
pylab.savefig('%s_xtalk.png' % sensor_id)

plots.latex_table('%s_results_table.tex' % sensor_id)
