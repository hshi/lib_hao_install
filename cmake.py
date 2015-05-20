#!/usr/bin/python
import sys
import os
import subprocess
typ  = sys.argv[1]
dirc = sys.argv[2]
if(typ=="mpi"):
  com="cmake -DCMAKE_CXX_COMPILER=mpic++ \
             -DCOMPILER_EXTRA_FLAG:STRING='-Wall -O3 -std=c++11' \
             -DCOMPILER_EXTRA_DEF:STRING='-DMPI_HAO' \
             -DMODULE_EXTRA_PATH:STRING='~/cmake/Modules' \
             -DCMAKE_INSTALL_PREFIX:PATH=~/lib_hao/mpi "+dirc
elif(typ=="serial"):
  com="cmake -DCOMPILER_EXTRA_FLAG:STRING='-Wall -O3 -std=c++11' \
             -DCOMPILER_EXTRA_DEF:STRING=' '\
             -DMODULE_EXTRA_PATH:STRING='~/cmake/Modules' \
             -DCMAKE_INSTALL_PREFIX:PATH=~/lib_hao/serial "+dirc
elif(typ=="storm"):
  os.environ['SPRNG'] = "~/sprng2.0"
  com="cmake -DCMAKE_CXX_COMPILER=mpicxx \
             -DCOMPILER_EXTRA_FLAG:STRING='-Wall -O3 -march=barcelona -std=c++11' \
             -DCOMPILER_EXTRA_DEF:STRING='-DMPI_HAO' \
             -DMODULE_EXTRA_PATH:STRING='~/cmake/Modules' \
             -DCMAKE_INSTALL_PREFIX:PATH=~/lib_hao/mpi "+dirc
elif(typ=="hu"):
  os.environ['SPRNG'] = "~/sprng2.0"
  com="cmake -DCMAKE_CXX_COMPILER=mpicxx \
             -DCOMPILER_EXTRA_FLAG:STRING='-Wall -O3 -march=corei7 -m64 -std=c++11' \
             -DCOMPILER_EXTRA_DEF:STRING='-DMPI_HAO' \
             -DMODULE_EXTRA_PATH:STRING='~/cmake/Modules' \
             -DCMAKE_INSTALL_PREFIX:PATH=~/lib_hao/mpi "+dirc
elif(typ=="hu+magma"):
  os.environ['SPRNG'] = "~/sprng2.0"
  com="cmake -DCMAKE_CXX_COMPILER=mpicxx \
             -DCOMPILER_EXTRA_FLAG:STRING='-Wall -O3 -march=corei7 -m64 -std=c++11' \
             -DCOMPILER_EXTRA_DEF:STRING='-DMPI_HAO' \
             -DUSE_MAGMA=on \
             -DMODULE_EXTRA_PATH:STRING='~/cmake/Modules' \
             -DCMAKE_INSTALL_PREFIX:PATH=~/lib_hao/mpimagma "+dirc
subprocess.call(com, shell=True )
