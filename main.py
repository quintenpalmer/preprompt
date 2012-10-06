#!/usr/bin/env python
from src.model.Model import Model
from src.model.clist import cltypes
from src.control.gameHandle.play.Play import PlayReq, PlayArgs
#from control import Controller
#from src.view import Display

if __name__ == '__main__':
	data = 1
	model = Model(data)
	gameId1 = model.startGame(((26,13),(1,2)))
	#model.out(26)
	model.games[gameId1].draw(26)
	#model.out(26)
	playReq = PlayReq(uid=26,cardList=cltypes.hand,cardNum=0,playArgs=PlayArgs(model.games[gameId1].game,uid=13,targetCard=0))
	model.games[gameId1].play(playReq)
	model.out(26)
	model.stopGame(gameId1)
	#model.out(26)
	#control = Controller(model)
	#disp = Display(model)
