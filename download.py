#!/usr/bin/python
import sys
import os
import subprocess
import glob

#Download the custom cmake modules.
print 'Dowload custom cmake modules, move the ~/cmake.\n'
subprocess.call('git clone https://github.com/hshi/Modules', shell=True)
subprocess.call('rm -rf ~/cmake', shell=True)
subprocess.call('mkdir ~/cmake', shell=True)
subprocess.call('mv Modules ~/cmake', shell=True)


subprocess.call('git clone https://github.com/hshi/fftw_lib_hao', shell=True)
subprocess.call('git clone https://github.com/hshi/kahan_error_analysis_lib_hao', shell=True)
subprocess.call('git clone https://github.com/hshi/lattice_lib_hao', shell=True)
subprocess.call('git clone https://github.com/hshi/math_lib_hao', shell=True)
subprocess.call('git clone https://github.com/hshi/matrix_lib_hao', shell=True)
subprocess.call('git clone https://github.com/hshi/mpi_lib_hao', shell=True)
subprocess.call('git clone https://github.com/hshi/random_lib_hao', shell=True)
subprocess.call('git clone https://github.com/hshi/time_lib_hao', shell=True)

