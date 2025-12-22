class Device(object):
    #data attributes
    device_type = "Electronic Device"
    def __init__(self, brand):
        self.brand = brand
        self._is_on = False
    
    #method to turn on the device
    def turn_on(self):
        self._is_on = True


  