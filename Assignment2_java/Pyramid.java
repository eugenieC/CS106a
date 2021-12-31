package cs106;

import acm.graphics.*;
import acm.program.*;

public class Pyramid extends GraphicsProgram {
		// constants
	private static final int BRICK_WIDTH = 30;
	private static final int BRICK_HEIGHT = 12;
	private static final int BRICKS_IN_BASE = 14;
	
	public void run() {
		// defining variables
		int x;
		int y;
		int beginX;
		int beginY;
		
		// defining beginning coordinates
		beginX = (getWidth())/(2) - BRICK_WIDTH*((BRICKS_IN_BASE)/(2));
		beginY = getHeight() - BRICK_HEIGHT;
		
		// changing y coordinates of bricks
		for (int i = 0; i < BRICKS_IN_BASE; i++) {
			
			y = beginY - i * BRICK_HEIGHT;
		
		// changing x coordinates of bricks
			
		for (int j = 0; j < (BRICKS_IN_BASE-i); j++) {
			
			x = beginX + BRICK_WIDTH * j + (i * BRICK_WIDTH/2);
			
			GRect Block = new GRect(x, y, BRICK_WIDTH, BRICK_HEIGHT);
			add(Block);
		}
		}	
	}
}