package model;

import org.w3c.dom.Element;

import pplib.XmlParser;
import pplib.exceptions.PPXmlException;

public class Player{
	int uid;
	String name;
	int health;

	public Player(int uid, String name){
		this.uid = uid;
		this.name = name;
		this.health = 50;
	}

	public Player(XmlParser xmlParser, Element element){
		try{
			this.uid = xmlParser.parseInt(element,"uid");
			this.name = xmlParser.parseString(element,"name");
			this.health = xmlParser.parseInt(element,"health");
		}
		catch(PPXmlException e){
			System.out.println(e.getMessage());
		}
	}

	public int getUid(){
		return this.uid;
	}
	public String getName(){
		return this.name;
	}
	public int getHealth(){
		return this.health;
	}
}
