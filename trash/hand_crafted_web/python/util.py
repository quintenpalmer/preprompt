import logging
import logging.config
import os

logger = None
def make_logger():
	global logger
	path = os.path.join(os.environ['pyproot'],'etc','pypweb_logger.conf')
	print path
	logging.config.fileConfig(path)
	logger = logging.getLogger('pypBasic')
