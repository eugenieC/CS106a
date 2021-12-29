#asks the user for their weight (you can assume is a real-valued input is given by the user) and prints out their weight on the moon. If the user enters a negative value (yes,they’re being mean and trying to break your program), you should just print out that weights can’t be negative. 


def main():
  moon_weight_ratio=0.165
  earth_weight=input("Enter your weight: ")
  earth_weight=float(earth_weight)
  if (earth_weight >= 0):
    moon_weight=earth_weight*moon_weight_ratio
    print("Your weight on the moon is ",moon_weight)
  else:
    print("Sorry, you can't have a negative weight.")

if __name__ == "__main__":
 main()