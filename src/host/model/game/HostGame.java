package host.model.game;

import shared.model.game.Game;
import host.model.player.HostPlayer;

/** There is one HostGame on the server 
* per game session between two players
*/
public class HostGame{

	HostPlayer player1;
	HostPlayer player2;

	/** Creates a host version of a game 
	* using the input to load the players from the database
	* @param uid1 the user id of player 1
	* @param did1 the deck id of player 1
	* @param uid2 the user id of player 2
	* @param did2 the deck id of player 2
	*/
	public HostGame(int uid1, int did1, int uid2, int did2) {
		// TODO GET DATABASE OPERATIONAL TO LOAD IN PLAYERS AND DECKS
		// Query the database to get the player info
		// player1 = Database.getPlayer(uid1);
		// player2 = Database.getPlayer(uid2);
		// deck1 = Database.getDeck(uid1,did1);
		// deck2 = Database.getDeck(uid1,did2);
		player1 = new HostPlayer(uid1);
		player2 = new HostPlayer(uid2);
	}

}
