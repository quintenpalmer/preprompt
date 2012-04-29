package host.model.player;

/** HostPlayer is a model for the player
* on the host
*/
public class HostPlayer{
	String name;

	/** Constructor for the HostPlayer
	* @param uid the user id of the player to create
	* @return the new HostPlayer
	*/
	public HostPlayer(int uid){
		// TODO GET THE DATABASE WORKING SO THIS CAN BE POPULATED
		name = "player" + uid;
	}
}
