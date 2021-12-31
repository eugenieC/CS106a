package cs106;

import java.awt.Color;

import acm.graphics.*;
import acm.program.*;

public class Target extends GraphicsProgram {
	public void run() {
		// convert inches to pixels
		double inch = 72;
		
		// define variables: radii
		double outerRad = inch;
		double midRad = 0.65 * inch;
		double innerRad = 0.3 * inch;
		
		// centering
		double centerX = (getWidth())/(2);
		double centerY = (getHeight())/(2);
		
		// inner circle
		GOval innerCirc = new GOval(centerX - innerRad/2, centerY - innerRad/2, innerRad, innerRad);
		innerCirc.setFilled(true);
		innerCirc.setFillColor(Color.RED);
		
		// middle circle
		GOval midCirc = new GOval(centerX - midRad/2, centerY - midRad/2, midRad, midRad);
		midCirc.setFilled(true);
		midCirc.setFillColor(Color.WHITE);
		
		// outer circle
		GOval outerCirc = new GOval(centerX - outerRad/2, centerY - outerRad/2, outerRad, outerRad);
		outerCirc.setFilled(true);
		outerCirc.setFillColor(Color.RED);
		
		// add to canvas
		add(outerCirc);
		add(midCirc);
		add(innerCirc);
		
	}
	
}
