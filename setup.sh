source ~/.bashrc
export SHELL=/bin/bash

#source /afs/slac/g/lsst/software/redhat6-x86_64-64bit-gcc44/DMstack/Winter2013-v6_2/loadLSST.sh

export PATH=/nfs/farm/g/lsst/u1/software/redhat6-x86_64-64bit-gcc44/anaconda/2.0.1/bin:${PATH}
source /nfs/farm/g/lsst/u1/software/redhat6-x86_64-64bit-gcc44/DMstack/Winter2014/loadLSST.sh

export EUPS_PATH=/nfs/slac/g/ki/ki18/jchiang/LSST/DMstack/eups:${EUPS_PATH}

setup eotest
setup mysqlpython
setup scipy

PS1="[eotest]$ "

export LCATR_LIMS_URL="http://localhost:9876/"
export PYTHONPATH=${PYTHONPATH}:/nfs/slac/g/ki/ki18/jchiang/LSST/JH/jh_modules
export VIRTUAL_ENV=/nfs/slac/g/ki/ki18/jchiang/LSST/JH/virtual_env
