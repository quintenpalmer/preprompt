package ppbackend.model.mainStruct;

import org.w3c.dom.Element;

import pplib.XmlParser;
import pplib.exceptions.*;

public class Player{
	int uid;
	String name;
	int health;

	public Player(int uid, String name){
		this.uid = uid;
		this.name = name;
		this.health = 50;
	}

	public Player(XmlParser xmlParser, Element element) throws PPXmlException {
		this.uid = xmlParser.parseInt(element,"uid");
		this.name = xmlParser.parseString(element,"name");
		this.health = xmlParser.parseInt(element,"health");
	}

	public String ppserialize(int playerType){
		String xml = "<uid>"+Integer.toString(this.uid)+"</uid>";
		xml += "<name>"+this.name+"</name>";
		xml += "<health>"+Integer.toString(this.health)+"</health>";
		return xml;
	}

	public void receiveDamage(int amount) throws PPGameActionException{
		if(this.health >= 0){
			this.health -= amount;
		}
		else{
			throw new PPGameActionException("Cannot damage a negative amount");
		}
	}

	public void receiveHeal(int amount) throws PPGameActionException{
		if(this.health >= 0){
			this.health += amount;
		}
		else{
			throw new PPGameActionException("Cannot heal a negative amount");
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
