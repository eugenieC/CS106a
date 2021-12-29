"""
This program is just meant to test your understanding
of variables, control flow, and functions.
"""
def mystery():
 x = 3
 x = 5 - x / 2
 print(x)

def main():
 x = 1
 while x < 20:
  print(f"x = {x}")
  mystery()
  x *= 2
 print(f"x = {x}")
 
if __name__ == "__main__":
 main()