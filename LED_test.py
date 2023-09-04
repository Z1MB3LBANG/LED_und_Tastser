from gpiozero import Button, LED

 

class led:

    def __init__(self, pin):

        self.led_pin = LED(pin)

        self.led_on = False

 

    def led_set(self):

        if self.led_on:

            self.led_pin.on()

        else:

            self.led_pin.off()

 

class button(led):

    def __init__(self, led_pin, button_pin):

        super().__init__(led_pin)

        self.button_pin = Button(button_pin)

        self.button_pin.when_pressed = self.button_pressed

 

    def button_pressed(self):

        self.led_on = not self.led_on

        self.led_set()

 

b = button(led_pin=12, button_pin=25)

 

while True:

    b.button_pressed()