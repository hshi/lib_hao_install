#!/usr/bin/python
import sys
import os
import subprocess
import glob

subprocess.call('rm -rf Modules', shell=True)
subprocess.call('rm -rf *lib_hao_0', shell=True)
subprocess.call('rm -rf *lib_hao_1', shell=True)
