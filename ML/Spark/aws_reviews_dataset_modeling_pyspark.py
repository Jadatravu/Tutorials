import sys
sys.path.append('/home/ubuntu/spark-2.2.0-bin-hadoop2.7/python/')
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
from pyspark.sql import SQLContext
from pyspark.ml import Pipeline
from pyspark.ml.feature import VectorAssembler


# Spark configuration for 2GB(RAM)/10GB(HDD) ubuntu 16.04 VM    
conf = (SparkConf()
    .set("spark.driver.maxResultSize", "2g"))
conf.set('spark.executor.heartbeatInterval',10000000)
conf.set('spark.network.timeout',10000000)
conf.set('spark.executor.memory', '1800m')
conf.set('spark.driver.memory', '1800m')

sc = pyspark.SparkContext(conf=conf)

spark = SQLContext(sc)

#Loading dataset from a HDFS file system
#df0=spark.read.option("sep", "\t").option('header',True).csv('hdfs://192.168.50.93:9000/user/hadoop/books2/amazon_reviews_us_Wireless_v1_00.tsv')

# READING/LOADING dataset(tab seperated file) from a local file system
df0=spark.read.option("sep", "\t").option('header',True).csv('file:///home/ubuntu/datasets/amazon_reviews_us_Watches_v1_00.tsv')
#printing the schema of the spark dataframe
df0.printSchema()

#removing the null value rows
df01 = df0.filter( (col("customer_id").isNotNull()) & (col("product_id").isNotNull()) & (col("star_rating").isNotNull())& (col("helpful_votes").isNotNull())& (col("total_votes").isNotNull() ) & (col("verified_purchase").isNotNull()))

#type casting the columns properly
dfe0 = df01.withColumn("istar_rating", col("star_rating").cast("int"))
dfe1 = dfe0.withColumn("ihelpful_votes", col("helpful_votes").cast("int"))
dfe2 = dfe1.withColumn("itotal_votes", col("total_votes").cast("int"))

from pyspark.ml.feature import OneHotEncoder
from pyspark.ml.feature import OneHotEncoder, StringIndexer

#encoding string values to numericals
stage_string = StringIndexer(inputCol="verified_purchase", outputCol="class_res")

#one hot encoding
#product_id_string = StringIndexer(inputCol="product_id", outputCol="class_pid")
#oproduct_id_string = OneHotEncoder(inputCol="class_pid", outputCol="oclass_pid")

#vectorAssembler = VectorAssembler(inputCols = ['oclass_pid', 'istar_rating', 'ihelpful_votes','itotal_votes'], outputCol = 'features')
vectorAssembler = VectorAssembler(inputCols = ['istar_rating', 'ihelpful_votes','itotal_votes'], outputCol = 'features')

#model building
from pyspark.ml.classification import RandomForestClassifier
rf = RandomForestClassifier(labelCol="class_res", featuresCol="features", numTrees=10)

from pyspark.ml.classification import GBTClassifier
gbt = GBTClassifier(labelCol="class_res", featuresCol="features", maxIter=10)

#ppl = Pipeline(stages=[stage_string, product_id_string,oproduct_id_string,vectorAssembler,gbt])
#ppl = Pipeline(stages=[stage_string, product_id_string,oproduct_id_string,vectorAssembler,rf])
ppl = Pipeline(stages=[stage_string,vectorAssembler,rf])

#test train split
(dfe2_train,dfe2_test) = dfe2.randomSplit([0.7,0.3])
#Model Training
model = ppl.fit(dfe2_train)

#Saving the trained model
model.write().overwrite().save("./aws_rw_watches_model")

class_res_pred = model.transform(dfe2_test)
#class_res_pred.select("prediction").coalesce(1).write.format("text").option("header", "false").mode("append").save("output.txt")
class_res_pred.select("prediction").write.save("output.txt")

"""
from pyspark.mllib.evaluation import BinaryClassificationMetrics
predictionAndLabels = dfe2_test.rdd.map(lambda lp: (float(model.predict(lp.features)), lp.class_res))

print(dir(predictionAndLabels))
#predictionAndLabels.to_csv("prediction_labels.csv")
#predictionAndLabels.saveAsTextFile("prediction_labels.csv")
predictionAndLabels.coalesce(1).write.format("text").option("header", "false").mode("append").save("output.txt")

metrics = BinaryClassificationMetrics(predictionAndLabels)

# Area under precision-recall curve
print("Area under PR = %s" % metrics.areaUnderPR)

# Area under ROC curve
print("Area under ROC = %s" % metrics.areaUnderROC)

"""


