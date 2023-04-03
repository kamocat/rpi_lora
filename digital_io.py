import gpiod

class PinIn:
    def __init__(self,chip,line):
        self.line = gpiod.chip(chip).get_line(line)
        config = gpiod.line_request()
        config.consumer=__name__
        config.request_type = gpiod.line_request.DIRECTION_INPUT
        self.line.request(config)

    def get(self):
        return self.line.get_value()
    

class PinOut:
    def __init__(self,chip,line):
        self.line = gpiod.chip(chip).get_line(line)
        config = gpiod.line_request()
        config.consumer=__name__
        config.request_type = gpiod.line_request.DIRECTION_OUTPUT
        self.line.request(config)

    def set(self, val):
        return self.line.set_value(val)
    
    def on(self):
        self.set(1)

    def off(self):
        self.set(0)
