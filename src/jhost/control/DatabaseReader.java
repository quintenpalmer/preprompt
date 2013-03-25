package control;

import model.Game;
import model.PlayerContainer;
import model.Player;
import model.Deck;
import model.Card;

public class DatabaseReader{
	public static Game getGame(int p1Uid, int p1Did, int p2Uid, int p2Did){
		PlayerContainer[] pcs = new PlayerContainer[2];
		for(int i=0;i<2;i++){
			Player player = new Player(1,"Quin");
			Deck deck = new Deck(new Card[5]);
			pcs[i] = new PlayerContainer(player,deck);
		}
		return new Game(pcs[0],pcs[1]);
	}
}
