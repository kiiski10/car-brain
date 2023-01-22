from decimal import Decimal
import os
import re
import time

base_sensor_path = os.path.join(
    "/",
    "sys",
    "bus",
    "w1",
    "devices",
)


class OneWireService:
    sensors = {}    
    valid_bus_address_re = re.compile("^(28-){1}[a-z0-9]{12}$")

    def __init__(self):
        print("Init 1-Wire service")
        self.find_sensors()
        self.read_all()
        for bus_adress, sensor in self.sensors.items():
            print("  {}".format(str(sensor)))

    def find_sensors(self):
        bus_addresses = [ba for ba in os.listdir(base_sensor_path) if self.valid_bus_address_re.match(ba)]
        self.sensors = {}
        for bus_address in bus_addresses:
            self.sensors[bus_address] = OneWireSensor(bus_address)
        
    def read_all(self):
        for bus_address, sensor in self.sensors.items():
            sensor.read()


class OneWireSensor:
    bus_address = ""
    latest_reading = None
    latest_reading_timestamp = None
    file_path = ""
    
    def __str__(self):
        return "{}: {}".format(
            self.bus_address,
            self.latest_reading,
        )

    def __init__(self, bus_address):
        self.bus_address = bus_address
        self.file_path = os.path.join(
            base_sensor_path,
            self.bus_address,
            "w1_slave"
        )
    
    def read(self):
        with open(self.file_path, "r") as sensor_file:
            line = [line for line in sensor_file.readlines() if " t=" in line][0]
            temp = Decimal(line.split(" t=")[-1]) / 1000

        self.latest_reading = temp
        self.latest_reading_timestamp = time.time()

        return temp
