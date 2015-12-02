#!/usr/bin/python
import sys
import os
import subprocess
import glob

typ  = sys.argv[1]
if(typ=="mpi"):
  for testname in glob.glob('*test'): 
      subprocess.call('mpirun -np 4 '+testname, shell=True )
      sys.stdout.flush()
elif(typ=="serial"):
  for testname in glob.glob('*test'):
      subprocess.call('./'+testname, shell=True )
      sys.stdout.flush()
elif(typ=="mvp"):
  for testname in glob.glob('*test'):
      subprocess.call('mvp2run ./'+testname, shell=True )
      sys.stdout.flush()
elif(typ=="ap"):
  for testname in glob.glob('*test'):
      subprocess.call('aprun ./'+testname, shell=True )
      sys.stdout.flush()
