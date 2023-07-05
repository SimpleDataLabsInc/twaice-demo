from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from unpivot_transformations.config.ConfigStore import *
from unpivot_transformations.udfs.UDFs import *

def byYearPivot(spark: SparkSession, in0: DataFrame) -> DataFrame:
    df1 = in0.groupBy(col("Year"))

    return df1.agg(sum(col("sales")).alias("total_sales"))
