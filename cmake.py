#!/usr/bin/python
import sys
import os
import subprocess
typ  = sys.argv[1]
dirc = sys.argv[2]
if(typ=="mpi"):
  com="cmake -DCMAKE_CXX_COMPILER=mpic++ \
             -DCOMPILER_EXTRA_FLAG='-Wall -O3 -std=c++11 -fopenmp -m64' \
             -DCOMPILER_EXTRA_DEF='-DMPI_HAO -DMKL_ILP64' \
             -DMODULE_EXTRA_PATH='~/cmake/Modules/general_local;~/cmake/Modules/lib_hao/mpi' \
             -DCMAKE_INSTALL_PREFIX:PATH=~/lib_hao/mpi "+dirc
elif(typ=="serial"):
  com="cmake -DCOMPILER_EXTRA_FLAG='-Wall -O3 -std=c++11 -fopenmp -m64' \
             -DCOMPILER_EXTRA_DEF='-DMKL_ILP64' \
             -DMODULE_EXTRA_PATH='~/cmake/Modules/general_local;~/cmake/Modules/lib_hao/serial' \
             -DCMAKE_INSTALL_PREFIX:PATH=~/lib_hao/serial "+dirc

subprocess.call(com, shell=True )
