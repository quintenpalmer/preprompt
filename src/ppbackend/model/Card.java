package ppbackend.model;

import org.w3c.dom.Element;

import pplib.XmlParser;
import pplib.exceptions.PPXmlException;

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

	public String xmlOutput(boolean full){
		String xml = "<type>full</type>";
		xml += "<name>"+this.name+"</name>";
		xml += "<effect>"+this.effect.xmlOutput(full)+"</effect>";
		return xml;
	}

	public Effect getEffect(){
		return this.effect;
	}

	public void play(String args){
		this.effect.play(args);
	}
}
