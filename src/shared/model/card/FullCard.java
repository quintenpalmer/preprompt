package shared.model.card;

import shared.control.Parser;
import org.w3c.dom.Element;

/** FullCard class used to represent one card will all information
*/
public class FullCard extends Card{
	String name;
	int id;

	/** Constructor for the FullCard class
	* currently only takes the location, but will 
	* take id and then query database to populate fields
	* @param newLocation the location of the new FullCard in the containing list
	* @return the new FullCard.
	*/
	public FullCard(int newLocation){
		super(newLocation);
		name = "card";
		id = 1;
	}

	/** used to serialize the card into the xml format
	* @return String that uniquely represents the FullCard
	*/
	public String xmlOutput(){
		String xml = "";
		xml += "<card>";
		xml += "<name>" + name + "</name>";
		xml += "<location>" + location + "</location>";
		xml += "</card>";
		return xml;
	}

	/** used to unserialze the xml element into a FullCard
	* @param ele the element of the sax xml parser
	*/
	public void xmlInput(Element ele){
		Parser parser = new Parser();
		name = parser.eleParseString(ele,"name");
		location = parser.eleParseInt(ele,"location");
	}
}
