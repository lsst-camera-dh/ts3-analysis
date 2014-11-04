from eTravelerComponents import Traveler

T03 = Traveler('T03_Simulation_JC', 'CCD', "Jim's Simulated EO Testing")

for test_type in ('system_noise', 'system_xtalk', 'fe55', 'dark', 
                  'spot', 'sflat_500', '_lambda', 'trap', 'flat'):
    name = 'TS3_' + test_type.strip('_')
    exec('%(test_type)s = T03.stepFactory("%(name)s")' % locals())

fe55_analysis = T03.stepFactory('Fe55_Analysis', description='Analysis of Fe55 data for system gain and PSF size')
fe55_analysis.add_pre_req(fe55)

read_noise = T03.stepFactory('Read_Noise', description='CCD Read Noise')
read_noise.add_pre_reqs((system_noise, fe55, fe55_analysis))

bright_pixels = T03.stepFactory('Bright_Pixels', description='Bright pixels and columns from darks')
bright_pixels.add_pre_reqs((dark, fe55_analysis))

dark_pixels = T03.stepFactory('Dark_Pixels', description='Dark pixels and columns from superflat data')
dark_pixels.add_pre_reqs((sflat_500, fe55_analysis, bright_pixels))

traps = T03.stepFactory('Traps', description='Find charge traps from pocket pumping data')
traps.add_pre_reqs((trap, fe55_analysis, bright_pixels, dark_pixels))

mask_generators = fe55_analysis, bright_pixels, dark_pixels, traps

dark_current = T03.stepFactory('Dark_Current', description='Dark current')
dark_current.add_pre_req(dark)
dark_current.add_pre_reqs(mask_generators)

cte = T03.stepFactory('CTE', description='Parallel and serial charge transfer efficiencies')
cte.add_pre_req(sflat_500)
cte.add_pre_reqs(mask_generators)

prnu = T03.stepFactory('PRNU', description='Photo-response non-uniformity')
prnu.add_pre_req(_lambda)
prnu.add_pre_reqs(mask_generators)

flat_pairs = T03.stepFactory('Flat_Pairs', description='Non-linearity and blooming full well from flat pair data')
flat_pairs.add_pre_req(flat)
flat_pairs.add_pre_reqs(mask_generators)

ptc = T03.stepFactory('PTC', description='Photon Transfer Curve')
ptc.add_pre_req(flat)
ptc.add_pre_reqs(mask_generators)

qe = T03.stepFactory('QE', description='Quantum Efficiency')
qe.add_pre_req(_lambda)
qe.add_pre_reqs(mask_generators)

crosstalk = T03.stepFactory('Crosstalk', description='Crosstalk from spot data')
crosstalk.add_pre_reqs((system_xtalk, spot))
crosstalk.add_pre_reqs(mask_generators)

test_report = T03.stepFactory('Test Report', description='Test report')
test_report.add_pre_reqs((fe55_analysis, read_noise, bright_pixels,
                          dark_pixels, traps, dark_current, cte, prnu,
                          flat_pairs, ptc, qe, crosstalk))

T03.write_yml('T03_sim.yml')
T03.write_fakelims_traveler('T03_sim.py')
