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

	public static String[] names = {
		"deck",
		"hand",
		"active",
		"grave",
		"special",
		"other"
	};

	public static HashMap<String,Integer> values = new HashMap<String,Integer>();
	static{
		values.put("deck",deck);
		values.put("hand",hand);
		values.put("active",active);
		values.put("grave",grave);
		values.put("special",special);
		values.put("other",other);
	}
}
