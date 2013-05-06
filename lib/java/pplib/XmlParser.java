package pplib;

import java.io.IOException;
import java.io.StringReader;

import javax.xml.parsers.*;

import org.w3c.dom.*;
import org.xml.sax.*;

import pplib.exceptions.PPXmlException;

public class XmlParser{

	DocumentBuilder db;

	public XmlParser(){
		try{
			DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
			this.db = dbf.newDocumentBuilder();
		}
		catch(ParserConfigurationException pce){
			pce.printStackTrace();
		}
	}

	public Element createElement(String xml) throws PPXmlException{
		try{
			InputSource inSource = new InputSource();
			inSource.setCharacterStream(new StringReader(xml));
			Document dom = this.db.parse(inSource);
			return dom.getDocumentElement();
		}
		catch(SAXException|IOException e){
			e.printStackTrace();
			throw new PPXmlException("Input XML String is invalid");
		}
	}

	public Element parseElement(Element element, String tag) throws PPXmlException{
		NodeList nl = element.getElementsByTagName(tag);
		if(nl != null && nl.getLength() > 0){
			return (Element)nl.item(0);
		}
		else{
			throw new PPXmlException("That element did not contain the tag "+tag);
		}
	}

	public Element[] parseElements(Element element, String tag) throws PPXmlException{
		NodeList nl = element.getElementsByTagName(tag);
		Element[] elements = new Element[nl.getLength()];
		if(nl != null && nl.getLength() > 0){
			for(int i=0;i<elements.length;i++){
				elements[i] = (Element)nl.item(i);
			}
			return elements;
		}
		else{
			throw new PPXmlException("That element did not contain the tag "+tag);
		}
	}

	public String parseString(Element element, String tag) throws PPXmlException{
		return parseElement(element,tag).getFirstChild().getNodeValue();
	}

	public int parseInt(Element element, String tag) throws PPXmlException{
		try{
			return Integer.parseInt(parseElement(element,tag).getFirstChild().getNodeValue());
		}
		catch(NumberFormatException e){
			throw new PPXmlException("Error parsing integer");
		}
	}

	public boolean parseBool(Element element, String tag) throws PPXmlException{
		String value = parseElement(element,tag).getFirstChild().getNodeValue();
		if(value == "true"){
			return true;
		}
		else if(value == "false"){
			return false;
		}
		else{
			throw new PPXmlException("Error parsing boolean");
		}
	}
}
