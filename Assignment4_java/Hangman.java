package cs106;

import acm.graphics.*;
import acm.util.*;
import acm.program.*;

import java.awt.*;
import java.util.*;

public class Hangman extends ConsoleProgram {
	// adjusting screen size
	public void init() { 
		this.setSize(600, 600);
	}
	
	// instance of hangman lexicon
    private HangmanLexicon lexicon;
    
    // our word for that round
    private String word;
    
    // random generator
    private RandomGenerator rgen = RandomGenerator.getInstance();
    
    // number of guesses
    private static int numberofGuesses = 8;
    
    // string for word to guess
    private String string = "";

    // define guess globally
    private String guess;
    
	public void run() {
	
		// Create a new HangmanLexicon 
    	lexicon = new HangmanLexicon();  	
    	
    	/* Loop to play repeatedly */
    	int wordCount = lexicon.getWordCount() - 1;
    	word = lexicon.getWord(rgen.nextInt(0, wordCount));
		
		// THE GAME (dun, dun, dun!)
    	
    	println("Welcome to Hangman!");
		
    	playRound();
    	
    	if (numberofGuesses > 0) {
    		win();
    	} else {
    		lose();
    	}
		
	}

	private void playRound() {
		
		// print out the "---"
		string = "";
		
		for (int i = 0; i < word.length(); i++) {
			string = string + "-";
		}
		
		while (numberofGuesses > 0 && !wordGuessed()) {
			println("The word now looks like this: " + string);
			println("You have " + numberofGuesses + " guesses left.");
			String guess = readLine("Your guess: ");
			
			if (!error(guess)) {
				char guessChar = guess.charAt(0);
				guessChar = Character.toUpperCase(guessChar);
				if (isInWord(guessChar)) {
					println("That guess is correct.");
					string = newstring(guessChar, string);
				} else {
					println("There are no " + guess + "'s in the word.");
					numberofGuesses--;
				}
			} else {
				println("That is not a valid input. Try again.");
			}
		}
		
	}
	
	private boolean error(String guess) {
		if (guess.length() > 0) {
			return false;
		} else {
			return true;
		}
	}
	
	private boolean isInWord(char ch) {
		for (int i = 0; i < word.length(); i++) {
			char wordChar = word.charAt(i);
			if (ch == wordChar) {
				return true;
			}
		}
		
		return false;
	}
	
	private String newstring(char ch, String string) {
		
		String tempstring = "";
		
		for (int i = 0; i < word.length(); i++) {
			char wordChar = word.charAt(i);
			char stringChar = string.charAt(i);
			
			if (stringChar != '-') {
				tempstring += stringChar;
			} else {
					if (ch == wordChar) {
						tempstring = tempstring + ch;
					} else {
						tempstring = tempstring + "-";
					}
				}
			}

		return tempstring;
	}
	
	private boolean wordGuessed() {
		int index = string.indexOf('-');
		if (index == -1) {
			return true;
		} else {
			return false;
		}
	}
	
	private void win() {
		println("The word was: " + word);
		println("You win.");
	}
	
	private void lose() {
		println("You're completely hung.");
		println("The word was: " + word);
		println("You lose.");
	}
	
}