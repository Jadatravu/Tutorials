import json
import sys

alpha = str('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
def get_value(xa):
    return list(alpha).index(xa)+1

def cal_values(names_dict, key):
    return reduce(lambda x,y:x+y, map(get_value, list(names_dict[key])))

def get_name_dict():
    names_dict={} 
    with open("p022_names.txt",'r') as fo: 
         lines = fo.readlines()
         l_ines = lines[0].split(',')
         l_ines=sorted(l_ines)
         count = 0
         for name in l_ines:
            names_dict[count] = name.strip('\"')
            count =count + 1
    return names_dict


def main():
    """
        https://projecteuler.net/problem=22
    """
    try:
       names_dict = get_name_dict()
    except IOError as e:
        print e
        print "Down load names.txt file from path https://projecteuler.net/project/resources/p022_names.txt"
        sys.exit()
    except Exception as e:
        print e
        sys.exit()
    #print names_dict
    total_value = 0
    for key,value in names_dict.iteritems():
        c_value = cal_values(names_dict,key)
        total_value = total_value + c_value*(key+1)
    print total_value 

if __name__ == "__main__":
    main()
