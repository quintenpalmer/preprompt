package client.view;

import client.model.Model;
import shared.model.constants.Constants;
import org.lwjgl.LWJGLException;
import org.lwjgl.opengl.Display;
import org.lwjgl.opengl.DisplayMode;
import org.lwjgl.opengl.GL11;
import org.lwjgl.input.Mouse;
import org.lwjgl.input.Keyboard;
import org.lwjgl.util.glu.Project;
import org.lwjgl.util.glu.GLU;
import org.lwjgl.BufferUtils;
import java.io.*;
import java.nio.FloatBuffer;

/** The View of the M-V-C Pattern
*/
public class View{

	GameDrawer gd;

	/** contructor for the View
	* @return A new fantastic point of View
	*/
	public View(){
		gd = new GameDrawer();
	}

	int mouseX = 0;
	int mouseY = 0;
	boolean finished = false;

	float in = 0.0f;

	float xspin = 0.0f;
	float yspin = 0.0f;
	float zspin = 0.0f;

	/** Initializes all of the GL requirements
	 * Sets up GL for displaying 3D graphics
	 */
	public void init(){
		try {
			Display.setDisplayMode(new DisplayMode(Constants.windowWidthInt,Constants.windowHeightInt));
			Display.create();
		}catch (LWJGLException e) {
			e.printStackTrace();
			System.exit(0);
		}

		GL11.glClearColor(1.0f,1.0f,1.0f,0.0f);
		GL11.glColor3f(0.0f,0.0f,0.0f);
		GL11.glPointSize(1.0f);
		GL11.glMatrixMode(GL11.GL_PROJECTION);
		GL11.glLoadIdentity( );
		GLU.gluOrtho2D(0.0f,Constants.windowWidth,0.0f,Constants.windowHeight);
		GL11.glClear(GL11.GL_COLOR_BUFFER_BIT);


		GL11.glEnable(GL11.GL_LIGHTING);
		GL11.glEnable(GL11.GL_LIGHT0);
		GL11.glShadeModel(GL11.GL_SMOOTH);
		GL11.glEnable(GL11.GL_DEPTH_TEST);
		GL11.glEnable(GL11.GL_NORMALIZE);
	
		GL11.glEnable(GL11.GL_COLOR_MATERIAL);
		GL11.glColorMaterial(GL11.GL_FRONT, GL11.GL_AMBIENT_AND_DIFFUSE);
		GL11.glEnable(GL11.GL_LINE_SMOOTH);
		GL11.glLineWidth(5.0f);

		// sets up the light
		FloatBuffer lightPosition = BufferUtils.createFloatBuffer(4).put(new float[] {50.0f, 50.0f, 10.0f, 1.0f });
		lightPosition.flip();
		FloatBuffer lightAmbient = BufferUtils.createFloatBuffer(4).put(new float[] {0.2f, 0.2f, 0.2f, 1.0f });
		lightAmbient.flip();
		FloatBuffer lightDiffuse = BufferUtils.createFloatBuffer(4).put(new float[] {0.5f, 0.5f, 0.5f, 1.0f });
		lightDiffuse.flip();
		GL11.glLight(GL11.GL_LIGHT0,GL11.GL_AMBIENT,lightAmbient);
		GL11.glLight(GL11.GL_LIGHT0,GL11.GL_DIFFUSE,lightDiffuse);
		GL11.glLight(GL11.GL_LIGHT0,GL11.GL_POSITION,lightPosition);


	}

	/** The GL to be run on each tick
	 * with diffuse and ambient lights
	 */
	public void run(Model model) throws IOException{
		while (!finished) {
			if(Display.isCloseRequested()){
				finished = true;
			}
			GL11.glMatrixMode(GL11.GL_PROJECTION);
			GL11.glLoadIdentity( );
			GL11.glClear(GL11.GL_COLOR_BUFFER_BIT | GL11.GL_DEPTH_BUFFER_BIT);
			GL11.glColor3f(.1f,.1f,.5f);

			// reset
			//GL11.glOrtho(-80,80,-80,80,-80,80);
			GLU.gluPerspective(90f,Constants.aspectRatio,10f/*Constants.boardHeight*/,Constants.boardHeight*3);
			GL11.glMatrixMode(GL11.GL_MODELVIEW);
			GL11.glLoadIdentity();
			Project.gluLookAt(Constants.boardWidth/2,Constants.viewHeight,Constants.boardHeight, Constants.boardWidth/2,0,Constants.boardHeight/2, 0,1,0);

			GL11.glPushMatrix();
				GL11.glTranslatef(in,0.0f,0.0f);
				GL11.glRotatef(xspin,1.0f,0.0f,0.0f);
				GL11.glRotatef(yspin,0.0f,1.0f,0.0f);
				GL11.glRotatef(zspin,0.0f,0.0f,1.0f);
				gd.draw(model);
			GL11.glPopMatrix();
			handleKey(model);
			handleMouse(model);
			//GL11.glFlush();
			Display.update();
		}
	}

	/** closes the GL when finished
	 */
	public void finish(){
		Display.destroy();
	}

	/** Handles the mouse input
	 * Currently rotates the space based on mouse movement
	 */
	public void handleMouse(Model model) throws IOException{
		int currentMouseX = Mouse.getX();
		int currentMouseY = Mouse.getY();
		if(Mouse.isButtonDown(0)){
			//yspin += currentMouseX - mouseX;
			xspin += currentMouseY - mouseY;
		}
		mouseX = currentMouseX;
		mouseY = currentMouseY;
	}

	/** Handles the key input
	 * Currently rotates/displaces the space based on keyboard input
	 * 'x' closes the program
	 */
	public void handleKey(Model model) throws IOException{
		while(Keyboard.next()){
			if(Keyboard.getEventKeyState()){
				switch(Keyboard.getEventKey()){
					case(Keyboard.KEY_A): yspin += 5f;
						break;
					case(Keyboard.KEY_D): yspin -= 5f;
						break;
					case(Keyboard.KEY_Q): xspin += 5f;
						break;
					case(Keyboard.KEY_E): xspin -= 5f;
						break;
					case(Keyboard.KEY_W): zspin += 5f;
						break;
					case(Keyboard.KEY_S): zspin -= 5f;
						break;
					case(Keyboard.KEY_X): finished = true;
						break;
					case(Keyboard.KEY_Z): in += 5f;
						break;
					case(Keyboard.KEY_C): in -= 5f;
						break;
					case(Keyboard.KEY_F): in -= 5f;//ClientControl.sendRequest(model, "new 1 1 2 2");
						break;
					case(Keyboard.KEY_G): in += 5f;//ClientControl.sendRequest(model, "perform 1 1 draw");
						break;
					default: System.out.println("NOKEY");
				}
			}
		}
	}
}
