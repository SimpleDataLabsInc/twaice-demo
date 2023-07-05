from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from unpivot_transformations.config.ConfigStore import *
from unpivot_transformations.udfs.UDFs import *

def unPivot(spark: SparkSession, quarterly_sales_data: DataFrame) -> DataFrame:
    out0 = quarterly_sales_data.selectExpr(
        "Year",
        "stack(4, 'Q1', Q1, 'Q2', Q2, 'Q3', Q3, 'Q4', Q4) as (quarter, sales)"
    )

    return out0
