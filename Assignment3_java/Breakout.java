package cs106;

import acm.graphics.*;
import acm.program.*;
import acm.util.*;
import java.applet.*;
import java.awt.*;
import java.awt.event.*;

public class Breakout extends GraphicsProgram {
	public void init() { 
		this.setSize(400, 1200);
	}
	
	//variables
	
	/** Width and height of application window in pixels */ 
	public static final int APPLICATION_WIDTH = 400; 
	public static final int APPLICATION_HEIGHT = 600;
	
	/** Dimensions of game board (usually the same) */ 
	private static final int WIDTH = APPLICATION_WIDTH; 
	private static final int HEIGHT = APPLICATION_HEIGHT;

	/** Dimensions of the paddle */
	private static final int PADDLE_WIDTH = 60; 
	private static final int PADDLE_HEIGHT = 10;
	
	/** Offset of the paddle up from the bottom */ 
	private static final int PADDLE_Y_OFFSET = 30;

	/** Number of bricks per row */
	private static final int NBRICKS_PER_ROW = 10;

	/** Number of rows of bricks */
	private static final int NBRICK_ROWS = 10;

	/** Separation between bricks */
	private static final int BRICK_SEP = 4;

	/** Width of a brick */
	private static final int BRICK_WIDTH = (WIDTH - (NBRICKS_PER_ROW - 1) * BRICK_SEP)/NBRICKS_PER_ROW;
	
	/** Height of a brick */
	private static final int BRICK_HEIGHT = 8;
	
	/** Color array of bricks */
	private static final Color[] BRICK_COLOR_ARRAY = { Color.RED, Color.ORANGE, Color.YELLOW, Color.GREEN, Color.CYAN};
	
	/** Radius of the ball in pixels */
	private static final int BALL_RADIUS = 10;
	
	/** Offset of the top brick row from the top */ 
	private static final int BRICK_Y_OFFSET = 70;
	 
	/** Number of turns */
	private static final int NTURNS = 3;
	
	/** Location of paddle before move */
	private GPoint before;
	
	/** Object being dragged */
	private GObject Gobj;
	
	/** Move paddle in x direction*/
	private double dx;
	
	/** Move ball */
	private double vx, vy;
	
	/** Random generator */
	private RandomGenerator randomGen = RandomGenerator.getInstance();
	
	/** counts number of bricks */
	private int numBricks = NBRICKS_PER_ROW * NBRICK_ROWS;
	
	private GOval ball;
	
	public void run() {
		initBreakout();
		initPlay();
	}
	
	public void initBreakout() {
		Bricks();
		Paddle();
		Ball();
	}
	
	private void Bricks() {
		int startX = WIDTH/2 - NBRICKS_PER_ROW/2 * (BRICK_WIDTH + BRICK_SEP);
		for (int i = 0; i < NBRICK_ROWS; i++) {
			int startY = (i * (BRICK_HEIGHT + BRICK_SEP)) + BRICK_Y_OFFSET;
			Color brickColor = BRICK_COLOR_ARRAY[i/2];
			drawBrickRow(startX, startY, brickColor);
		}
	}
	
	private void drawBrickRow(int startX, int startY, Color brickC) {
		
		for (int i = 0; i < NBRICKS_PER_ROW; i++) {
			int x = startX + i*(BRICK_WIDTH + BRICK_SEP);
			int y = startY;
			
			GRect brick = new GRect(x, y, BRICK_WIDTH, BRICK_HEIGHT);
			brick.setFilled(true);
			brick.setColor(brickC);
			add(brick);
		}
	}

	private void Paddle() {
		drawpaddle();
		addMouseListeners();
	}

	private void drawpaddle() {
		int x = WIDTH/2 - PADDLE_WIDTH/2;
		
		GRect paddle = new GRect(x, HEIGHT - PADDLE_Y_OFFSET, PADDLE_WIDTH, PADDLE_HEIGHT);
		paddle.setFilled(true);
		paddle.setColor(Color.BLACK);
		add(paddle);
	}
		
	public void mousePressed(MouseEvent e) {
		before = new GPoint(e.getPoint());
		Gobj = getElementAt(before);
	}

	public void mouseDragged(MouseEvent e) {
		if (Gobj != null) {
			double paddleX = Gobj.getX();
			
			if (paddleX < 0) {
				dx = -paddleX;
			} else if (paddleX > WIDTH - PADDLE_WIDTH){
				dx = (WIDTH - PADDLE_WIDTH) - paddleX;
			} else {
				dx = e.getX() - before.getX();
			}
		}
		Gobj.move(dx, 0);
		before = new GPoint(e.getPoint());
	}

	private void Ball() {
		GOval ball = new GOval(WIDTH/2 - BALL_RADIUS, HEIGHT/2 - BALL_RADIUS, BALL_RADIUS, BALL_RADIUS);
		ball.setFilled(true);
		ball.setColor(Color.BLACK);
		add(ball);
	}
	
	public void initPlay() {
		ballmove();
	}
	
	private void ballmove() {
		vx = randomGen.nextDouble(1.0, 3.0);
		
		if (randomGen.nextBoolean(0.5)) vx = -vx;
		
		while (numBricks > 0) {
			moveBall();
			checkforcollision();
		}
	}

	private void moveBall() {
		ball.move(vx, vy);
	}

	private void checkforcollision() {
		// variables for the sides of the ball
		double ballLeft = ball.getX();
		double ballRight = ball.getX() + BALL_RADIUS * 2;
		double ballTop = ball.getY();
		double ballBottom = ball.getY() - BALL_RADIUS * 2;
		
		if (ballLeft <= 0 || ballRight >= WIDTH) {
			vx = -vx;
		} else if (ballTop <= 0) {
			vy = -vy;
		} else if (ballBottom >= HEIGHT) {
			remove(ball);
		}
	}
	
	private GObject getCollidingObject(double leftX, double rightX, double topY, double bottomY) {
		GObject collider = getElementAt(leftX, topY);
			if (collider == null) {
				collider = getElementAt(rightX, topY);
			}
			if (collider == null) {
				collider = getElementAt(leftX, bottomY);
			}
			if (collider == null) {
				collider = getElementAt(rightX, bottomY);
			}
			return collider;
	}
	
}