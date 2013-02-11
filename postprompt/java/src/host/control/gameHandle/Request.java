package host.control.gameHandle;

import java.util.StringTokenizer;

/** One Request is create each time a client makes a request
* TODO SANITIZE ALL OF THIS
*/
public class Request{
	StringTokenizer st;

	int location;
	String destination;

	String command;
	int gameId, uid;
	int uid1, did1, uid2, did2;
	String action;
	
	/** Creates a new Request
	* @param toParse the action request to parse
	* @return the new Request
	*/
	public Request(String toParse){
		//System.out.println(toParse);
		st = new StringTokenizer(toParse);
		command = st.nextToken();
		if(command.equals("new")){
			uid1 = Integer.parseInt(st.nextToken());
			did1 = Integer.parseInt(st.nextToken());
			uid2 = Integer.parseInt(st.nextToken());
			did2 = Integer.parseInt(st.nextToken());
		}
		else if(command.equals("perform")){
			gameId = Integer.parseInt(st.nextToken());
			uid = Integer.parseInt(st.nextToken());

			action = st.nextToken();
	

			if(action.equals("play")){
				location = Integer.parseInt(st.nextToken());
			}

		}
		else if(command.equals("view")){
			gameId = Integer.parseInt(st.nextToken());
			uid = Integer.parseInt(st.nextToken());
		}
	}

	/** getter for the command (new/perform/view)
	* @return the command	
	*/
	public String getCommand(){
		return command;
	}

	/** getter for the action (play/draw/phase/turn)
	* @return the action
	*/
	public String getAction(){
		return action;
	}
}
