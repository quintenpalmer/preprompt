package ppbackend.control;

import org.w3c.dom.Element;

import pplib.XmlParser;
import pplib.exceptions.*;
import pplib.dataTypes.CommandType;

import ppbackend.model.Model;
import ppbackend.model.mainStruct.Game;
import ppbackend.control.ResponseBuilder;

public class CommandHandler{

	Element element;

	XmlParser xmlParser;
	ResponseBuilder responseBuilder;
	CommandType commandType;
	MetaType metaType;
	Model model;
	Game game;

	int gameId;
	int uid;

	String ret;

	public CommandHandler(Model model){
		this.model = model;
		this.xmlParser = new XmlParser();
		this.responseBuilder = new ResponseBuilder();
	}

	public String handle(String command){
		try{
			element = this.xmlParser.createElement(command);
			commandType = CommandType.getCommandType(
				this.xmlParser.parseString(element,"command") );
			metaType = getMetaType(commandType);
			//System.out.println(metaType);
			ret = responseBuilder.respondNotImplemented();
			if(metaType == MetaType.sys){
				if(commandType == CommandType.Test){
					int version = this.xmlParser.parseInt(element,"version");
					if(version == this.model.getVersion()){
						ret = responseBuilder.respondTest(this.model.getVersion());
					}
					else{
						ret = responseBuilder.respondError("Version numbers do not match");
					}
				}
				else if(commandType == CommandType.Exit){
					ret = responseBuilder.respondExit();
				}
			}
			else if(metaType == MetaType.meta){
				if(commandType == CommandType.New){
					int p1Uid = xmlParser.parseInt(element,"p1_uid");
					int p1Did = xmlParser.parseInt(element,"p1_did");
					int p2Uid = xmlParser.parseInt(element,"p2_uid");
					int p2Did = xmlParser.parseInt(element,"p2_did");

					int gameId = model.startGame(p1Uid,p1Did,p2Uid,p2Did);
					ret = responseBuilder.respondAction(commandType,gameId,model.xmlOutput(gameId,p1Uid));
				}
				else if(commandType == CommandType.List){
					int uid = xmlParser.parseInt(element,"uid");
					ret = responseBuilder.respondList(model.getGameIdsFromUid(uid));
				}
			}
			else if(metaType == MetaType.perform){
				this.gameId = xmlParser.parseInt(element,"game_id");
				this.uid = xmlParser.parseInt(element,"player_id");
				this.game = model.getGameFromGameId(gameId);
				if(commandType == CommandType.Setup){
					this.game.setup();
				}
				else if(commandType == CommandType.Draw){
					this.game.draw(uid);
				}
				else if(commandType == CommandType.Play){
					this.game.play(uid);
				}
				else if(commandType == CommandType.Phase){
					this.game.stepPhase(uid);
				}
				else if(commandType == CommandType.Turn){
					this.game.stepTurn(uid);
				}
				else if(commandType == CommandType.Forfeit){
					this.game.forfeit(uid);
				}
				ret = responseBuilder.respondAction(commandType,gameId,model.xmlOutput(gameId,uid));
			}
			return ret;
		}
		catch(PPXmlException e){
			return responseBuilder.respondError(e.getMessage());
		}
		catch(PPGameActionException e){
			return responseBuilder.respondError(e.getMessage());
		}
	}

	private MetaType getMetaType(CommandType command){
		if(command == CommandType.New || command == CommandType.List){
			return MetaType.meta;
		}
		else if(command == CommandType.Setup ||
			command == CommandType.Draw ||
			command == CommandType.Phase ||
			command == CommandType.Turn ||
			command == CommandType.Play ||
			command == CommandType.Out){
			return MetaType.perform;
		}
		else if (command == CommandType.Exit || command == CommandType.Test){
			return MetaType.sys;
		}
		else{
			return MetaType.unknown;
		}
	}

	private enum MetaType{
		meta,perform,sys,unknown;
	}
}
