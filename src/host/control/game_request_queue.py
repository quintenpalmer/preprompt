
class Game_Request_Queue:
	def __init__(self):
		self.queue = []

	def add_request(self,req):
		self.queue.append(req):
		if len(self.queue) > 1:
			req1 = self.queue.pop(0)
			req0 = self.queue.pop(0)
			p1_uid = req1[0]
			p1_did = req1[1]
			p2_uid = req2[0]
			p2_did = req2[1]
			game_id = model.start_game(Config_Args(
				Config_Player(p1_uid,p1_did),
				Config_Player(p2_uid,p2_did)))
			ret0 =  respond_action('new',game_id,model.out(game_id,p1_uid))
			ret0 =  respond_action('new',game_id,model.out(game_id,p1_uid))

			#req1.send_response()
			#req2.send_response()
