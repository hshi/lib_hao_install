#!/usr/bin/python
import sys
import os
import subprocess
import glob

#Download the custom cmake modules.
print "\033[1m"'Dowload custom cmake modules, move to ~/cmake.'"\033[0m"
subprocess.call('git clone https://github.com/hshi/Modules', shell=True)
subprocess.call('rm -rf ~/cmake', shell=True)
subprocess.call('mkdir ~/cmake', shell=True)
subprocess.call('cp -r Modules ~/cmake', shell=True)

print "\033[1m" "Dowload fftw_lib_hao_0:" "\033[92m"
print "Need fftw library, and FFTW=/PATH/TO/FFTW, e.g. export FFTW='/opt/fftw' " "\033[0m"
subprocess.call('git clone https://github.com/hshi/fftw_lib_hao_0', shell=True)

print "\033[1m" "Dowload kahan_error_analysis_lib_hao_0:""\033[0m"
subprocess.call('git clone https://github.com/hshi/kahan_error_analysis_lib_hao_0', shell=True)

print "\033[1m" "Dowload lattice_lib_hao_0:""\033[0m"
subprocess.call('git clone https://github.com/hshi/lattice_lib_hao_0', shell=True)

print "\033[1m" "Dowload math_lib_hao_0:""\033[0m"
subprocess.call('git clone https://github.com/hshi/math_lib_hao_0', shell=True)

print "\033[1m"  "Dowload matrix_lib_hao_0:" "\033[92m"
print "Need mkl library, and MKL=/PATH/TO/MKL, e.g. export MKL='/opt/intel/mkl' "
print "Or need acml library, and ACML=/PATH/TO/ACML, e.g. export ACML='/usr/local/acml-5.1.0/' "
print "Need magma library(optional), and MAGMA=/PATH/TO/MAGMA, e.g. export MAGMA='/usr/local/intel64/nehalem/magma-1.3.0' " "\033[0m"
subprocess.call('git clone https://github.com/hshi/matrix_lib_hao_0', shell=True)


print "\033[1m"  "Dowload mpi_lib_hao_0:" "\033[92m"
print "Need mpi. " "\033[0m"
subprocess.call('git clone https://github.com/hshi/mpi_lib_hao_0', shell=True)

print "\033[1m"  "Dowload random_lib_hao_0:" "\033[92m"
print "Need sprng library, and SPRNG=/PATH/TO/SPRNG, e.g. export SPRNG='/home/username/sprng/sprng2.0'. "
print "Need gmp library, and GMP=/PATH/TO/GMP, e.g. export GMP='/usr/local/gmp-4.3.2'. " "\033[0m"
subprocess.call('git clone https://github.com/hshi/random_lib_hao_0', shell=True)

print "\033[1m"  "Dowload time_lib_hao_0:" "\033[0m"
subprocess.call('git clone https://github.com/hshi/time_lib_hao_0', shell=True)

print "\033[1m"  "Dowload thread_mc_data_manipulate_lib_hao_1:" "\033[0m"
subprocess.call('git clone https://github.com/hshi/thread_mc_data_manipulate_lib_hao_1', shell=True)
print "1st level Lib_hao, need matrix_lib_hao_0, mpi_lib_hao_0, and kahan_error_analysis_lib_hao_0." "\033[0m"

print "\033[1m"  "\n\n\nDownload finished."
print "Please make sure the dependent libraries have been installed."
print "Set the path to those libraries before install lib_hao." 
print "Run 'python install.py type' to install (type can be found in cmake.py)." "\033[0m"
