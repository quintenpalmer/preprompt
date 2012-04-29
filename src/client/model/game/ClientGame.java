package client.model.game;

import client.model.player.ClientPlayer;

/** The ClientGame is the client's representation of the game
* One player represents the person playing the game
* and the other represents his/her opponent
*/
public class ClientGame{

	ClientPlayer playerme;
	ClientPlayer playerthem;

	/** Constructor for the ClientGame
	* @param player1name the name of the self player
	* @param player2name the name of the enemy player
	*/
	public ClientGame(String player1name, String player2name) {
		playerme = new ClientPlayer(player1name);
		playerthem = new ClientPlayer(player2name);
	}

}
