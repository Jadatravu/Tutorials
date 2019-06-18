def get_min_max(digit_count):
    sum = 1
    for i in range(digit_count-1):
        sum = sum*10
    m_in = sum
    m_ax = sum*10-1
    return (m_in,m_ax)

def main():
    """
       This is the solution for the problem 63
       https://projecteuler.net/problem=63
    """
    for ic in range(1,10):
        m_in,m_ax = get_min_max(ic)
        for i1 in range(m_in,m_ax):
            i2 = 2
            while True:
                val = i2**ic
                if val > i1:
                    break
                elif val == i1:
                    print("%d, %d => %d"%(ic, i2, i1))
                i2+=1
            


if __name__ == "__main__":
    main()

        
