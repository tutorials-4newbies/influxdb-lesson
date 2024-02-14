from random import random
from time import sleep

from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from influxdb_client.domain.bucket_retention_rules import BucketRetentionRules

client = InfluxDBClient(url="http://localhost:8086", token="super_secret_token", org="my_org")

#
# 1 - create a bucket
#
bucket = "storage_deck"

buckets_api = client.buckets_api()
retention_rules = BucketRetentionRules(type="expire", every_seconds=3600)  # one hour
created_bucket = buckets_api.create_bucket(bucket_name=bucket, retention_rules=retention_rules, org="my_org")

#
# 2-  Write some data
#
write_api = client.write_api(write_options=SYNCHRONOUS)
for i in range(0, 2000):
    temp_from_sensor = random.randrange(0, 1000)
    p = Point("temperature").tag("location", "top").field("heat", temp_from_sensor)

    write_api.write(bucket=bucket, record=p)
    print("next")
write_api.close()

#
# 3 - Make some queries
#
query_api = client.query_api()

query_text = f"""
    from(bucket:"{bucket}")
        |> range(start: -10m)
    """

result_tables = query_api.query(query_text)

for table in result_tables:
    print(table)
    for row in table.records:
        value = row.values.get("_value")
        timestamp = row.values.get("_time")
        print(f"{timestamp} - {value}")


# get only highest
query_text = f"""
        from(bucket:"{bucket}")
            |> range(start: -10m)
            |> filter(fn: (r) => r["_value"] >= 987)
        """

# get only highest
query_text = f"""
        from(bucket:"{bucket}")
            |> range(start: -10m)
            |> filter(fn: (r) => r["_value"] >= 987)
            |> aggregateWindow(every: 1m, fn: mean, createEmpty: false)
        """