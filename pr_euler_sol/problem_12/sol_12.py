def get_factor(num):
    return filter(lambda x: num % x ==0 ,range(1,num-1))

def main():
    """
       Problem : https://projecteuler.net/problem=12
    """
    triangular_list =[1]
    count = 1
    factors_dict ={}
    while True:
         new_val = count+triangular_list[count-1]
         triangular_list.append(new_val)
         count = count+1
         factors_dict[new_val] = get_factor(new_val)
         if len(factors_dict[new_val]) == 500:
               print new_val
               print factors_dict[new_val]
               break

if __name__ == '__main__':
    main()
