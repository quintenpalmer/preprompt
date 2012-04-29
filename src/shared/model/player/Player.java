package shared.model.player;

/** Represents the player of the game
*/
public class Player{
	String name;
	int uid;

	/** Constructs the Player
	* @param newUid the id of player to construct
	* @return the new Player
	*/
	public Player(int newUid){
		name = "Player" + uid;
		uid = newUid;
	}
}
