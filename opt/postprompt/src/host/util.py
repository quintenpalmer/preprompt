import logging
import logging.config
import os

logger = None
def make_logger():
	global logger
	path = os.path.join(os.environ['pyproot'],'etc','pyphost_logger.conf')
	print path
	logging.config.fileConfig(path)
	logger = logging.getLogger('pypBasic')

def clear_saves():
	base_dir = os.path.join(os.environ['pyproot'],'opt','postprompt','tables','games')
	paths = os.listdir(base_dir)
	print paths
	for path in paths:
		if path.split('.')[1] == 'save':
			os.remove(os.path.join(base_dir,path))
	print os.listdir(base_dir)
