package ppbackend.model.shared;

import java.util.HashMap;

public class CLTypes{
	public static int deck = 0;
	public static int hand = 1;
	public static int active = 2;
	public static int grave = 3;
	public static int special = 4;
	public static int other = 5;

	public static int size = 6;

	public static String[] names =
	{"deck",
	"hand",
	"active",
	"grave",
	"special",
	"other"};

	/*
	public static HashMap<String,Integer> values = new HashMap<String,Integer>();
	values["deck"] = deck;
	values["hand"] = hand;
	values["active"] = active;
	values["grave"] = grave;
	values["special"] = special;
	values["other"] = other;
	*/
}
