package shared.control;

import java.io.IOException;
import java.io.StringReader;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;

import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.NodeList;
import org.xml.sax.SAXException;
import org.xml.sax.InputSource;

/** The Parser class is used to parse xml strings/elements into
* strings, ints, booleans, and sub-elements
* TODO POSSIBLY SANITIZE THESE IF POSSIBLE?
*/
public class Parser {

	/** Parses an element out of the input xml string based on the tag
	* @param xml The xml string to search
	* @param tag The tag used to search the xml
	* @return The element in the match of the given tag in the xml string
	*/
	public Element parseElement(String xml, String tag){
		Element ele = parseXml(xml);
		return eleParseElement(ele,tag);
	}

	/** Parses a string out of the input xml string based on the tag
	* @param xml The xml string to search
	* @param tag The tag used to search the xml
	* @return The string in the match of the given tag in the xml string
	*/
	public String parseString(String xml, String tag){
		Element ele= parseXml(xml);
		return eleParseString(ele,tag);
	}

	/** Parses an int out of the input xml string based on the tag
	* @param xml The xml string to search
	* @param tag The tag used to search the xml
	* @return The int in the match of the given tag in the xml string
	*/
	public int parseInt(String xml, String tag){
		Element ele = parseXml(xml);
		return eleParseInt(ele,tag);
	}

	/** Parses a boolean out of the input xml string based on the tag
	* @param xml The xml string to search
	* @param tag The tag used to search the xml
	* @return The boolean in the match of the given tag in the xml string
	*/
	public boolean parseBoolean(String xml, String tag){
		Element ele = parseXml(xml);
		return eleParseBoolean(ele,tag);
	}

	/** Parses a string out of the input element based on the tag
	* @param ele The element to search
	* @param tag The tag used to search the element
	* @return The string in the match of the given tag in the element
	*/
	public String eleParseString(Element ele, String tag){
		String textVal = "";
		NodeList nl = ele.getElementsByTagName(tag);
		if(nl != null && nl.getLength()>0){
			try{
			Element newEle = (Element)nl.item(0);
			textVal = newEle.getFirstChild().getNodeValue();
			}
			catch(NullPointerException npe){
				textVal = "";
			}
		}
		return textVal;
	}

	/** Parses a boolean out of the input element based on the tag
	* @param ele The element to search
	* @param tag The tag used to search the element
	* @return The boolean in the match of the given tag in the element
	*/
	public boolean eleParseBoolean(Element ele, String tag){
		return eleParseString(ele,tag).equals("true");
	}

	/** Parses an element out of the input element based on the tag
	* @param ele The element to search
	* @param tag The tag used to search the element
	* @return The element in the match of the given tag in the element
	*/
	public Element eleParseElement(Element ele, String tag){
		NodeList nl = ele.getElementsByTagName(tag);
		if(nl != null && nl.getLength()>0){
			return (Element)nl.item(0);
		}
		else{
			return null;
		}
	}

	/** Parses an int out of the input element based on the tag
	* @param ele The element to search
	* @param tag The tag used to search the element
	* @return The int in the match of the given tag in the element
	*/
	public int eleParseInt(Element ele, String tag){
		try{
			return Integer.parseInt(eleParseString(ele, tag));
		}catch(NumberFormatException nfe){
			return -1;
		}
	}

	/** Constructs the entire tree of the input xml string in an element
	* @param xml The xml to search
	* @return The element form of the xml
	*/
	private Element parseXml(String xml){
		Document dom;
		DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();

		try{
			DocumentBuilder db = dbf.newDocumentBuilder();
			InputSource inSource = new InputSource();
			inSource.setCharacterStream(new StringReader(xml));
			dom = db.parse(inSource);
			return dom.getDocumentElement();
		}catch(ParserConfigurationException pce) {
			pce.printStackTrace();
		}catch(SAXException se) {
			se.printStackTrace();
		}catch(IOException ioe) {
			ioe.printStackTrace();
		}
		return null;
	}
}

