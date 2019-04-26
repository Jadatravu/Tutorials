def get_tria_list(num):
    tria_list = [1]
    i = 0
    n = 0
    while n < num:
        i += 1
        n = tria_list[-1]+i
        if n > num:
            break
        tria_list.append(n)
    return tria_list

def get_num_of_str(s2):
    s1=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    s2_list=list(s2)
    val = 0
    for i2 in s2_list:
        val += (s1.index(i2)+1)
    return val

def main():
    """
       This is the solution for the problem 42
       https://projecteuler.net/problem=42
    """
    l1=[]
    with open("p042_words.txt",'r') as op:
        lines=op.readlines()    
        l1 = lines[0].split(',')
    
    val_list=[]
    for ind in range(len(l1)):
        val_list.append(get_num_of_str(l1[ind].strip('\"')))

    num= max(val_list)
    tria_list = get_tria_list(num)

    tria_str_list = []
    for ind in range(len(l1)):
        val = get_num_of_str(l1[ind].strip('\"'))
        if val in tria_list:
            tria_str_list.append(l1[ind].strip('\"'))

    print(tria_str_list)
    print(len(tria_str_list))

if __name__ == '__main__':
    main()
