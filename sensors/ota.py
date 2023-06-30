import config
import os
import utime
import urequests
import machine

mqtt_server = config.MQTT_SERVER

def download_file():
    i = 0
    server_url = f"http://{mqtt_server}:8000/" # TODO: start the file server from node-RED. Example: python -m http.server
    FILES = os.listdir()
    print(FILES)
    for file in FILES:
        i+=1
        response = urequests.get(server_url + file)
        if response.status_code == 200:
            print("downloading", response.content)
            f = open(file, "w")
            f.write(response.content)
            f.close()
            response.close()
        else:
            print(response.status_code)
        if i >= len(FILES):
            print("download complete.")
            print("resetting machine...")
            machine.reset()