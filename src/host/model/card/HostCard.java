package host.model.card;

import shared.model.card.FullCard;

/** The HostCard is the card used on the host end
* it contains all of the information about the card
*/
public class HostCard extends FullCard{

	/** Constructor for the FullCard 
	* @param newLocation the location of the card in the conataining list
	* @return the new card
	*/
	public HostCard(int newLocation){
		super(newLocation);
	}

}
