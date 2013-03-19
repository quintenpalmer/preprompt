import os
import logging
import logging.config

logger = None
def make_logger(host_or_client):
	global logger
	path = os.path.join(os.environ['pyproot'],'etc','pyp'+host_or_client+'_logger.conf')
	logging.config.fileConfig(path)
	logger = logging.getLogger('pypBasic')
