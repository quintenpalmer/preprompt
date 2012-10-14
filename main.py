#!/usr/bin/env python
from src.model.Model import Model
from src.model.clist import cltypes
from src.control.gameHandle.play.Play import PlayArgs
#from control import Controller
#from src.view import Display

if __name__ == '__main__':
	data = 1
	model = Model(data)
	gameId1 = model.startGame(((26,13),(1,2)))
	#model.out(26)
	model.games[gameId1].draw(26)
	#model.out(26)
	playArgs = PlayArgs(game=model.games[gameId1].game,srcUid=26,srcCard=0,srcList=cltypes.hand,tgtUid=13,tgtCard=0,tgtList=cltypes.active)
	model.games[gameId1].play(playArgs)
	model.out(26)
	model.stopGame(gameId1)
	#model.out(26)
	#control = Controller(model)
	#disp = Display(model)
