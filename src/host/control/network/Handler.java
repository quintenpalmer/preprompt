package host.control.network;

import java.io.*;
import java.net.*;
import java.util.*;
import java.sql.*;
import host.model.Model;
import host.control.gameHandle.Request;
import host.control.gameHandle.HostHandler;

/** The handler is used to handle a specific requests
*/
public class Handler extends Thread{
	private Socket socket = null;

	/** constructs the Handler
	* also makes its thread have a unique name
	* @param newSocket the socket to connect on
	* @return the new Handler
	*/
	public Handler(Socket newSocket){
		super("Handler" + newSocket.getPort());
		socket=newSocket;
	}

	/** connects to the client performing a move
	* @param model the model this handler is affecting
	*/
	public void connect(Model model) throws IOException{
		try{
			PrintWriter out = new PrintWriter(socket.getOutputStream(),true);
			BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
			String inputLine, outputLine;

			while((inputLine=in.readLine()) !=null){
				outputLine=processClient(inputLine,model);
				System.out.println(inputLine);
				out.println(outputLine);
				/*if(outputLine.equals("terminate")){
					break;
				}*/
			}
			out.close();
			in.close();
			socket.close();
		} catch(IOException e){
			e.printStackTrace();
		}
	}

	/** processing request of the client on the given model
	* @param input the string representation of what to perform
	* @param model the model to perform the action on
	* @return the xml string represtation of the game state after the action is performed
	*/
	private static String processClient(String input, Model model){
		Request request = new Request(input);
		return HostHandler.process(model,request);
	}
}
