package client.control.network;

import java.io.*;
import java.net.*;

/** The packet serves as the class that 
* sends the request to the server and 
* receives the game state back
*/
public class Packet{

	/** sends the packet to the server and receives the server's response
	* @param command the command to send to the server
	* @return the xml game state received from the server
	*/
	public static String sendPacket(String command) throws IOException{
		Socket socket=null;
		PrintWriter out=null;
		BufferedReader in=null;
		String host="localhost";

		try{
			socket=new Socket(host,52690);
			out=new PrintWriter(socket.getOutputStream(),true);
			in=new BufferedReader(new InputStreamReader(socket.getInputStream()));
		}
		catch(UnknownHostException e){
			return "Unable to connect to Host" + host;
		}
		catch(IOException e){
			return "Coudn't get I/O for the connection to : " + host;
		}

		// Use stdIn to run requests from the terminal
		//BufferedReader stdIn = new BufferedReader(new InputStreamReader(System.in));
		String fromServer;

		out.println(command);
		fromServer=in.readLine();

		out.close();
		in.close();
		socket.close();
		socket.close();
		return fromServer;
	}
}
