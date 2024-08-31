import board
import digitalio
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Configuração dos pinos para o DB9
pin_config = {
    'up': board.GP2,     # DB9 pino 1
    'down': board.GP4,   # DB9 pino 2
    'left': board.GP6,   # DB9 pino 3
    'right': board.GP8,  # DB9 pino 4
    'b': board.GP10,      # DB9 pino 6
    'c': board.GP12,      # DB9 pino 9
    'select': board.GP14, # DB9 pino 7
    
    # Pino 5 (VCC) não é conectado ao Pico
    # Pino 8 (GND) deve ser conectado ao GND do Pico
}

buttons = {name: digitalio.DigitalInOut(pin) for name, pin in pin_config.items()}
for button in buttons.values():
    button.direction = digitalio.Direction.INPUT
    button.pull = digitalio.Pull.UP

keyboard = Keyboard(usb_hid.devices)

button_map = {
    'up': Keycode.UP_ARROW,
    'down': Keycode.DOWN_ARROW,
    'left': Keycode.LEFT_ARROW,
    'right': Keycode.RIGHT_ARROW,
    'a': Keycode.A,
    
    'b': Keycode.X,
    'c': Keycode.C,
    'x': Keycode.Z,
    
    'y': Keycode.S,
    'z': Keycode.D,
    'start': Keycode.M,
    'mode': Keycode.ENTER
}

def read_extended_buttons():
    buttons['select'].direction = digitalio.Direction.OUTPUT
    buttons['select'].value = False
    time.sleep(0.000020)  # 20 microssegundos
    #a_state = buttons['up'].value
    #start_state = buttons['down'].value
    #z_state = buttons['left'].value
    #y_state = buttons['right'].value
    x_state = buttons['b'].value
    mode_state = buttons['c'].value
    buttons['select'].direction = digitalio.Direction.INPUT
    buttons['select'].pull = digitalio.Pull.UP
    time.sleep(0.000020)  # Aguarde antes de ler novamente
    return {'x': not x_state, 'mode': not mode_state}

last_state = {name: False for name in button_map}
debounce_time = 0.005
extended_read_interval = 0.016  # ~60Hz
last_extended_read = time.monotonic()

print("Inicializando o controlador...")

while True:
    current_time = time.monotonic()
    
    # Lê os botões padrão
    for name, button in buttons.items():
        if name != 'select':
            current_state = not button.value
            if current_state != last_state[name]:
                time.sleep(debounce_time)
                if not button.value == current_state:
                    if name in button_map:
                        if current_state:
                            print(f"Pressionando {name}")
                            keyboard.press(button_map[name])
                        else:
                            print(f"Soltando {name}")
                            keyboard.release(button_map[name])
                    last_state[name] = current_state
    
    # Lê os botões estendidos em intervalos
    if current_time - last_extended_read >= extended_read_interval:
        extended_buttons = read_extended_buttons()
        for name, state in extended_buttons.items():
            if state != last_state[name]:
                time.sleep(debounce_time)
                if state == extended_buttons[name]:
                    if name in button_map:
                        if state:
                            print(f"Pressionando {name}")
                            keyboard.press(button_map[name])
                        else:
                            print(f"Soltando {name}")
                            keyboard.release(button_map[name])
                    last_state[name] = state
        last_extended_read = current_time
    
    time.sleep(0.001)