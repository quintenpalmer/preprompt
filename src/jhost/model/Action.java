package model;

import model.Game;
import model.Effect;

public class Action{
	ArrayList<SubAction> actions;
	Game game;
	int uid;

	public Action(Game game, int uid){
		this.actions = new ArrayList<SubAction>();
		this.game = game;
		this.uid = uid;
	}

	public void addAction(Effect effect){
		this.actions.add(new SubAction(game,uid,effect));
	}

	public void act(){
	}

	private class SubAction{
		Game game;
		PlayerContainer me;
		PlayerContainer them;
		Element element = null;

		public SubAction(Game game, int uid, Effect effect){
			this.game = game;
			this.me = game.getMeFromUid(uid);
			this.them = game.getThemFromUid(uid);
		}
	}
}
