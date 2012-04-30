package client.model.card;

import org.w3c.dom.Element;

/** The ClientCard is used as a base for the types of
* cards a client uses
*/
public interface ClientCard{
	public void xmlInput(Element ele);
	public String xmlOutput();
}
