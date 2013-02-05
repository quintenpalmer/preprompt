import logging
import logging.config
import os

logger = None
def make_logger():
	global logger
	path = os.path.join(os.environ['pyp'],'etc','pypclient_logger.conf')
	logging.config.fileConfig(path)
	logger = logging.getLogger('pypBasic')
