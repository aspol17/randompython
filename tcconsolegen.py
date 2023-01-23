def interpret(rgb, char):
  
# the format that i'm looking to create is 8 hex numbers with a length of 2, without the 0x prefix

    global chari
    chari = hex(char)
    chari = chari.replace('0x', '')
    global r
    global g
    global b 
    global br 
    global bg
    global bb
    r, g, b, br, bg, bb = [rgb[i] for i in (0, 1, 2, 3, 4, 5)]
    r = hex(r)
    g = hex(g)
    b = hex(b)
    br = hex(br)
    bg = hex(bg)
    bb = hex(bb)
    r = r.replace('0x', '')
    g = g.replace('0x', '')
    b = b.replace('0x', '')
    br = br.replace('0x', '')
    bg = bg.replace('0x', '')
    bb = bg.replace('0x', '')
    if(len(r) < 2):
        r = '0' + r
        if(r == '000'):
            r = '00'
    if(len(g) < 2):
        g = '0' + r
        if(g == '000'):
            r = '00'
    if(len(b) < 2):
        b = '0' + b
        if(b == '000'):
            b = '00'
    if(len(br) < 2):
        br = '0' + br
        if(br == '000'):
            br = '00'
    if(len(bg) < 2):
        bg = '0' + bg
        if(bg == '000'):
            bg = '00'
    if(len(bb) < 2):
        bb = '0' + bb
        if(bb == '000'):
            bg = '00'

def codes(rgb):
  
#   this prints the hex codes for the character color, and the background color, formatted so that it's easier
#   to copy into html and stuff

    char = 0
    interpret(rgb, char)
    print("Output: \n")
    print("Foreground:\n" + "#" + r + g + b + '\n')
    print("Background:\n" + "#" + br + bg + bb + '\n')

def generate(time, rgb, char):
  
#   this prints the machine code for the console in the game 'Turing Complete' by Stuffe
#   each 8 bytes is 1 pixel
#   this follows the format of
#   -----------------------------------------------------------------------
#   the character that will be displayed, the RGB values of the character color,
#   the RGB values of the space around the character, an empty unused byte.
#   -----------------------------------------------------------------------
#   for example if i were to call:
#   "rgb = [255, 255, 255, 0, 0, 0]"
#   "generate(1, rgb, a)"
#   
#   this should output:
#   61 ff ff ff 00 00 00 00
#
#   which outputs a white "a" on a black background.
  
  
    interpret(rgb, char)
    for i in range(time):
        print("\n", char, r, g, b, br, bg, bb, '00')
        
char = ord(input("Character: "))
time = int(input("How many cycles?: "))
rgb = []
for i in range(6):
  ele = int(input("Color code: "))
  rgb.append(ele)
choice = int(input("Code or Hex values?: (1 or 2)"))
if(choice == 1):
    generate(time, rgb, char)
if(choice == 2):
   codes(rgb)
