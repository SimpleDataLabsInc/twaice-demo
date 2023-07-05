from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from timestamp_conversion_example.config.ConfigStore import *
from timestamp_conversion_example.udfs.UDFs import *

def SchemaTransform_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0\
        .withColumn("created_at_ts", to_timestamp(col("created_at"), "MM-dd-yy HH:mm:ss"))\
        .withColumn("created_at_ts2", date_format(col("created_at_ts"), "MM-dd-yyyy HH:mm:ss SSS"))\
        .withColumn("created_at_ts3", date_format(col("created_at_ts"), "yyyy-mm-dd HH->mm->ss SSS"))\
        .drop("created_at")
