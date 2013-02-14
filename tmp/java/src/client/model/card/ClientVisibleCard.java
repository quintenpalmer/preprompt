package client.model.card;

import shared.model.card.FullCard;

/** VisibleCard is a card that the client can see all of the information about
*/
public class ClientVisibleCard extends FullCard implements ClientCard{

	/** Constructor for the VisibleCard
	* @param newLocation the location of the card in the conataining list
	* @return the new card
	*/
	public ClientVisibleCard(int newLocation){
		super(newLocation);
	}

}
