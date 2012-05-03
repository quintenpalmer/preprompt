package client.model.card;

import shared.model.card.Card;

/** NonVisibleCard is used to represent a card
* that the client cannot see
*/
public class ClientNonVisibleCard extends Card implements ClientCard{
	/** Constructor for the NonVisibleCard 
	* @param newLocation the location of the card in the conataining list
	* @return the new card
	*/
	public ClientNonVisibleCard(int newLocation){
		super(newLocation);
	}
}
