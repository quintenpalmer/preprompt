package model;

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

	public Card(XmlParser xmlParser, Element element){
		try{
			String cardType = xmlParser.parseString(element,"type");
			this.name = xmlParser.parseString(element,"name");
			this.effect = new Effect(xmlParser,xmlParser.parseElement(element,"effect"));
		}
		catch(PPXmlException e){
			System.out.println(e.getMessage());
		}
	}

	public void play(String args){
		this.effect.play(args);
	}
}
