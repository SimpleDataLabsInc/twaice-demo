from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from dataanalysislookup.config.ConfigStore import *
from dataanalysislookup.udfs.UDFs import *

def OrderByCount(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.orderBy(col("count").desc())
