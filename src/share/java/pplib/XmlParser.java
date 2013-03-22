package pplib;

import java.io.IOException;
import java.io.StringReader;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;

import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.NodeList;
import org.xml.sax.InputSource;
import org.xml.sax.SAXException;

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
}
