package shared.model.card;

import org.w3c.dom.Element;
import shared.control.Parser;

/** Class for cards
* Only has the base information which is needed
* for both viewable and non-viewable cards
*/
public abstract class Card{
	// index of the card in the containing list
	int location;

	/** Constructor for the Card 
	* @param newLocation the location of the card in the conataining list
	* @return the new Card
	*/
	public Card(int newLocation){
		location = newLocation;
	}

	/** used to serialize the card into the xml format
	* @return String that uniquely represents the Card
	*/
	public String xmlOutput(){
		String xml = "";
		xml += "<location>" + location + "</location>";
		return xml;
	}

	/** used to unserialze the xml element into a Card
	* @param ele the element of the sax xml parser
	*/
	public void xmlInput(Element ele){
		Parser parser = new Parser();
		location = parser.eleParseInt(ele,"location");
	}

}
