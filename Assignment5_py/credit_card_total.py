"""
File: credit_card_total.py
--------------------------
This program totals up a credit card bill based on
how much was spent at each store on the bill.
"""

import re
from collections import defaultdict

INPUT_FILE = 'Assignment5/bill2.txt'


def main():
    d =  {}

    with open(INPUT_FILE) as f:
        for line in f:
            s = re.split(r'\[|\]|\$', line)  
            # print(s)
            if s[1] in d:
                d[s[1]].append(int(s[3]))
            else:
                d[s[1]] = [int(s[3])]
        
    # print(d)

    totals={}
    for k, v in d.items():
        totals[k]=0
        for j in range(len(v)):
            totals[k] += v[j]
        print(k,": $",totals[k],sep = '')
    
    
# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()


