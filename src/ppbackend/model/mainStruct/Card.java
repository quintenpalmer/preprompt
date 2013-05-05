package ppbackend.model.mainStruct;

import org.w3c.dom.Element;

import pplib.XmlParser;
import pplib.exceptions.PPXmlException;

import ppbackend.model.effect.Effect;

public class Card{
	String name;
	Effect effect;

	public Card(String name, Effect effect){
		this.name = name;
		this.effect = effect;
	}

	public Card(XmlParser xmlParser, Element element) throws PPXmlException{
		String cardType = xmlParser.parseString(element,"type");
		this.name = xmlParser.parseString(element,"name");
		this.effect = new Effect(xmlParser,xmlParser.parseElement(element,"effect"));
	}

	public String ppserialize(boolean full){
		String xml = "<type>full</type>";
		xml += "<name>"+this.name+"</name>";
		xml += "<effect>"+this.effect.ppserialize(full)+"</effect>";
		return xml;
	}

	public Effect getEffect(){
		return this.effect;
	}
}
