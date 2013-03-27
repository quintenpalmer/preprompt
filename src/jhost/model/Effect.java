package model;

import org.w3c.dom.Element;

import pplib.XmlParser;
import pplib.exceptions.PPXmlException;
import model.effect.InstantList;
import model.effect.PersistList;
import model.effect.PersistActivateList;

public class Effect{
	InstantList instantList;
	PersistList persistList;
	PersistActivateList pactivateList;

	public Effect(InstantList instantList, PersistList persistList, PersistActivateList pactivateList){
		this.instantList = instantList;
		this.persistList = persistList;
		this.pactivateList = pactivateList;
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
