import sys
#sys.path.append('/home/ubuntu/packages/spark-2.2.0-bin-hadoop2.7/python/')
sys.path.append('/home/hadoop/spark/python/')
import pyspark
from pyspark import SparkConf
from pyspark.sql.types import IntegerType, StringType,FloatType, ArrayType
from pyspark.sql.functions import udf,array,struct,col
from pyspark.sql import SparkSession
import math
import re
import datetime
from numpy import array

from pyspark.ml.feature import HashingTF, IDF, Tokenizer
from pyspark.ml.classification import NaiveBayes
from pyspark.ml.feature import OneHotEncoder
from pyspark.ml.feature import OneHotEncoder, StringIndexer
from pyspark.ml import Pipeline
from pyspark.ml.feature import HashingTF, IDF, Tokenizer
from pyspark.sql import SQLContext


# SPARK CONFIGURATION    
conf = (SparkConf()
    .set("spark.driver.maxResultSize", "2g"))
conf.set('spark.executor.memory', '2100m')
conf.set('spark.worker.cleanup.enabled',True)
conf.set('spark.worker.cleanup.interval',30)
conf.set('spark.yarn.executor.memoryOverhead','400m')
#spark = SparkSession.builder.appName('ml-bank').conf(conf=conf).getOrCreate()
#spark = SparkSession.conf(conf=conf).builder.appName('ml-bank').getOrCreate()

#SQL CONTEXT CREATION
sc = pyspark.SparkContext(conf=conf)
spark = SQLContext(sc)

#LOADING DATA FROM HDFS TO SPARK DATAFRAME
df0=spark.read.option("sep", "\t").option('header',True).csv('hdfs://192.168.50.93:9000/user/hadoop/books2/amazon_reviews_us_Wireless_v1_00.tsv')
df0.printSchema()

#FILTERING FOR EMPTY VALUES
df01 = df0.filter((col("review_body").isNotNull()) & (col("verified_purchase").isNotNull()))

#ENCODING LABEL
stage_string = StringIndexer(inputCol="verified_purchase", outputCol="class_res")
ppl = Pipeline(stages=[stage_string])
df1 = ppl.fit(df01).transform(df01)

#CREATING TF_IDF
tokenizer = Tokenizer(inputCol="review_body", outputCol="words")
wordsData = tokenizer.transform(df1)
hashingTF = HashingTF(inputCol="words", outputCol="rawFeatures", numFeatures=20)
featurizedData = hashingTF.transform(wordsData)
idf = IDF(inputCol="rawFeatures", outputCol="features")
idfModel = idf.fit(featurizedData)
rescaledData = idfModel.transform(featurizedData)

#NAIVEBAYES 
nb = NaiveBayes(featuresCol="features", labelCol="class_res")

#Model training
model = nb.fit(rescaledData)

#Model Saving
model.write().overwrite().save("./NB_model")

#Predictions
pred = model.transform(rescaledData)

#Disploying top 5 prediction values
pred.select('prediction').show(5)

