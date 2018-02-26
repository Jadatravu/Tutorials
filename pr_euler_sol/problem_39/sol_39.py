def get_triangular_dict_list(num):
    tria_list =[]
    for a in range(1,num+1):
        for b in range(1,num+1):
            if (a+b) > num:
               break
            for c in range(1,num+1):
                 if (a+b+c) > num:
                     break
                 if (a+b+c) != num:
                     continue
                 nl =[]
                 if (a**2 + b**2) == c**2:
                    nl= [a,b,c]
                 elif (b**2 + c**2) == a**2:
                    nl= [a,b,c]
                 elif (c**2 + a**2) == b**2:
                    nl= [a,b,c]
                 if len(nl) > 0:
                    nl.sort()
                    if nl not in tria_list:
                        if (a+b+c) == num:
                           tria_list.append(nl)
    return tria_list 
     
def main():
    """
       https://projecteuler.net/problem=39
    """
    num_tria_count_dict = {}
    count = 0
    for num in range(1,1001):
        num_tria_count_dict[num] = get_triangular_dict_list(num)
        n_count = len(num_tria_count_dict[num])
        if n_count > count:
             count = n_count
             print num, " => ", num_tria_count_dict[num], " count => ", len(num_tria_count_dict[num])

if __name__ == "__main__":
    main()
