import sys
#sys.path.append('/home/ubuntu/packages/spark-2.2.0-bin-hadoop2.7/python/')
sys.path.append('/home/ubuntu/spark-2.2.0-bin-hadoop2.7/python/')
import pyspark
from pyspark import SparkConf
from pyspark.sql import SparkSession
import re
import unicodedata

def search_string(doc,key_text):
    #print type(doc["review_headline"])
    try:
        #d_str = unicodedata.normalize('NFKD',doc["review_headline"])
        d_str = unicodedata.normalize('NFKD',doc["review_body"])
        ob=re.findall(key_text,d_str)
        ret_val = len(ob)
    except Exception as e:
        ret_val = 0
    return (key_text,ret_val)
   
def agg_func(accum,n):
    return accum+n
    
conf = (SparkConf()
    .set("spark.driver.maxResultSize", "2g"))
conf.set('spark.executor.heartbeatInterval',10000000)
conf.set('spark.network.timeout',10000000)
conf.set('spark.executor.memory', '1800m')
conf.set('spark.driver.memory', '1800m')

sc = pyspark.SparkContext(conf=conf)
from pyspark.sql import SQLContext

spark = SQLContext(sc)

#Loading dataset from a HDFS file system
#df0=spark.read.option("sep", "\t").option('header',True).csv('hdfs://192.168.50.93:9000/user/hadoop/books2/amazon_reviews_us_Wireless_v1_00.tsv')

# READING/LOADING dataset(tab seperated file) from a local file system
df0=spark.read.option("sep", "\t").option('header',True).csv('file:///home/ubuntu/datasets/amazon_reviews_us_Watches_v1_00.tsv')

#printing the schema of the spark dataframe
df0.printSchema()


#review_headline_df = df0.select("review_headline")
review_headline_df = df0.select("review_body")
review_headline_df.printSchema()

key_text = "good"

new_rdd = review_headline_df.rdd.map(lambda x:search_string(x,key_text))

print new_rdd.take(5)

o_rdd=new_rdd.reduceByKey(lambda x,y:x+y)

print o_rdd.take(5)

key_text = "bad"

new_rdd_1 = review_headline_df.rdd.map(lambda x:search_string(x,key_text))
print new_rdd_1.take(5)

o_rdd_1=new_rdd_1.reduceByKey(lambda x,y:x+y)
print o_rdd_1.take(5)



