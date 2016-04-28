#!/usr/bin/python
import sys
import os
import subprocess
import glob

typ               = sys.argv[1]

install_dirc_name = '~/lib'

print "\033[1m" "Install custom cmake modules to "+install_dirc_name+"/Modules." "\033[0m"
subprocess.call('rm -rf '+install_dirc_name+'/Modules', shell=True)
subprocess.call('cp -r Modules '+install_dirc_name, shell=True)

print "\033[1m" "Install cmake_code_script to "+install_dirc_name+"/cmake_code_script." "\033[0m"
subprocess.call('rm -rf '+install_dirc_name+'/cmake_code_script', shell=True)
subprocess.call('cp -r cmake_code_script '+install_dirc_name, shell=True)

print "\033[1m" "Install lib_hao level 0 to "+install_dirc_name+"/lib_hao/"+typ+"." "\033[0m"
subprocess.call("python cmake_code_script/lib_install.py "+typ+" '*lib_hao_0' "+ install_dirc_name+"/lib_hao", shell=True )

print "\033[1m" "Install lib_hao level 1 to "+install_dirc_name+"/lib_hao/"+typ+"." "\033[0m"
subprocess.call("python cmake_code_script/lib_install.py "+typ+" '*lib_hao_1' "+ install_dirc_name+"/lib_hao", shell=True )
