package client.model.card;

import org.w3c.dom.Element;
import shared.control.Parser;

/** The ClientCard is used as a base for the types of
* cards a client uses
*/
public interface ClientCard{
	public void xmlInput(Parser parser, Element ele);
	public String xmlOutput();
}
