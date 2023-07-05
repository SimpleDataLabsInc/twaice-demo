from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from timestamp_conversion_example.config.ConfigStore import *
from timestamp_conversion_example.udfs.UDFs import *
from prophecy.utils import *
from timestamp_conversion_example.graph import *

def pipeline(spark: SparkSession) -> None:
    df_user_data = user_data(spark)
    df_SchemaTransform_1 = SchemaTransform_1(spark, df_user_data)
    user_final_data(spark, df_SchemaTransform_1)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/timestamp_conversion_example")
    registerUDFs(spark)
    
    MetricsCollector.start(spark = spark, pipelineId = "pipelines/timestamp_conversion_example")
    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
