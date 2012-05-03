package client.model.display;

public class DisplayInfo{
	static int rhotate = 0;

	public static void tick(){
		rhotate += 1;
		if(rhotate>359){
			rhotate = 0;
		}
	}

	public static int getRhot(){
		return rhotate;
	}
}
