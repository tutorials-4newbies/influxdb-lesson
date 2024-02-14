import random
from time import sleep

from influxdb_client import InfluxDBClient
from influxdb_client.client.write.point import Point
from influxdb_client.client.write_api import SYNCHRONOUS
from influxdb_client.domain.bucket_retention_rules import BucketRetentionRules


def main():
    bucket = "storage"
    client = InfluxDBClient(url="http://localhost:8086", token="super_secret_token", org="my_org")

if __name__ == '__main__':
    main()
