def main():
    """
       https://projecteuler.net/problem=20
    """
    print reduce(lambda x,y:int(y)+int(x),list(str(reduce(lambda x,y:x*y,range(1,100)))))

if __name__ == '__main__':
    main()
