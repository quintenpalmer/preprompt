package host.model.player;

import shared.model.player.Player;

/** HostPlayer is a model for the player
* on the host
*/
public class HostPlayer extends Player{

	/** Constructor for the HostPlayer
	* @param uid the user id of the player to create
	* @return the new HostPlayer
	*/
	public HostPlayer(int newUid){
		super("player" + newUid);
		// TODO GET THE DATABASE WORKING SO THIS CAN BE POPULATED
	}
}
