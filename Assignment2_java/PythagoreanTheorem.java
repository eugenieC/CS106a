package cs106;

import acm.program.*;

public class PythagoreanTheorem extends ConsoleProgram {
	public void run() {
		println("Enter values to compute Pythagorean theorem.");
		int a = readInt("a: ");
		int b = readInt("b: ");
		double c = Math.sqrt((double) a * (double) a + (double) b * (double) b);
		println("c = " + c);
	}
}