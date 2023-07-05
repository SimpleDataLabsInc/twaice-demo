from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from timestamp_conversion_example.config.ConfigStore import *
from timestamp_conversion_example.udfs.UDFs import *

def user_final_data(spark: SparkSession, convert_timestamp: DataFrame):
    convert_timestamp.write\
        .option("header", True)\
        .option("sep", ",")\
        .mode("overwrite")\
        .option("separator", ",")\
        .option("header", True)\
        .csv("dbfs:/Users/ashish/twaice/output/user_cleaned")
