package ppbackend.model;

import java.util.*;
import org.w3c.dom.Element;

import pplib.XmlParser;
import pplib.exceptions.PPXmlException;
import ppbackend.model.*;

public class Effect{
	InstantList instantList;
	PersistList persistList;
	PersistActivateList pactivateList;
	ElementType elementType;

	public Effect(InstantList instantList, PersistList persistList, PersistActivateList pactivateList, ElementType elementType){
		this.instantList = instantList;
		this.persistList = persistList;
		this.pactivateList = pactivateList;
		this.elementType = elementType;
	}

	public Effect(XmlParser xmlParser, Element element) throws PPXmlException {
		xmlParser.parseInt(element,"name");
	}

	public String xmlOutput(boolean full){
		String xml = "<instants>"+this.instantList.xmlOutput(full)+"</instants>";
		xml += "<persists>"+this.persistList.xmlOutput(full)+"</persists>";
		xml += "<pactivates>"+this.pactivateList.xmlOutput(full)+"</pactivates>";
		xml += "<elements>";
		xml += "<element>"+elementType.toString()+"</element>";
		xml += "</elements>";
		return xml;
	}

	public void play(String args){
	}

	public boolean doesPersist(){
		return this.persistList.doesPersist();
	}

	public int[] getInstantPhases(){
		return this.instantList.getPhases();
	}

	public Instant[] getInstants(){
		return this.instantList.getInstants();
	}
}
