import logging
import logging.config

logger = None
def make_logger():
	global logger
	logging.config.fileConfig('etc/pyphost_logger.conf')
	logger = logging.getLogger('pypBasic')
