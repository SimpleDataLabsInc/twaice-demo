from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from unpivot_transformations.config.ConfigStore import *
from unpivot_transformations.udfs.UDFs import *

def byYear(spark: SparkSession, in0: DataFrame) -> DataFrame:
    df1 = in0.groupBy(col("Year"))

    return df1.agg((((first(col("Q1")) + first(col("Q2"))) + first(col("Q3"))) + first(col("Q4"))).alias("total_sales"))
