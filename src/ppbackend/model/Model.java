package ppbackend.model;

import java.util.*;

import pplib.exceptions.*;
import pplib.DatabaseConnection;

import ppbackend.control.DatabaseReader;
import ppbackend.model.mainStruct.*;

public class Model{
	int maxGameCountPerPlayer = 10;
	int gameCount;
	int version;
	HashMap<Integer,Game> games;
	HashMap<Integer,ArrayList<Integer>> userMap;
	DatabaseReader databaseReader;
	DatabaseConnection databaseConnection;

	public Model(int numGames) throws PPLoadException{
		this.games = new HashMap<Integer,Game>(numGames);
		this.gameCount = 1;
		this.version = 0;
		this.userMap = new HashMap<Integer,ArrayList<Integer>>();
		try{
			databaseConnection = new DatabaseConnection("pp_shared");
			databaseReader = new DatabaseReader();
		}
		catch(PPDatabaseException e){
			System.out.println(e.getMessage());
			System.exit(1);
		}
		try{
			//TODO have all the data come back (need to call rs.getString(2) in this case, need to do this smartly
			ArrayList<String> rawGame = databaseConnection.select("select * from play_games");
			System.out.println(rawGame);
			this.gameCount = rawGame.size()+1;
		}
		catch(PPDatabaseException e){
			throw new PPLoadException("Could not load games from database "+e.getMessage());
		}
	}

	public String ppserialize(int gameId, int uid) throws PPGameActionException{
		return getGameFromGameId(gameId).ppserialize(uid);
	}

	public int startGame(int p1Uid, int p1Did, int p2Uid, int p2Did) throws PPGameActionException{
		if(canStartGame(p1Uid) && canStartGame(p2Uid)){
			int gameId = getNextId();
			Game game;
			try{
				game = databaseReader.getGame(p1Uid, p1Did, p2Uid, p2Did);
			}
			catch(PPDatabaseException e){
				throw new PPGameActionException("Player didn't exist? "+e.getMessage());
			}
			game.shuffle();
			try{
				//TODO actually write game to disk
				databaseConnection.update("insert into play_games values("+Integer.toString(gameId)+",'"+game.ppserialize(PlayerType.full)+"')");
				//databaseConnection.update("insert into play_games values("+Integer.toString(gameId)+",'hi')");
			}
			catch(PPDatabaseException e){
				throw new PPGameActionException("Error writing game data "+e.getMessage());
			}
			bookKeepGame(game,gameId,p1Uid,p2Uid);
			return gameId;
		}
		else{
			throw new PPGameActionException("Cannot start any more games");
		}
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

	private void bookKeepGame(Game game, int gameId, int uid1, int uid2){
		ArrayList<Integer> userGames;
		if(!this.userMap.containsKey(uid1)){
			userGames = new ArrayList<Integer>();
			this.userMap.put(uid1,userGames);
		}
		else{
			userGames = this.userMap.get(uid1);
		}
		userGames.add(gameId);
		if(!this.userMap.containsKey(uid2)){
			userGames = new ArrayList<Integer>();
			this.userMap.put(uid2,userGames);
		}
		else{
			userGames = this.userMap.get(uid2);
		}
		userGames.add(gameId);
		this.games.put(gameId,game);
	}

	private boolean canStartGame(int uid){
		return getGameIdsFromUid(uid).size() < maxGameCountPerPlayer;
	}

	private int getNextId(){
		int ret = this.gameCount;
		this.gameCount++;
		return ret;
	}
}
