def main():
    """
       This is the solution for the problem 13
       https://projecteuler.net/problem=13
    """
    with open("file.txt",'r+') as fo:
         line = fo.readline()
         num = 0
         sum = long(num) 
         while line :
            sline= line[40:50]
            sum = sum + long(sline)
            line = fo.readline()
    print str(sum)[2:12]

if __name__ == '__main__':
   main()
            
