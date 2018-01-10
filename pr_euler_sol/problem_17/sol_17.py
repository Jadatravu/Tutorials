import sys

ones={0:'',1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}

tens={10:"ten",20:"twenty",30:"thirty",40:"fourty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety"}

eve={11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen"}

def get_one(n):
    return ones[n]

def get_ten(n):
    if n in tens.keys():
       return  tens[n]
    elif n > 10 and n < 20:
       return eve[n]
    else:
       ten = n/10
       one = n%10
       return "%s %s"%(tens[ten*10],ones[one])

def get_hundred(n):
    hun = n/100
    ten = n%100
    ten_str = ''
    if ten >= 10:
       ten_str = get_ten(ten)
    else:
        o_ne = ten%10
        ten_str = "%s"%(ones[o_ne])
    return "%s hundred and %s"%(ones[hun],ten_str)


def get_str(num):
    if num < 10:
       return get_one(num)
    elif num <100:
       return get_ten(num)
    elif num <1000:
       return get_hundred(num)

def cal_str_len(num_str):
    num_str_list = num_str.split(' ')
    count = 0
    for a_str in num_str_list:
        count = count + len(a_str)
    return count

def cal_list_len(num_str):
    return reduce(lambda x,y:x+y,map(len, num_str.split(' ')))
       

def approach_2():
    count = 0
    for num in range(1,999):
        num_str = get_str(num)
        count = count + cal_list_len(num_str)
    print count

def approach_1():
    print reduce(lambda x,y:x+y, map(cal_list_len, map(get_str, range(1,999))))

def main():
    """
       https://projecteuler.net/problem=17
    """
    approach_1()
    approach_2()

if __name__ == '__main__':
    main()
