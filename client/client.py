from src.view.view import View
from src.control.network.network_client import Requester
import time

if __name__ == '__main__':
	view = View()
	requester = Requester()
	def do(param):
		ret = requester.send_request(param)
		time.sleep(.01)
		return ret
	print do('test')
	gid,status = do('new 26 0 13 1').split(' ')
	print status
	print do('setup '+gid+' 26')
	print do('draw '+gid+' 26')
	print do('phase '+gid+' 26')
	print do('phase '+gid+' 26')
	print do('play '+gid+' 26 1 0 13 2 0')
	print do('play '+gid+' 26 1 0 13 2 0')
	print do('phase '+gid+' 26')
	print do('turn '+gid+' 26')
	print do('draw '+gid+' 13')
	print do('phase '+gid+' 13')
	print do('phase '+gid+' 13')
	print do('play '+gid+' 13 1 0 13 2 0')
	print do('play '+gid+' 13 1 0 13 2 0')
	print do('phase '+gid+' 13')
	print do('turn '+gid+' 13')
	print do('out '+gid+' 26')
	print requester.send_request('exit')
