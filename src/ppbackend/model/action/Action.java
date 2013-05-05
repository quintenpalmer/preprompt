package ppbackend.model.action;

import java.util.*;

import pplib.exceptions.*;

import ppbackend.model.mainStruct.*;
import ppbackend.model.shared.*;
import ppbackend.model.effect.*;
import ppbackend.model.action.*;
import ppbackend.control.CardLoader;

public class Action{
	LinkedList<SubAction> actions;

	public Action(Game game, int uid, InstantList ilist) throws PPGameActionException{
		this.actions = new LinkedList<SubAction>();
		for(Instant instant : ilist.getInstants()){
			this.actions.add(new SubAction(game,uid,instant));
		}
		while(!actions.isEmpty()){
			actions.poll().act();

			int index = 0;
			for(Card card : game.getMeFromUid(uid).getDeck().getCardList(CLTypes.active).getCards()){
				if(! card.getEffect().getPersistList().doesPersist()){
					actions.add(0,new SubAction(game,uid,CardLoader.getDestroyEffect(index,0)));
					break;
				}
				index++;
			}
			index = 0;
			for(Card card : game.getThemFromUid(uid).getDeck().getCardList(CLTypes.active).getCards()){
				if(! card.getEffect().getPersistList().doesPersist()){
					actions.add(0,new SubAction(game,uid,CardLoader.getDestroyEffect(index,1)));
					break;
				}
				index++;
			}
		}
	}
}
