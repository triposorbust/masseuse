#!/usr/bin/env python

import datetime
import numpy as np

def standard(n):
    return np.random.normal(0,1,n)

def main(number, length, density=0.05):
    offset = 0
    while number > 0:
        if np.random.random() <= density:
            date = datetime.date.today() + datetime.timedelta(offset)
            data = standard(length)
            number -= 1

            print("{0}\t{1}".format(date.strftime("%Y-%m-%d"),
                                    "\t".join(map(str, data))))
        offset += 1

if __name__ == "__main__":
    main(100,1,0.35)
