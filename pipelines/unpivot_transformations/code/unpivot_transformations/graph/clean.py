from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from unpivot_transformations.config.ConfigStore import *
from unpivot_transformations.udfs.UDFs import *

def clean(spark: SparkSession, unPivot: DataFrame) -> DataFrame:
    return unPivot.select(
        col("Year"), 
        col("quarter"), 
        concat(lit("\u20AC"), col("sales"), lit("M")).alias("sales"), 
        concat(lit("\u20AC"), (col("sales") / lit(1000)), lit("B")).alias("sales_in_billions")
    )
