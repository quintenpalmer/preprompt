package shared.model.constants;

/** Used for constants in display and more
*/
public class Constants{
	/* Gameplay related constants
	 */

	// the number of cards a player is allowed to have active
	public static final int numActiveCard = 5;

	/* Display related constants
	 */

	// width of a card
	public static final float cardWidth = 5f;
	// height of a card
	public static final float cardHeight = 7f;
	// width of a card with boundaries so that they are not all touching
	public static final float outerCardWidth = 6f;
	// height of a card with boundaries so that they are not all touching
	public static final float outerCardHeight = 8f;

	// width of the active playing area
	public static final float activeWidth = outerCardWidth * numActiveCard;
	// height of the game board
	public static final float boardWidth = outerCardWidth * (numActiveCard + 2);
	// height of the game board
	public static final float boardHeight = outerCardHeight * 6;

	// Deck locations
	public static final float deckX = 0f;
	public static final float deckY = outerCardHeight;
	public static final float meDeckX = deckX;
	public static final float meDeckY = deckY;
	public static final float themDeckX = deckX;
	public static final float themDeckY = 5 * outerCardHeight - deckY;

	// Hand locations
	public static final float handX = outerCardWidth;
	public static final float handY = outerCardHeight;
	public static final float meHandX = handX;
	public static final float meHandY = handY;
	public static final float themHandX = handX;
	public static final float themHandY = 5 * outerCardHeight - handY;

	// Grave locations
	public static final float graveX = 0f;
	public static final float graveY = outerCardHeight * 2;
	public static final float meGraveX = graveX;
	public static final float meGraveY = graveY;
	public static final float themGraveX = graveX;
	public static final float themGraveY = 5 * outerCardHeight - graveY;

	// Active locations
	public static final float activeX = outerCardWidth;
	public static final float activeY = outerCardHeight * 2;
	public static final float meActiveX = activeX;
	public static final float meActiveY = activeY;
	public static final float themActiveX = activeX;
	public static final float themActiveY = 5 * outerCardHeight - activeY;

	// into the up dimension for the camera
	public static final float viewHeight = 7f * 4f;

	// how far off of the table the cards are
	public static final float cardRise = .5f;
	// how far off of the table the location markers are
	public static final float locationRise = .25f;

	// width of the a player's plate in game
	public static final float playerPlateWidth = 8f;
	// height of the a player's plate in game
	public static final float playerPlateHeight = 4f;

	// x offset for drawing the current player's playing area
	public static final float meOffsetX = outerCardHeight * 0;
	// y offset for drawing the current player's playing area
	public static final float meOffsetY = outerCardWidth * 0;
	// x offset for drawing the opposing player's playing area
	public static final float themOffsetX = outerCardHeight * 2;
	// y offset for drawing the opposing player's playing area
	public static final float themOffsetY = outerCardWidth * 0;

	// width of window
	public static final int windowWidthInt = 900;
	public static final float windowWidth = 900f;
	// height of window
	public static final int windowHeightInt = 700;
	public static final float windowHeight = 700f;
}
