package client.view;

import client.model.Model;
import client.model.game.ClientGame;
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
		if(game!=null){
			drawGame(game);
		}
	}
	
	/** Draws the backdrop for the game
	* @param card a ClientCard to be drawn
	*/
	private void drawGame(ClientGame game){
		float[] colors = {.39f,.32f,.28f};
		GL11.glRotatef(0f,0f,0f,0f);
		drawQuad(0,0,0,Constants.boardWidth,Constants.boardHeight,colors);
	}

	/** Draws an individual Card
	* @param card a ClientCard to be drawn
	*/
	private void drawCard(ClientCard card){
		float[] colors = {0f,.5f,0f};
		GL11.glRotatef(0f,0f,0f,0f);
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
				GL11.glVertex3f(x,y+height,z);
				GL11.glVertex3f(x+width,y+height,z);
				GL11.glVertex3f(x+width,y,z);
			GL11.glEnd();
		GL11.glPopMatrix();
	}
}
