from pyautogui import size
from pynput.keyboard import Key, Listener
from pynput.mouse import Button, Controller
import configparser
from os.path import exists

config = configparser.ConfigParser()

if not exists("cnfif.ini"):
	config['DEFAULT'] = {'a':97, 'g':98, 'e':99, 'd':100, 'c':101, 'f': 102}

	with open('cnfif.ini', 'w') as cnf:
		config.write(cnf)
else:
	config.read('cnfif.ini')
cfg = {}
for a in config['DEFAULT']:
	cfg[a] = int(config['DEFAULT'][a])

sx, sy = size()

ms = Controller()

print("""--------------------------------
TERRARIA INSTRUMENT HELPER v1.0.0
                          by LMNYX
  Fork on
       github.com/LMNYX/TerrariaGuitar
--------------------------------""")

def on_press(key):
    try:
    	if(key.vk == cfg['a']):
    		print("A#")
    		ms.position = (sx/2,sy/2)
    		ms.press(Button.left)
    	if(key.vk == cfg['g']):
    		print("G#")
    		ms.position = (sx/2+100,sy/2)
    		ms.press(Button.left)
    	if(key.vk == cfg['e']):
    		print("E#")
    		ms.position = (sx/2+200,sy/2)
    		ms.press(Button.left)
    	if(key.vk == cfg['d']):
    		print("D#")
    		ms.position = (sx/2+250,sy/2)
    		ms.press(Button.left)
    	if(key.vk == cfg['c']):
    		print("C#")
    		ms.position = (sx/2+350,sy/2)
    		ms.press(Button.left)
    	if(key.vk == cfg['f']):
    		print("F#")
    		ms.position = (sx/2+400,sy/2)
    		ms.press(Button.left)
    except Exception:
    	return

def on_release(key):
    try:
    	if key.vk == cfg['g'] or key.vk == cfg['d'] or key.vk == cfg['e'] or key.vk == cfg['f'] or key.vk == cfg['c'] or key.vk == cfg['a']:
    		ms.release(Button.left)
    except Exception:
    	pass
    if key == Key.f4:
        # Stop listener
        return False

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()