def main():
    multiple_list = []
    sum = 0
    for a in range(0,1000):
        if a%3 == 0 or a%5 ==0:
           multiple_list.append(a)
           sum = sum + a
    print multiple_list
    print sum

if __name__ == '__main__':
   main()
    
