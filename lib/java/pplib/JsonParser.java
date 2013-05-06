package pplib;

import java.io.IOException;
import java.util.List;

import org.json.simple.*;
import org.json.simple.parser.*;

import pplib.EasyFileReader;
import pplib.exceptions.*;

public class JsonParser{
	JSONParser parser;

	public JsonParser(){
		parser = new JSONParser();
	}

	public JSONObject createObject(String filename) throws PPJsonException{
		try{
			String jsonString = EasyFileReader.readFileToString(filename);
			JSONParser parser = new JSONParser();
			JSONObject object = (JSONObject)parser.parse(jsonString);
			return object;
		}
		catch (IOException|ParseException e){
			throw new PPJsonException(e.getMessage());
		}
	}

	public Object getRaw(JSONObject object, String tag){
		return object.get(tag);
	}

	public JSONObject getObject(JSONObject object, String tag){
		JSONObject retObject = (JSONObject)object.get(tag);
		return retObject;
	}

	public JSONArray getArray(JSONObject object, String tag){
		JSONArray array = (JSONArray)object.get(tag);
		return array;
	}

	public Object getString(JSONObject object, String tag){
		String string = (String)object.get(tag);
		return string;
	}

	public int getInt(JSONObject object, String tag){
		int integer = ((Long)object.get(tag)).intValue();
		return integer;
	}
}
