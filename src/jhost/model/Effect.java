package model;

import org.w3c.dom.Element;

import pplib.XmlParser;
import pplib.exceptions.PPXmlException;

public class Effect{

	public Effect(){

	}

	public Effect(XmlParser xmlParser, Element element){
		try{
			xmlParser.parseInt(element,"name");
		}
		catch(PPXmlException e){
			System.out.println(e.getMessage());
		}
	}

	public void play(String args){
	}
}
