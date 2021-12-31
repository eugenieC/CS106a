package cs106;

import acm.program.*;

public class Min_Max extends ConsoleProgram {
	private static final int SENTINEL = 0;
	
	public void run() {
		println("This program finds the largest and smallest numbers.");
		
		// defining min, max, and user value
		int min = 0;
		int max = 0;
		
		while (true) {
			int userValue = readInt("? ");
			// stopping if sentinel is reached
			
			if (userValue == SENTINEL) {
				break;
			}
		
			if (userValue > max) {
				max = userValue;
			}
			if (userValue < min) {
				min = userValue;
			}
		
		}
	println("smallest: " + min);
	println("largest: " + max);
	}
}
