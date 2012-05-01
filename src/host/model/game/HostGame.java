package host.model.game;

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

	/** serializes the game into an xml string that represents the game state
	 * @param uid the user id of the player requesting the game state
	 * @return the xml string
	 */
	public String xmlOutput(int uid){
		String xml = "";
		xml += "<mePlayer>";
		xml += getSelfFromUid(uid).xmlOutput();
		xml += "</mePlayer>";
		xml += "<themPlayer>";
		xml += getEnemyFromUid(uid).xmlOutput();
		xml += "</themPlayer>";
		return xml;
	}

	/** Returns the "me" player given this uid
	 * @param uid the user/player id of the "me" player
	 * @return The "me" player
	 */
	public HostPlayer getSelfFromUid(int uid){
		if(player1.getUid()==uid){
			return player1;
		}
		else if(player2.getUid()==uid){
			return player2;
		}
		else{
			return null;
		}
	}

	/** Returns the "them" player given this uid
	 * @param uid the user/player id of the "me" player
	 * @return The "them" player
	 */
	public HostPlayer getEnemyFromUid(int uid){
		if(player1.getUid()==uid){
			return player2;
		}
		else if(player2.getUid()==uid){
			return player1;
		}
		else{
			return null;
		}
	}
}
