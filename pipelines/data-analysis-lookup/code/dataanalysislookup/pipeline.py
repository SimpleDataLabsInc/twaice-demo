from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from dataanalysislookup.config.ConfigStore import *
from dataanalysislookup.udfs.UDFs import *
from prophecy.utils import *
from dataanalysislookup.graph import *

def pipeline(spark: SparkSession) -> None:
    df_laptop_data = laptop_data(spark)
    df_byModel = byModel(spark, df_laptop_data)
    df_OrderByCount = OrderByCount(spark, df_byModel)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/data-analysis-lookup")
    registerUDFs(spark)
    
    MetricsCollector.start(spark = spark, pipelineId = "pipelines/data-analysis-lookup")
    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
