def check_palindrome(num):
    new_num = str(num)[::-1]
    return  new_num == str(num)

def get_binary_num(num):
    return "{0:b}".format(num)

def bin_palindrome(num):
    bin_num = get_binary_num(num)
    return check_palindrome(bin_num)

def main():
    """
        https://projecteuler.net/problem=36
    """
    count = 1
    while True:
       if check_palindrome(count) and bin_palindrome(count):
            print count, " ", get_binary_num(count) 
       count += 1
       if count > 1000000:
           break
       

if __name__ == "__main__": 
   main()
