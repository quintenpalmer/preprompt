package ppbackend.control;

import java.net.*;
import java.io.*;

import ppbackend.model.Model;
import ppbackend.control.CommandHandler;

public class Listener{
	ServerSocket serverSocket;
	boolean listening;
	CommandHandler commandHandler;

	public Listener(Model model){
		this.listening = true;
		this.commandHandler = new CommandHandler(model);
		try {
			this.serverSocket = new ServerSocket(52690);
		}
		catch (IOException e) {
			System.err.println("Failed to listen on 52690.");
			System.exit(1);
		}
	}

	public void listenForever(){
		try{
			while (listening){
				Socket socket = this.serverSocket.accept();
					PrintWriter out = new PrintWriter(socket.getOutputStream(),true);
					BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
					char[] inputLine = new char[32768];
					String command;
					String outputLine;

					while(in.read(inputLine,0,32768) != -1){
						outputLine=processRequest(String.valueOf(inputLine).trim());
						System.out.println(inputLine);
						out.println(outputLine);
					}
					out.close();
					in.close();
					socket.close();
			}
			serverSocket.close();
		}
		catch(IOException e){
			e.printStackTrace();
		}
	}

	private String processRequest(String command){
		return this.commandHandler.handle(command);
	}
}
