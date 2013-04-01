package model;

import java.util.*;
import org.w3c.dom.Element;

import pplib.XmlParser;
import pplib.exceptions.PPXmlException;
import model.effect.*;
import model.ElementType;

public class Effect{
	InstantList instantList;
	PersistList persistList;
	PersistActivateList pactivateList;
	ElementType[] elements;

	public Effect(InstantList instantList, PersistList persistList, PersistActivateList pactivateList, ElementType[] elements){
		this.instantList = instantList;
		this.persistList = persistList;
		this.pactivateList = pactivateList;
		this.elements = elements;
	}

	public Effect(XmlParser xmlParser, Element element) throws PPXmlException {
		xmlParser.parseInt(element,"name");
	}

	public String xmlOutput(boolean full){
		String xml = "<instants>"+this.instantList.xmlOutput(full)+"</instants>";
		xml += "<persists>"+this.persistList.xmlOutput(full)+"</persists>";
		xml += "<pactivates>"+this.pactivateList.xmlOutput(full)+"</pactivates>";
		xml += "<elements>";
		for(ElementType element : this.elements){
			xml += "<element>"+element.toString()+"</element>";
		}
		xml += "</elements>";
		return xml;
	}

	public void play(String args){
	}

	public int[] getInstantPhases(){
		return this.instantList.getPhases();
	}

	public ArrayList<Instant> getInstants(){
		return this.instantList.getInstants();
	}
}
