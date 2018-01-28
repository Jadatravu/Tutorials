def main(start, end):
    result_list = []
    for a in range(start,end+1):
        for b in range(start,end+1):
           result_list.append(pow(a,b))
    result_list =list(set(result_list))
    result_list.sort()
    #print result_list
    print len(result_list)
          
def main1(start,end):
    res_list=list(set([pow(a,b) for a in range(start,end+1) for b in range(start,end+1)]))
    #print res_list
    print len(res_list)

if __name__ == '__main__':
   #approach 1 with list append
   main(2,100)
   #approach 2 with list comprehension
   main1(2,100)

