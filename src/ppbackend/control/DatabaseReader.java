package ppbackend.control;

import java.util.ArrayList;

import ppbackend.control.CardLoader;
import ppbackend.model.shared.ElementType;
import ppbackend.model.mainStruct.*;

public class DatabaseReader{
	public Game getGame(int p1Uid, int p1Did, int p2Uid, int p2Did){
		PlayerContainer[] pcs = new PlayerContainer[2];
		for(int i=0;i<2;i++){
			Player player = new Player(i+1,"Quin");
			ArrayList<Card> cards = new ArrayList<Card>(10);
			int[] loadedDeck = {1,1,1,1,1,1,1,1,1,1};
			for(int cardId : loadedDeck){
				cards.add(CardLoader.getDirectDamage("Fire Blast",ElementType.fire,5));
			}
			Deck deck = new Deck(cards);
			pcs[i] = new PlayerContainer(player,deck);
		}
		return new Game(pcs[0],pcs[1]);
	}
}
