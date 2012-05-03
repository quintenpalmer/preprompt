package host.model.player;

import host.model.deck.HostDeck;

/** The HostPlayerContainer contains the player information and the deck of each player
 */
public class HostPlayerContainer{
	HostPlayer player;
	HostDeck deck;
	int uid;

	/** Constructor for HostPlayerContainer
	 * @param newUid the user id of the new player
	 * @param newDid the deck id for the new deck for this player
	 * @return the new HostPlayerContainer
	 */
	public HostPlayerContainer(int newUid, int newDid){
		uid = newUid;
		player = new HostPlayer(newUid);
		deck = new HostDeck(20);
		//TODO GET THE DATABASE WORKING FOR THIS TOO
	}

	/** Getter for the user/player id
	 * @return the player's id
	 */
	public int getUid(){
		return uid;
	}

	/** Serializes the player container into an xml string
	 * @return the xml string
	 */
	public String xmlOutput(boolean full){
		String xml = "";
		xml += "<player>";
		xml += player.xmlOutput();
		xml += "</player>";
		xml += "<deck>";
		xml += deck.xmlOutput(full);
		xml += "</deck>";
		return xml;
	}
}
