from math import factorial

def check_number(num):
    if num <= 99 and num > 9:
       one_div = num%10
       ten_div = num/10
       result = factorial(one_div) + factorial(ten_div)
    elif num >99 and num <=999:
       hun_rem = num%100
       hun_div = num/100
       ten_div = hun_rem/10
       one_div = hun_rem%10
       result = factorial(one_div) + factorial(ten_div) + factorial(hun_div)
    elif num >999 and num <=9999:
       th_div = num/1000
       th_rem = num%1000
       hun_rem = th_rem%100
       hun_div = th_rem/100
       ten_div = hun_rem/10
       one_div = hun_rem%10
       result = factorial(one_div) + factorial(ten_div) + factorial(hun_div) + factorial(th_div)
    elif num >9999 and num <=99999:
       tth_div = num/10000
       tth_rem = num%10000
       th_div = tth_rem/1000
       th_rem = tth_rem%1000
       hun_rem = th_rem%100
       hun_div = th_rem/100
       ten_div = hun_rem/10
       one_div = hun_rem%10
       result = factorial(one_div) + factorial(ten_div) + factorial(hun_div) + factorial(th_div)+factorial(tth_div)
    return result == num

def main():
    """
       https://projecteuler.net/problem=34
    """
    print reduce(lambda x,y: x+y, filter(check_number, range(10,100000)))
   
if __name__ == '__main__':
     main() 
