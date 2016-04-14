#!/usr/bin/python
import sys
import os
import subprocess
import glob

subprocess.call('rm -rf Modules', shell=True)
subprocess.call('rm -rf *lib_hao_*', shell=True)
