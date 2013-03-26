package model;

import org.w3c.dom.Element;

import pplib.XmlParser;
import pplib.exceptions.PPXmlException;

public class Effect{

	public Effect(){

	}

	public Effect(XmlParser xmlParser, Element element) throws PPXmlException {
		xmlParser.parseInt(element,"name");
	}

	public String xmlOutput(boolean full){
		return "5";
	}

	public void play(String args){
	}
}
