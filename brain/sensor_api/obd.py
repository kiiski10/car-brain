import obd


class OBDService:
    """
    TODO:
        make this class able to maintain serial port connectivity with
        elm327 and keep track of latest sensor data

    """
    serial_port = "/dev/ttyUSB0"
    connection = None

    def __init__(self):
        print("Init OBD service")
        self.connection = obd.OBD(self.serial_port)
        cmd = obd.commands.SPEED                # select an OBD command (sensor)
        
        response = self.connection.query(cmd)   # send the command, and parse the response
        print(response.value)                   # returns unit-bearing values thanks to Pint
        print(response.value.to("mph"))         # user-friendly unit conversions
