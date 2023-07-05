from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from timestamp_conversion_example.config.ConfigStore import *
from timestamp_conversion_example.udfs.UDFs import *

def user_data(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("userid", StringType(), True), StructField("name", StringType(), True), StructField("created_at", StringType(), True), StructField("email", StringType(), True), StructField("region", StringType(), True)
        ])
        )\
        .option("header", True)\
        .option("inferSchema", True)\
        .option("sep", ",")\
        .csv("dbfs:/Users/ashish/twaice/timestamp_conversion_example.csv")
