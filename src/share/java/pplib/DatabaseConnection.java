package pplib;

import java.util.ArrayList;
import java.sql.*;

import pplib.exceptions.PPDatabaseException;

public class DatabaseConnection{
	Connection con;

	public DatabaseConnection(String databaseName) throws PPDatabaseException{
		try{
		this.con = DriverManager.getConnection("jdbc:mysql://localhost/"+databaseName,"developer","jfjfkdkdlslskdkdjfjf");
		}
		catch(SQLException e){
			System.out.println(e.getMessage());
			throw new PPDatabaseException("Could not connect to database "+databaseName);
		}
	}
	public ArrayList<String> select(String sqlCommand) throws PPDatabaseException{
		try{
			Statement st = this.con.createStatement();
			ResultSet rs = st.executeQuery(sqlCommand);
			ArrayList<String> ret = new ArrayList<String>();
			for(int i=1;rs.next();i++){
				ret.add(rs.getString(i));
			}
			return ret;
		}
		catch(SQLException e){
			System.out.println(e.getMessage());
			throw new PPDatabaseException("Error running command"+e.getMessage());
		}
	}

	public void update(String sqlCommand) throws PPDatabaseException{
		try{
			Statement st = this.con.createStatement();
			st.executeUpdate(sqlCommand);
		}
		catch(SQLException e){
			System.out.println(e.getMessage());
			throw new PPDatabaseException("Error running command"+e.getMessage());
		}
	}
}
