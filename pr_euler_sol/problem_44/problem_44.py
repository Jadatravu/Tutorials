def get_pent_numbers(num):
    pent_list = []
    for i in range(1,num):
        pent_list.append(i*int(((3*i)-1)/2))
    return pent_list

def main():
    n = 10000 # first 10000 pent numbers
    pent_list = get_pent_numbers(n)
    res_list = {}
    print(pent_list)
   
    for c1 in range(n-1):
        for c2 in range(c1+1, n-1):
            a1 = pent_list[c1] + pent_list[c2]
            s1 = pent_list[c2] - pent_list[c1]
            if (a1 in pent_list) and (s1 in pent_list):                
                res_list[s1]=[pent_list[c1],pent_list[c2]]
    ke_ys = res_list.keys()
    #ke_ys.sort()
    print (ke_ys)
    print (res_list)

if __name__ == '__main__':
    main()
