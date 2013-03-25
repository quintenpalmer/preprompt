package pplib;

import pplib.exceptions.PPDatabaseException;

public class DatabaseConnection{
	public static String[] run(String sqlCommand) throws PPDatabaseException{
		String[] ret = {"hi","you"};
		return ret;
	}
}
