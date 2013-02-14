package host;

import java.io.IOException;
import host.model.Model;
import host.control.network.Listener;

/** Main class for host
*/
public class Main{

	/** main method for host
	*/
	public static void main(String[] args) throws IOException{
		Model model = new Model(1);
		Listener.start(model);
		System.out.println("Hope all went well!");
	}
}
