# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.scanners import DioadeOrientation
from kmk.extensions.peg_oled_Display import Oled,OledDisplayMode,OledReactionType,OledData
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP0, board.GP1, board.GP2, board.GP3)
keyboard.row_pins = (board.GP4, board.GP5, board.GP6)
keyboard.diode_orientation = MatrixScanner.DIODE_COL2ROW

encoder_handler.pins =((board.GP7, board.GP8, False, False))

# set up oled
oled_data = OledData()
oled_ext = Oled(
    oled_data=oled_data,
    flip=False,
)

# track pressed keys
pressed_keys = set()

# make oled display pressed keys
def update_oled():
    pressed_text = ", ".join(sorted(pressed_keys))
    oled_ext.display_text(pressed_text)

def process_event(key, pressed, keyboard):
    key_str = str(key)
    if pressed:
        pressed_keys.add(key_str)
    else:
        pressed_keys.discard(key_str)
    update_oled()

# updates oled after the matrix scan
keyboard.after_matrix_scan = update_oled

# rotary encoder mapping
encoder_handler.map = [
                        ((KC.VOLD, KC.VOLU))
                        ]

# sw1, sw2, sw3, sw4
# sw5, sw6, sw7, sw8
# sw9, sw10, sw11, sw12
keyboard.keymap = [
    [
        KC.VOLU, KC.VOLD, KC.MUTE,KC.HOME,
        KC.7, KC.8, KC.9, KC.DELETE,
        KC.4, KC.5, KC.6, KC.ENTER,
        Kc.1, KC.2, KC.3, KC.0,
    ]
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()