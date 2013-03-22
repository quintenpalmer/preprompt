import pplib.errors.PPLoadException;

import control.ConfigArg;
import model.Model;

public class Host{
	public static void main(String[] args){
		try{
			Model model = new Model(10);
			System.out.println("Hello postprompt player!");
			model.startGame(new ConfigArg(1,0,2,0));
		}
		catch(PPLoadException e){
			System.out.println("error caught");
		}
	}
}
