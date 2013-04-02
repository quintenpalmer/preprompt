import pplib.exceptions.PPLoadException;

import ppbackend.control.Listener;
import ppbackend.model.Model;

public class Host{
	public static void main(String[] args){
		try{
			System.out.println("Host: Starting!");
			Model model = new Model(10);
			Listener listener = new Listener(model);
			listener.listenForever();
			System.out.println("Host: Exiting!");
		}
		catch(PPLoadException e){
			System.out.println("Host: Could not load games from database!");
			System.exit(1);
		}
	}
}
