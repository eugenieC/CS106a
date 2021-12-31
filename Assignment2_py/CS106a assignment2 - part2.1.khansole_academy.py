# generate simple addition problems that involve adding two 2-digit integers (i.e., the numbers 10 through 99). The user should be asked for an answer to each problem. Your program should determine if the answer was correct or not, and give the user an appropriate message to let them know. Your program should keep giving the user problems until the user has gotten 3 problems correct in a row

import random

def main():
  italics = '\033[3m'
  plain = '\033[0m'

  MIN_RANDOM=10
  MAX_RANDOM=99
  num_in_a_row=0

  while num_in_a_row < 3:
    a = random.randint(MIN_RANDOM,MAX_RANDOM)
    b = random.randint(MIN_RANDOM,MAX_RANDOM)
    print("What is ",a,"+ ",b,"?")
    c = a+b
    ans = input(plain+"Your answer: "+italics) 
    ans=int(ans)
    if (c==ans):
      num_in_a_row += 1
      print(plain+"Correct! You've gotten ",num_in_a_row," correct in a row."+plain)
    else:
      print(plain+"Incorrect. The expected answer is ",c)
      num_in_a_row=0

  print("Congratulations! You mastered addition.")
if __name__ == "__main__":
 main()