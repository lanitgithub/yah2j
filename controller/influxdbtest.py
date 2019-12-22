from influxdb import InfluxDBClient
import time
while True:
    json_body = [
        {
            "measurement": "mymetrix",
            "tags": {
                "host": "myserver",
                "sampler": "mysampler"
            },
            "fields": {
                "value": 0.64,
                "min": 1.22,
                "max": 6.12
            }
        }]

    client = InfluxDBClient(
        'ec2-3-19-227-69.us-east-2.compute.amazonaws.com', 8086, 'root', 'root', 'example')
    client.write_points(json_body)
    print('!!!')
    time.sleep(1)
