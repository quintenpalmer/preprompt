package host.control.network;

import java.net.*;
import java.io.*;
import host.model.Model;

/** The Listener listens for requests and passes them to the handler
*/
public class Listener{

	/** static method to call to start listening
	* @param model the model to be affecting
	*/
	public static void start(Model model) throws IOException{
		ServerSocket serverSocket = null;
		boolean listening = true;

		try {
			serverSocket = new ServerSocket(52690);
		} catch (IOException e) {
			System.err.println("Failed to listen on 52690.");
			System.exit(-1);
		}

		while (listening){
			new Handler(serverSocket.accept()).connect(model);
		}

		serverSocket.close();
	}
}
