# InfluxDB V2 lesson

Documentation - https://docs.influxdata.com/influxdb/v2/

## Setup steps to complete before the lesson

1. **Windows users:**
    * You have might have to install Visual C++ Build Tools
      2015 - http://go.microsoft.com/fwlink/?LinkId=691126&fixForIE=.exe
    * Instructions taken from the influx python client: https://influxdb-client.readthedocs.io/en/stable/#installation

2. Create the virtualenv using poetry:

   ```shell
    poetry install
   ```
   
3. Build and run the influxdb docker container:
   ```shell
   docker compose up
   ```
4. Browse to the influx gui to see that everything is running
   * http://localhost:8086
   * Try to log in, good luck finding the credentials!