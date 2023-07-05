from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from unpivot_transformations.config.ConfigStore import *
from unpivot_transformations.udfs.UDFs import *
from prophecy.utils import *
from unpivot_transformations.graph import *

def pipeline(spark: SparkSession) -> None:
    df_quarterly_sales_data = quarterly_sales_data(spark)
    df_byYear = byYear(spark, df_quarterly_sales_data)
    df_unPivot = unPivot(spark, df_quarterly_sales_data)
    df_dedup = dedup(spark, df_unPivot)
    df_reformat = reformat(spark, df_dedup)
    df_clean = clean(spark, df_unPivot)
    df_byYearPivot = byYearPivot(spark, df_reformat)
    df_OrderBy = OrderBy(spark, df_byYearPivot)
    df_OrderByY = OrderByY(spark, df_byYear)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/unpivot_transformations")
    registerUDFs(spark)
    
    MetricsCollector.start(spark = spark, pipelineId = "pipelines/unpivot_transformations")
    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
