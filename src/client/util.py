import logging
import logging.config

from os import environ

logger = None
def make_logger():
	global logger
	logging.config.fileConfig(environ['pyp']+'/etc/pypclient_logger.conf')
	logger = logging.getLogger('pypBasic')
