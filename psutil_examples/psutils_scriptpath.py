"""
Python script path using psutil
"""


import psutil
import os


processes = filter(lambda p: psutil.Process(p).name() == "python", psutil.pids())

scripts = []
paths = []
for pid in processes:
    try:
    	scripts.append(psutil.Process(pid).cmdline()[1])
    except IndexError:
 	pass

for script in scripts:
    paths.append(os.path.abspath(script))

print paths
