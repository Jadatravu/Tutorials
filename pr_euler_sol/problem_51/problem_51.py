def check_prime(num):
    for i1 in range(2,int(num/2)):
        if num%i1 == 0:
            return False
    return True

def get_str_counts(n_str):
    sw_count = {}
    ss1 = set(n_str)
    for w in ss1:
        sw_count[w] = 0
    for w in ss1:
        for w1 in n_str:
            if w1 == w:
                sw_count[w]+=1
    ret_dict = {}
    for k1 in sw_count.keys():
        if sw_count[k1] > 1:
            ret_dict[k1] = sw_count[k1]
    return ret_dict

def main():
    """
       This is the solution for the problem 51
       https://projecteuler.net/problem=51
    """
    for num in range(10000001,100000000,2):
        if check_prime(num):
            num_str = str(num)
            if len(num_str) > len(set(num_str)):
                str_counts = get_str_counts(num_str)
                if len(str_counts.keys()) == 1:
                    o1= list(str_counts.keys())
                    print(str_counts)
                    if o1[0] != '0':
                        print (num)
                        break
if __name__ == "__main__":
    main()
