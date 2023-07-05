from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from unpivot_transformations.config.ConfigStore import *
from unpivot_transformations.udfs.UDFs import *

def OrderBy(spark: SparkSession, byYearPivot: DataFrame) -> DataFrame:
    return byYearPivot.orderBy(col("Year").asc())
