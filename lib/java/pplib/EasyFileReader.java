package pplib;

import java.io.*;
import java.lang.*;

public class EasyFileReader{
	public static String readFileToString(String filename) throws IOException{
		BufferedReader reader = new BufferedReader(new FileReader(filename));
		try{
			StringBuffer fileContents = new StringBuffer();
			char[] buf = new char[1024];
			int numRead = 0;
			while((numRead = reader.read(buf)) != -1){
				String readData = String.valueOf(buf, 0, numRead);
				fileContents.append(readData);
			}
			return fileContents.toString();
		}
		finally{
			reader.close();
		}
	}
}
