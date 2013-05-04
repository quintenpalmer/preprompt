#!/usr/bin/env python

import sys
import os
import subprocess

postprompt_dir = os.environ['postprompt']

def _run_command(command,sub_dir=''):
	cwd = os.path.join(postprompt_dir,sub_dir)
	print subprocess.check_output(command,cwd=cwd)

def javac():
	build_path = os.path.join(os.environ['postprompt'],'build')
	if not os.path.isdir(build_path):
		os.mkdir(build_path)
	_run_command(['javac','-cp','src:src/share/java','-d','build','src/ppbackend/Host.java'])

if __name__ == "__main__":
	javac()
