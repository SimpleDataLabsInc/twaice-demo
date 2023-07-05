from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from dataanalysislookup.config.ConfigStore import *
from dataanalysislookup.udfs.UDFs import *

def byModel(spark: SparkSession, laptop_data: DataFrame) -> DataFrame:
    df1 = laptop_data.groupBy(col("`Model Number`").alias("model"))

    return df1.agg(count(lit(1)).alias("count"))
