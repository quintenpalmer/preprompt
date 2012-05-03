package shared.model.constants;

/** Used for constants in display and more
*/
public class Constants{
	/* Gameplay related constants
	 */

	// the number of cards a player is allowed to have active
	public static final int numActiveCard = 5;

	public static final int startHealth = 50;

	/* Display related constants
	 */

	// scale factor between card with and height (width / height)
	public static final float cardScale = 1.4f;
	// width of a card
	public static final float cardWidth = 5f;
	// height of a card
	public static final float cardHeight = cardWidth * cardScale;
	// scale factor that the buffer card size is over the card size
	public static final float cardOuterScale = 1.2f;
	// width of a card with boundaries so that they are not all touching
	public static final float outerCardWidth = cardWidth * cardOuterScale;
	// height of a card with boundaries so that they are not all touching
	public static final float outerCardHeight = cardHeight * cardOuterScale;

	// width of the active playing area
	public static final float activeWidth = outerCardWidth * numActiveCard;
	// height of the game board
	public static final float boardWidth = outerCardWidth * (numActiveCard + 2);
	// height of the game board
	public static final float boardHeight = outerCardHeight * 6;

	// width of the a player's plate in game
	public static final float playerPlateWidth = outerCardWidth * 2;
	// height of the a player's plate in game
	public static final float playerPlateHeight = outerCardHeight;

	// Deck locations
	public static final float deckX = 0f;
	public static final float deckY = outerCardHeight;
	public static final float themDeckX = deckX;
	public static final float themDeckY = deckY;
	public static final float meDeckX = deckX;
	public static final float meDeckY = 5 * outerCardHeight - deckY;

	// Hand locations
	public static final float handX = outerCardWidth;
	public static final float handY = outerCardHeight;
	public static final float themHandX = handX;
	public static final float themHandY = handY;
	public static final float meHandX = handX;
	public static final float meHandY = 5 * outerCardHeight - handY;

	// Grave locations
	public static final float graveX = 0f;
	public static final float graveY = outerCardHeight * 2;
	public static final float themGraveX = graveX;
	public static final float themGraveY = graveY;
	public static final float meGraveX = graveX;
	public static final float meGraveY = 5 * outerCardHeight - graveY;

	// Active locations
	public static final float activeX = outerCardWidth;
	public static final float activeY = outerCardHeight * 2;
	public static final float themActiveX = activeX;
	public static final float themActiveY = activeY;
	public static final float meActiveX = activeX;
	public static final float meActiveY = 5 * outerCardHeight - activeY;

	// Player Display locations
	public static final float playerX = 0f;
	public static final float playerY = 0f;
	public static final float themPlayerX = playerX;
	public static final float themPlayerY = playerY;
	public static final float mePlayerX = playerX;
	public static final float mePlayerY = 5 * outerCardHeight - playerY;

	// Player Info Display locations
	public static final float playerInfoX = playerPlateWidth;
	public static final float playerInfoY = 0f;
	public static final float themPlayerInfoX = playerInfoX;
	public static final float themPlayerInfoY = playerInfoY;
	public static final float mePlayerInfoX = playerInfoX;
	public static final float mePlayerInfoY = 5 * outerCardHeight - playerInfoY;

	// into the up dimension for the camera
	public static final float viewHeight = 7f * 4f;

	// how far off of the table the cards are
	public static final float cardRise = 1f;
	// how far off of the table the location markers are
	public static final float locationRise = .5f;

	// width of window
	public static final int windowWidthInt = 1700;
	public static final float windowWidth = 1700f;
	// height of window
	public static final int windowHeightInt = 900;
	public static final float windowHeight = 900f;

	// aspect ratio (width/height)
	public static final float aspectRatio = windowWidth/windowHeight;

	// Framerate to display at
	public static final int Framerate = 60;


	/* Temp and Testing
	 */
	// name of the current player
	public static final String me = "vim";
	// name of the opposing player
	public static final String them = "emacs";
}
