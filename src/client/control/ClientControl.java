package client.control;

import client.control.network.Packet;
import client.model.Model;
import java.io.IOException;

/** Class used to handle client control,
 *	sends and receives network information and then
 *	unserializes it
 */
public class ClientControl{

	/** Used to send send request to server and receive
	 *	game state back
	 */
	public static void sendRequest(Model model, String request) throws IOException{
		String xml = Packet.sendPacket(request);
		model.xmlInput(xml);
		//System.out.println(model.xmlOutput());
	}
}
