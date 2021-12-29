# reads two real numbers from the user and prints the first number minus the second number.

def main():
  print("This program subtracts one number from another.")
  a=input("Enter first number: ")
  b=input("Enter second number: ")
  c = float(a) - float(b)
  print("The result is ",c)

if __name__ == "__main__":
 main()