package client;

import client.model.Model;
import client.view.View;
import java.io.IOException;

/** Main class for client
 *	Main!
 */
public class Main{

	/** main method for client
	 *	does not take command line arguments
	 */
	public static void main(String[] args) throws IOException{
		Model model = new Model(1);
		View view = new View();
		view.init();
		view.run(model);
		view.finish();
		System.out.println("It was fun!");
	}
}