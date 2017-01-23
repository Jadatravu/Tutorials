def main():
    """ 
       This is the solution for the problem 31
       https://projecteuler.net/problem=31
    """ 
    ma=[1,2,4,10,20,40,100,200]
    count = 0
    for a in range(ma[0]):
        for b in range(ma[1]):
           for c in range(ma[2]):
               for d in range(ma[3]):
                   for e in range(ma[4]):
                        for f in range(ma[5]):
                            for g in range(ma[6]):
                                sum = a*200+b*100+c*50+d*20+e*10+f*2+g*1 
                                if sum == 200:
                                   count = count + 1
                                   print  str("count ")+ str(count) + str(" ")+ str(a) + str(" 200p ") + str(b) + str(" 100p ") + str(c) + str(" 50p ") + str(d) + str(" 20p ")+ str(e) + str(" 10p ") + str(f) + str(" 2p ") + str(g) + str(" 1p ")

if __name__ == '__main__':
   main()
