package ppbackend.control;

import java.util.ArrayList;

import pplib.DatabaseConnection;
import pplib.exceptions.PPDatabaseException;

import ppbackend.control.CardLoader;
import ppbackend.model.shared.ElementType;
import ppbackend.model.mainStruct.*;

public class DatabaseReader{
	DatabaseConnection database;

	public DatabaseReader() throws PPDatabaseException{
		database = new DatabaseConnection("pp_shared");
	}
	public Game getGame(int p1Uid, int p1Did, int p2Uid, int p2Did) throws PPDatabaseException{
		PlayerContainer[] pcs = new PlayerContainer[2];
		int[] uids = new int[]{p1Uid,p2Uid};
		int[] dids = new int[]{p1Did,p2Did};
		for(int i=0;i<2;i++){
			String name = database.select("select username from auth_user where id="+Integer.toString(uids[i])).get(0);
			Player player = new Player(uids[i],name);
			ArrayList<Card> cards = new ArrayList<Card>();
			ArrayList<String> cardIds = database.select("select card_id from play_decks where uid="+Integer.toString(uids[i])+" and deck_id="+Integer.toString(dids[i]));
			for(String cardId : cardIds){
				cards.add(CardLoader.getDirectDamage("Fire Blast",ElementType.fire,5));
			}
			Deck deck = new Deck(cards);
			pcs[i] = new PlayerContainer(player,deck);
		}
		return new Game(pcs[0],pcs[1]);
	}
}
