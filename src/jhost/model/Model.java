package model;

import java.util.HashMap;

import pplib.errors.*;
import pplib.Database;

import control.DatabaseReader;
import control.ConfigArg;
import model.Game;

public class Model{
	int gameCount;
	int version;
	Game[] games;
	HashMap<Integer,Game> userMap;

	public Model(int numGames) throws PPLoadException{
		this.games = new Game[numGames];
		this.gameCount = 0;
		this.version = 0;
		this.userMap = new HashMap<Integer,Game>();
		try{
			String[] rawGame = Database.run("select * from play_games");
		}
		catch(PPDatabaseException e){
			throw new PPLoadException("Could not load games from database");
		}
	}

	public void startGame(ConfigArg configArg){
		int gameId = getNextId();
		Game game = DatabaseReader.getGame(configArg);
	}

	private int getNextId(){
		int ret = this.gameCount;
		this.gameCount++;
		return ret;
	}
}
