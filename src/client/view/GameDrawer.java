package client.view;

import client.model.Model;
import client.model.game.ClientGame;
import client.model.player.ClientPlayer;
import client.model.player.ClientPlayerContainer;
import client.model.deck.ClientDeck;
import client.model.card.ClientCard;
import client.model.display.DisplayInfo;
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
		drawRhomb(5f);
		if(game!=null){
			ClientPlayerContainer pc1 = game.getPlayer(1);
			ClientPlayerContainer pc2 = game.getPlayer(2);

			drawGame(game);
			if(pc1!=null){
				ClientPlayer p1 = pc1.getPlayer();
				ClientDeck d1 = pc1.getDeck();
				drawPlayer1(p1);
				drawDeck1(d1);
			}
			if(pc2!=null){
				ClientPlayer p2 = pc2.getPlayer();
				ClientDeck d2 = pc2.getDeck();
				drawPlayer2(p2);
				drawDeck2(d2);
			}
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

		drawQuad(0,0,0,Constants.boardWidth,Constants.boardHeight,gameColor);

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
		float[] color = {.1f,.7f,.2f};
		float playerHealth = (float)player.getHealth();
		float red = (Constants.startHealth-playerHealth) / 50f;
		float[] healthColor = {red,playerHealth/50f,0f};
		drawQuad(Constants.mePlayerX,Constants.locationRise,Constants.mePlayerY,Constants.playerPlateWidth,Constants.playerPlateHeight,color);
		drawQuad(Constants.mePlayerInfoX,Constants.locationRise,Constants.mePlayerInfoY,Constants.playerPlateWidth,Constants.playerPlateHeight,healthColor);
	}

	/** Draws player 2
	 * @param player the player to draw
	 */
	private void drawPlayer2(ClientPlayer player){
		float[] color = {.7f,.1f,.2f};
		float playerHealth = (float)player.getHealth();
		float red = (Constants.startHealth-playerHealth) / 50f;
		float[] healthColor = {red,playerHealth/50f,0f};
		drawQuad(Constants.themPlayerX,Constants.locationRise,Constants.themPlayerY,Constants.playerPlateWidth,Constants.playerPlateHeight,color);
		drawQuad(Constants.themPlayerInfoX,Constants.locationRise,Constants.themPlayerInfoY,Constants.playerPlateWidth,Constants.playerPlateHeight,healthColor);
	}

	/** Draws player 1's deck
	 * @param deck the deck to draw
	 */
	private void drawDeck1(ClientDeck deck){
		float[] color = {.5f,.1f,.1f};
		if(deck.getStack().getSize() > 0){
			drawQuad(Constants.meDeckX,Constants.locationRise,Constants.meDeckY,Constants.cardWidth,Constants.cardHeight,color);
		}
		/*
		drawQuad(Constants.meHandX,Constants.locationRise,Constants.meHandY,Constants.activeWidth,Constants.outerCardHeight,handColor);
		drawQuad(Constants.meActiveX,Constants.locationRise,Constants.meActiveY,Constants.activeWidth,Constants.outerCardHeight,activeColor);
		drawQuad(Constants.meGraveX,Constants.locationRise,Constants.meGraveY,Constants.activeWidth,Constants.outerCardHeight,graveColor);
		*/
	}

	/** Draws player 2's deck
	 * @param deck the deck to draw
	 */
	private void drawDeck2(ClientDeck deck){
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

	private void drawRhomb(float size){
		GL11.glPushMatrix();
		DisplayInfo.tick();
		GL11.glTranslatef(-10f,0f,0f);
		GL11.glRotatef((float)DisplayInfo.getRhot(),0f,1f,0f);
		GL11.glScalef(size,size,size);
        for (int i = 0; i < 12; i++) {
            //GL11.glBegin(GL11.GL_LINE_LOOP);
			GL11.glBegin(GL11.GL_QUADS);
            GL11.glNormal3d(rdod_n[i][0], rdod_n[i][1], rdod_n[i][2]);
            for (int j = 0; j <= 3; j++) {
                GL11.glVertex3d(rdod_r[rdod_v[i][j]][0], rdod_r[rdod_v[i][j]][1], rdod_r[rdod_v[i][j]][2]);
            }
            GL11.glEnd();
        }
		GL11.glPopMatrix();
	}

	private static final double rdod_r[][] = {
            {0.0, 0.0, 1.0},
            {0.707106781187, 0.000000000000, 0.5},
            {0.000000000000, 0.707106781187, 0.5},
            {-0.707106781187, 0.000000000000, 0.5},
            {0.000000000000, -0.707106781187, 0.5},
            {0.707106781187, 0.707106781187, 0.0},
            {-0.707106781187, 0.707106781187, 0.0},
            {-0.707106781187, -0.707106781187, 0.0},
            {0.707106781187, -0.707106781187, 0.0},
            {0.707106781187, 0.000000000000, -0.5},
            {0.000000000000, 0.707106781187, -0.5},
            {-0.707106781187, 0.000000000000, -0.5},
            {0.000000000000, -0.707106781187, -0.5},
            {0.0, 0.0, -1.0}
    };

    private static final int rdod_v[][] = {
            {0, 1, 5, 2},
            {0, 2, 6, 3},
            {0, 3, 7, 4},
            {0, 4, 8, 1},
            {5, 10, 6, 2},
            {6, 11, 7, 3},
            {7, 12, 8, 4},
            {8, 9, 5, 1},
            {5, 9, 13, 10},
            {6, 10, 13, 11},
            {7, 11, 13, 12},
            {8, 12, 13, 9}
    };

    private static final double rdod_n[][] = {
            {0.353553390594, 0.353553390594, 0.5},
            {-0.353553390594, 0.353553390594, 0.5},
            {-0.353553390594, -0.353553390594, 0.5},
            {0.353553390594, -0.353553390594, 0.5},
            {0.000000000000, 1.000000000000, 0.0},
            {-1.000000000000, 0.000000000000, 0.0},
            {0.000000000000, -1.000000000000, 0.0},
            {1.000000000000, 0.000000000000, 0.0},
            {0.353553390594, 0.353553390594, -0.5},
            {-0.353553390594, 0.353553390594, -0.5},
            {-0.353553390594, -0.353553390594, -0.5},
            {0.353553390594, -0.353553390594, -0.5}
    };
}
