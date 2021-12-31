# prints 10 random integers (each random integer should have a value between 0 and 100, inclusive).

import random

def main():
  NUM_RANDOM=10
  MIN_RANDOM=0
  MAX_RANDOM=100

  for x in range(0,NUM_RANDOM):
    random_numbers=random.randint(MIN_RANDOM,MAX_RANDOM)
    print(random_numbers)

if __name__ == "__main__":
 main()