#!/usr/bin/env python

import sys
import os
import subprocess
from pptoollib import PPParse

postprompt_dir = os.environ['postprompt']

def _run_command(command,sub_dir=''):
	cwd = os.path.join(postprompt_dir,sub_dir)
	print subprocess.check_output(command,cwd=cwd)

def _verify_build_dir():
	build_path = os.path.join(postprompt_dir,'build')
	if not os.path.isdir(build_path):
		os.mkdir(build_path)

def javac():
	_verify_build_dir()
	_run_command(['javac','-cp','src:lib/java','-d','build','src/ppbackend/Host.java'])

def bashrc():
	with open(os.path.join(os.environ['HOME'],'.bashrc'),'a') as f:
		f.write((
			'\n'
			'# PostPrompt Setup\n'
			'\n'
			'export postprompt=`pwd`\n'
			'export pp=$postprompt\n'
			'export postpromptroot=$postprompt\n'
			'export PATH=$PATH:$postprompt/bin\n'
			'export PYTHONPATH=$PYTHONPATH:$postprompt/lib/python\n'
			'export GOPATH=$postprompt'
			'alias cdpp="cd $postprompt"\n'))
		sys.stdout.write("run 'source ~/.bashrc' to have this take effect\n")

parser = PPParse()
parser.add_command('javac','compiles the java code',javac),
parser.add_command('bashrc','setup your bashrc for the project',bashrc),

if __name__ == "__main__":
	if len(sys.argv) > 1:
		parser.parse()
	else:
		parser.help_text()
