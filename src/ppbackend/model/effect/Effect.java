package ppbackend.model.effect;

import java.util.*;
import org.w3c.dom.Element;

import pplib.XmlParser;
import pplib.exceptions.PPXmlException;

import ppbackend.model.shared.ElementType;

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

	public String ppserialize(boolean full){
		String xml = "<instants>"+this.instantList.ppserialize(full)+"</instants>";
		xml += "<persists>"+this.persistList.ppserialize(full)+"</persists>";
		xml += "<pactivates>"+this.pactivateList.ppserialize(full)+"</pactivates>";
		xml += "<elements>";
		xml += "<element>"+elementType.toString()+"</element>";
		xml += "</elements>";
		return xml;
	}

	public InstantList getInstantList(){
		return this.instantList;
	}

	public PersistList getPersistList(){
		return this.persistList;
	}

	public PersistActivateList getPersistActivateList(){
		return this.pactivateList;
	}
}
