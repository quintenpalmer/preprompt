package control;

import model.Model;
import pplib.XmlParser;
import control.ResponseBuilder;
import pplib.exceptions.*;
import pplib.dataTypes.CommandType;
import org.w3c.dom.Element;

public class CommandHandler{

	Model model;
	XmlParser xmlParser;
	ResponseBuilder responseBuilder;
	Element element;
	CommandType commandType;
	String ret;
	MetaType metaType;

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
			System.out.println(metaType);
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
					ret = responseBuilder.respondAction(commandType,gameId,model.out(gameId,p1Uid));
				}
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
}

enum MetaType{
	meta,perform,sys,unknown;
}
