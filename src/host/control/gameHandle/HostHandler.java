package host.control.gameHandle;

import host.model.Model;
import host.control.gameHandle.Request;

public class HostHandler{

	/** Static method to process a request on a given model
	* @param model the Model to perform the request on
	* @param request the Request to perform
	* @return the string representing the game state after the request is processed
	*/
	public static String process(Model model, Request request){
		//TODO SANITIZE EVERYTHING HERE
		String command = request.getCommand();
		String startInfo = "1 1 2 2";
		if(command.equals("new")){
			model.addGame(1,1,2,2);
			return model.xmlOutput(1);
		}
		else if(command.equals("perform")){
			performAction(model, request.getAction());
			return model.xmlOutput(1);
		}
		else if(command.equals("view")){
			return model.xmlOutput(1);
		}
		else{
			return "Nice Try!";
		}
	}

	private static void performAction(Model model, String action){
		//TODO use old code to perform actions WITHIN THE CONTROLLER, NOT IN THE MODEL
		if(action.equals("draw")){
			model.draw(1);
		}
	}

}
