package cs106;

import acm.graphics.*;
import acm.program.*;

public class ACM_Diagram extends GraphicsProgram {
	// constants
	public static final int boxWidth = 120;
	public static final int boxHeight = 50;
	public static final int boxSpacing = 20;
	
//	Java Applet Windows size setting
	public void init() { 
		this.setSize(600, 300);
	}
	
	public void run() {
		// variables
		double centerX = getWidth()/2;
		double centerY = getHeight()/2;
		
		// program box
		GRect ProgramB = new GRect(centerX - boxWidth/2, centerY - (3 *boxHeight)/2 - boxSpacing*2, boxWidth, boxHeight);
		
		// drawing the subclasses
		GRect GraphicsProgramB = new GRect(centerX - 1.5*boxWidth - boxSpacing, centerY - boxHeight/2, boxWidth, boxHeight);
		GRect ConsoleProgramB = new GRect(centerX - boxWidth/2, centerY - boxHeight/2, boxWidth, boxHeight);
		GRect DialogProgramB = new GRect(centerX + boxWidth/2 + boxSpacing, centerY - boxHeight/2, boxWidth, boxHeight);
		
		// lines
		GLine P_CP = new GLine(centerX, centerY - boxHeight/2 - 2*boxSpacing, centerX, centerY - boxHeight/2);
		GLine P_GP = new GLine(centerX, centerY - boxHeight/2 - 2*boxSpacing, centerX - boxWidth - boxSpacing, centerY - boxHeight/2);
		GLine P_DP = new GLine(centerX, centerY - boxHeight/2 - 2*boxSpacing, centerX + boxWidth + boxSpacing, centerY - boxHeight/2);
		
		GLine test = new GLine(centerX, centerY, 50, 50);
		
		// program label
		
		GLabel dummy = new GLabel("Program");
		
		double labelWIDTH = dummy.getWidth();
		double labelASCENT = dummy.getAscent();
		
		GLabel programL = new GLabel("Program", centerX - dummy.getWidth()/2, centerY - boxHeight - 2 * boxSpacing + labelASCENT/2);
		
		// graphics program label
		
		GLabel dummy2 = new GLabel("GraphicsProgram");
		
		double labelWIDTH2 = dummy2.getWidth();
		double labelASCENT2 = dummy2.getAscent();
		
		
		GLabel GPL = new GLabel("GraphicsProgram", centerX - boxWidth - boxSpacing - labelWIDTH2/2, centerY + labelASCENT2/2);
		
		// console program label
		
		GLabel dummy3 = new GLabel("ConsoleProgram");
				
		double labelWIDTH3 = dummy3.getWidth();
		double labelASCENT3 = dummy3.getAscent();
				
				
		GLabel CPL = new GLabel("ConsoleProgram", centerX - labelWIDTH3/2, centerY + labelASCENT3/2);
		
		// dialog program label
		
		GLabel dummy4 = new GLabel("DialogProgram");
						
		double labelWIDTH4= dummy4.getWidth();
		double labelASCENT4 = dummy4.getAscent();
						
						
		GLabel DPL = new GLabel("DialogProgram", centerX + boxWidth + boxSpacing - labelWIDTH4/2, centerY + labelASCENT4/2);
				
		
		
		// add to canvas
		add(ProgramB);
		add(GraphicsProgramB);
		add(ConsoleProgramB);
		add(DialogProgramB);
		add(P_CP);
		add(P_GP);
		add(P_DP);
		add(programL);
		add(GPL);
		add(CPL);
		add(DPL);
	}
}
