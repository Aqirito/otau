MQTT_SERVER = "device_ip_address"
WIFI_SSID = "wifi_network"
WIFI_PASSWORD = "wifi_password"

SENSOR_TYPE = "SO2" # CO, DHT, NO2, SO2, PM25, O3
SENSOR_IP = "sensor_ip_address" # Sensor IP address (check in the README)
TOPIC_PUB = "topic_for_publish_mqtt" # CO_sensor, DHT_sensor, NO2_sensor, SO2_sensor, PM25_sensor, O3_sensor
TOPIC_SUB = "topic_for_subscribe_mqtt" # topic for subscribe incoming message from MQTT server example: "server"