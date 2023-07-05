from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from unpivot_transformations.config.ConfigStore import *
from unpivot_transformations.udfs.UDFs import *

def dedup(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0\
        .withColumn("row_number", row_number().over(Window.partitionBy("Year", "quarter").orderBy(lit(1))))\
        .filter(col("row_number") == lit(1))\
        .drop("row_number")
