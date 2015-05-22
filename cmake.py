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
elif(typ=="titan"):
  os.environ['SPRNG'] = os.environ['SPRNG_DIR']
  os.environ['FFTW']  = "/opt/fftw/3.3.4.0/interlagos"
  os.environ['ACML']  = "/opt/acml/5.3.1/gfortran64"
  com="cmake -DCMAKE_CXX_COMPILER=CC \
             -DCOMPILER_EXTRA_FLAG:STRING='-Wall -O3 -fopenmp -std=c++11' \
             -DCOMPILER_EXTRA_DEF:STRING='-DMPI_HAO' \
             -DMODULE_EXTRA_PATH:STRING='~/cmake/Modules' \
             -DCMAKE_INSTALL_PREFIX:PATH=~/lib_hao/mpi "+dirc
elif(typ=="titan+magma"):
  os.environ['SPRNG'] = os.environ['SPRNG_DIR']
  os.environ['FFTW']  = "/opt/fftw/3.3.4.0/interlagos"
  os.environ['ACML']  = "/opt/acml/5.3.1/gfortran64"
  os.environ['CUDA']  = os.environ['CRAY_CUDATOOLKIT_DIR']
  os.environ['MAGMA'] ="/ccs/home/hshi/magma/magma-1.6.1"
  com="cmake -DCMAKE_CXX_COMPILER=CC \
             -DCOMPILER_EXTRA_FLAG:STRING='-Wall -O3 -fopenmp -std=c++11' \
             -DCOMPILER_EXTRA_DEF:STRING='-DMPI_HAO' \
             -DUSE_MAGMA=on \
             -DMODULE_EXTRA_PATH:STRING='~/cmake/Modules' \
             -DCMAKE_INSTALL_PREFIX:PATH=~/lib_hao/mpimagma "+dirc

subprocess.call(com, shell=True )
