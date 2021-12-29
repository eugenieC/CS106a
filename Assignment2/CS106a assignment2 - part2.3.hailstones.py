# Pick some positive integer and call it n.
# If n is even, divide it by two.
# If n is odd, multiply it by three and add one.
# Continue this process until n is equal to one.


def main():
  italics = '\033[3m'
  plain = '\033[0m'

  init_value = input(plain+"Enter a number: "+italics) 
  print (plain, end ="")

  value=int(init_value)
  count=0

  while (value!=1):
    count += 1
    if ((value % 2)==1):
      print(value,"is odd, so I make 3n + 1:", (3*value+1))
      value=3*value+1
    else:
      print(value,"is even, so I take half:", int(value/2))
      value=int(value/2)

  print("The process took ",count,"steps to reach 1")

if __name__ == "__main__":
 main()