from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from unpivot_transformations.config.ConfigStore import *
from unpivot_transformations.udfs.UDFs import *

def quarterly_sales_data(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("id", StringType(), True), StructField("Year", StringType(), True), StructField("Q1", StringType(), True), StructField("Q2", StringType(), True), StructField("Q3", StringType(), True), StructField("Q4", StringType(), True)
        ])
        )\
        .option("header", True)\
        .option("sep", ",")\
        .csv("dbfs:/Users/ashish/twaice/q_sales.csv")
