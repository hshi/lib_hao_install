#!/usr/bin/python
import sys
import os
import subprocess
import glob

typ  = sys.argv[1]
if(typ=="mpi"):
  for dirname in glob.glob('*test'): 
      subprocess.call('mpirun -np 4 '+dirname, shell=True )
      sys.stdout.flush()
elif(typ=="serial"):
  for dirname in glob.glob('*test'):
      subprocess.call('./'+dirname, shell=True )
      sys.stdout.flush()
elif(typ=="sciclone"):
  for dirname in glob.glob('*test'):
      subprocess.call('mvp2run ./'+dirname, shell=True )
      sys.stdout.flush()
elif(typ=="titan"):
  for dirname in glob.glob('*test'):
      subprocess.call('aprun ./'+dirname, shell=True )
      sys.stdout.flush()
