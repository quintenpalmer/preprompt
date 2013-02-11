package host.model.card;

import host.control.gameHandle.cardEffect.CardEffect;
import shared.model.card.FullCard;

/** The HostCard is the card used on the host end
* it contains all of the information about the card
*/
public class HostCard extends FullCard{
	CardEffect ce;
	
	/** Constructor for the FullCard 
	* @param newLocation the location of the card in the conataining list
	* @return the new card
	*/
	public HostCard(int newLocation){
		super(newLocation);
		ce = new CardEffect("a,d,f,2");
	}
}
