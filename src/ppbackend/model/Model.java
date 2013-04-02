package ppbackend.model;

import java.util.HashMap;
import java.util.ArrayList;

import pplib.exceptions.*;
import pplib.DatabaseConnection;

import ppbackend.control.DatabaseReader;
import ppbackend.model.Game;
import ppbackend.model.CLTypes;

public class Model{
	int maxGameCount = 10;
	int gameCount;
	int version;
	HashMap<Integer,Game> games;
	HashMap<Integer,ArrayList<Integer>> userMap;
	DatabaseReader databaseReader = new DatabaseReader();
	DatabaseConnection databaseConnection = new DatabaseConnection();

	public Model(int numGames) throws PPLoadException{
		this.games = new HashMap<Integer,Game>(numGames);
		this.gameCount = 0;
		this.version = 0;
		this.userMap = new HashMap<Integer,ArrayList<Integer>>();
		try{
			String[] rawGame = databaseConnection.run("select * from play_games");
		}
		catch(PPDatabaseException e){
			throw new PPLoadException("Could not load games from database");
		}
	}

	public int startGame(int p1Uid, int p1Did, int p2Uid, int p2Did) throws PPGameActionException{
		if(canStartGame(p1Uid) && canStartGame(p2Uid)){
			int gameId = getNextId();
			Game game = DatabaseReader.getGame(p1Uid, p1Did, p2Uid, p2Did);
			for(PlayerContainer pc : game.getPlayers()){
				pc.getDeck().getCardList(CLTypes.deck).shuffle();
			}
			try{
				databaseConnection.run("insert into play_games ");
			}
			catch(PPDatabaseException e){
				throw new PPGameActionException("Error writing game data");
			}
			bookKeepGame(gameId,game,p1Uid,p2Uid);
			return gameId;
		}
		else{
			throw new PPGameActionException("Cannot start any more games");
		}
	}

	public void bookKeepGame(int gameId, Game game, int uid1, int uid2){
		ArrayList<Integer> games;
		if(!this.userMap.containsKey(uid1)){
			games = new ArrayList<Integer>();
			this.userMap.put(uid1,games);
		}
		else{
			games = this.userMap.get(uid1);
		}
		games.add(gameId);
		if(!this.userMap.containsKey(uid2)){
			games = new ArrayList<Integer>();
			this.userMap.put(uid2,games);
		}
		else{
			games = this.userMap.get(uid2);
		}
		games.add(gameId);

		this.games.put(gameId,game);
	}

	private int getNextId(){
		int ret = this.gameCount;
		this.gameCount++;
		return ret;
	}

	public int getVersion(){
		return this.version;
	}

	public ArrayList<Integer> getGameIdsFromUid(int uid){
		if(this.userMap.containsKey(uid)){
			return this.userMap.get(uid);
		}
		else{
			return new ArrayList<Integer>(0);
		}
	}

	public Game getGameFromGameId(int gameId) throws PPGameActionException{
		if(this.games.containsKey(gameId)){
			return this.games.get(gameId);
		}
		else{
			throw new PPGameActionException("That gameId is not in play");
		}
	}

	public boolean canStartGame(int uid){
		return getGameIdsFromUid(uid).size() < maxGameCount;
	}

	public String out(int gameId, int uid) throws PPGameActionException{
		return getGameFromGameId(gameId).xmlOutput(uid);
	}
}
