#!/usr/bin/python
import sys
import os
import subprocess
import glob

typ  = sys.argv[1]
com='../cmake.py '+ typ + ' '
path = os.path.abspath(os.path.dirname(__file__))
subprocess.call('rm -rf build', shell=True)
subprocess.call('mkdir build', shell=True)
os.chdir('build')

for dirname in glob.glob(path+'/*lib_hao'):
    subprocess.call('rm -rf *', shell=True)
    subprocess.call(com + dirname, shell=True )
    subprocess.call('make', shell=True )
    subprocess.call('make install', shell=True )


os.chdir('..')
subprocess.call('rm -rf build', shell=True)
