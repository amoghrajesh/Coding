
from pyspark.sql import SparkSession
  
spark = SparkSession.builder.appName("DataFrame").getOrCreate()
  
df = spark.read.text("file:///app/mount/Folder-1/Folder-2/input.txt")
  
df.selectExpr("split(value, ' ') as\
Text_Data_In_Rows_Using_Text").show(4,False)