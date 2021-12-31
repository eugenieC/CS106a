package cs106;

import acm.program.*;

public class Hailstone extends ConsoleProgram {
	
	// variables
	int k;
	int numSteps = 0;
	
	public void run() {
		int n = readInt("Enter a number: ");

		while (true) {
			if (n == 1) {
				break;
			}
			
			if (n % 2 == 1) {
				k = 3*n + 1;
				println(n + " is odd, so I make 3n+1: " + k);
				n = k;
				numSteps ++;
			}
			
			if (n % 2 == 0) {
				k = n/2;
				println(n + " is even, so I take half: " + k);
				n = k;
				numSteps ++;
			}
		}
		println("The process took " + numSteps + " to reach 1");
	}
}
