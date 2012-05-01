package client.view;

import client.model.Model;
import client.model.game.ClientGame;
import client.model.player.ClientPlayer;
import client.model.card.ClientCard;
import org.lwjgl.opengl.GL11;
import shared.model.constants.Constants;

/** GameDrawer is responsible for drawing the game onto the screen
*/
public class GameDrawer{

	/** Draw is used to draw the game onto the screen
	* @param model the game model to draw
	*/
	public void draw(Model model){
		ClientGame game = model.getGame();
		ClientPlayer p1 = model.getGame().getPlayer(1);
		ClientPlayer p2 = model.getGame().getPlayer(2);
		if(game!=null){
			drawGame(game);
		}
		if(p1!=null){
			drawPlayer1(p1);
		}
		if(p2!=null){
			drawPlayer2(p2);
		}
	}
	
	/** Draws the backdrop for the game
	 * @param card a ClientCard to be drawn
	 */
	private void drawGame(ClientGame game){
		float[] gameColor = {.39f,.32f,.28f};
		float[] deckColor = {.52f,.40f,.34f};
		float[] handColor = {.65f,.53f,.47f};
		float[] activeColor = {.45f,.43f,.97f};
		float[] graveColor = {.15f,.13f,.17f};

		drawQuad(0,0,Constants.cardRise,Constants.boardWidth,Constants.boardHeight,gameColor);

		drawQuad(Constants.meDeckX,Constants.locationRise,Constants.meDeckY,Constants.outerCardWidth,Constants.outerCardHeight,deckColor);
		drawQuad(Constants.meHandX,Constants.locationRise,Constants.meHandY,Constants.activeWidth,Constants.outerCardHeight,handColor);
		drawQuad(Constants.meActiveX,Constants.locationRise,Constants.meActiveY,Constants.activeWidth,Constants.outerCardHeight,activeColor);
		drawQuad(Constants.meGraveX,Constants.locationRise,Constants.meGraveY,Constants.activeWidth,Constants.outerCardHeight,graveColor);

		drawQuad(Constants.themDeckX,Constants.locationRise,Constants.themDeckY,Constants.outerCardWidth,Constants.outerCardHeight,deckColor);
		drawQuad(Constants.themHandX,Constants.locationRise,Constants.themHandY,Constants.activeWidth,Constants.outerCardHeight,handColor);
		drawQuad(Constants.themActiveX,Constants.locationRise,Constants.themActiveY,Constants.activeWidth,Constants.outerCardHeight,activeColor);
		drawQuad(Constants.themGraveX,Constants.locationRise,Constants.themGraveY,Constants.activeWidth,Constants.outerCardHeight,graveColor);
	}

	/** Draws player 1
	 * @param player the player to draw
	 */
	private void drawPlayer1(ClientPlayer player){

	}

	/** Draws player 2
	 * @param player the player to draw
	 */
	private void drawPlayer2(ClientPlayer player){

	}

	/** Draws a player
	 * @param player the ClientPlayer to draw
	 * @param playerNum the number the player is in the game
	 */
	private void drawPlayer(ClientPlayer player, int playerNum){
		float[] colors = {1f,.3f,.3f};
		drawQuad(0,0,0,Constants.playerPlateWidth,Constants.playerPlateHeight,colors);
		drawQuad(0,0,0,Constants.playerPlateWidth,Constants.playerPlateHeight,colors);
	}

	/** Draws an individual Card
	 * @param card a ClientCard to be drawn
	 */
	private void drawCard(ClientCard card){
		float[] colors = {0f,.5f,0f};
		drawQuad(0,0,0,Constants.cardWidth,Constants.cardHeight,colors);
	}

	/** Draws a quadrilateral at the given (x,y,z) with the 
	 * given width and height and of the given color
	 * @param x the x position to draw the quad at
	 * @param y the y position to draw the quad at
	 * @param z the z position to draw the quad at
	 * @param width the width of the quad to draw
	 * @param height the height of the quad to draw
	 * @param colors what color to draw the quad
	 */
	private void drawQuad(float x, float y, float z, float width, float height, float[] colors){
		GL11.glPushMatrix();
			GL11.glColor3f(colors[0],colors[1],colors[2]);
			GL11.glBegin(GL11.GL_QUADS);
				GL11.glVertex3f(x,y,z);
				GL11.glVertex3f(x,y,z+height);
				GL11.glVertex3f(x+width,y,z+height);
				GL11.glVertex3f(x+width,y,z);
			GL11.glEnd();
		GL11.glPopMatrix();
	}
}
