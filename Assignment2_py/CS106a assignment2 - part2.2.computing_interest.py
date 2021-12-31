# compute how much interest their bank account will accrue over time. The program starts by asking the user for an initial account balance, which is entered as a float (you can assume a positive realvalue is entered). The program then asks the user for a starting year and month as well as an ending year and month, all entered as integers. The program then asks the user for a monthly interest rate. For example, a 2% interest rate would be entered by the user as the value 0.02.


def main():
  italics = '\033[3m'
  plain = '\033[0m'

  init_bal = input(plain+"Initial balance: "+italics) 
  start_yr = input(plain+"Start year: "+italics)
  start_mon = input(plain+"Start month: "+italics)
  end_yr = input(plain+"End year: "+italics)
  end_mon = input(plain+"End month: "+italics)

  start_yrmon=int(start_yr)*12+int(start_mon)
  end_yrmon=int(end_yr)*12+int(end_mon)

  if ( start_yrmon>=end_yrmon):
    print(plain+"Starting date needs to be before the ending date.")

  ir = 0.02;
  while (ir!=0):
    ir=float(input(plain+"Interest rate (0 to quit):"+italics))
    if (ir!=0):
      balance=float(init_bal)
      print(plain+"Year ",start_yr,", month ",start_mon," balance: ",balance)
      for x in range((start_yrmon+1), (end_yrmon+1)):
        balance = balance*(1+ir)
        if ((x % 12)==0):
         print("Year ",int(x/12),", month ",12 ," balance: ",balance)
        else:
         print("Year ",int(x/12),", month ",(x % 12)," balance: ",balance)

if __name__ == "__main__":
 main()