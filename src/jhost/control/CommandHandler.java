package control;

import model.Model;
import pplib.XmlParser;
import control.ResponseBuilder;
import pplib.exceptions.PPXmlException;
import pplib.dataTypes.CommandType;
import org.w3c.dom.Element;

public class CommandHandler{

	Model model;
	XmlParser parser;
	ResponseBuilder responseBuilder;
	Element element;
	CommandType commandType;
	String ret;

	public CommandHandler(Model model){
		this.model = model;
		this.parser = new XmlParser();
		this.responseBuilder = new ResponseBuilder();
	}

	public String handle(String command){
		try{
			element = this.parser.createElement(command);
			commandType = CommandType.getCommandType(
				this.parser.parseString(element,"command") );
			MetaType metaType = getMetaType(commandType);
			System.out.println(metaType);
			ret = responseBuilder.respondNotImplemented();
			if(metaType == MetaType.sys){
				if(commandType == CommandType.Test){
					int version = this.parser.parseInt(element,"version");
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
			return ret;
		}
		catch(PPXmlException e){
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
