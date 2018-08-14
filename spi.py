import RPi.GPIO
import time
from datetime import datetime

font = bytearray(
    [0x00, 0x00, 0x00, 0x00, 0x00, 0x3E, 0x5B, 0x4F, 0x5B, 0x3E,
	0x3E, 0x6B, 0x4F, 0x6B, 0x3E, 0x1C, 0x3E, 0x7C, 0x3E, 0x1C,
	0x18, 0x3C, 0x7E, 0x3C, 0x18, 0x1C, 0x57, 0x7D, 0x57, 0x1C,
	0x1C, 0x5E, 0x7F, 0x5E, 0x1C, 0x00, 0x18, 0x3C, 0x18, 0x00,
	0xFF, 0xE7, 0xC3, 0xE7, 0xFF, 0x00, 0x18, 0x24, 0x18, 0x00,
	0xFF, 0xE7, 0xDB, 0xE7, 0xFF, 0x30, 0x48, 0x3A, 0x06, 0x0E,
	0x26, 0x29, 0x79, 0x29, 0x26, 0x40, 0x7F, 0x05, 0x05, 0x07,
	0x40, 0x7F, 0x05, 0x25, 0x3F, 0x5A, 0x3C, 0xE7, 0x3C, 0x5A,
	0x7F, 0x3E, 0x1C, 0x1C, 0x08, 0x08, 0x1C, 0x1C, 0x3E, 0x7F,
	0x14, 0x22, 0x7F, 0x22, 0x14, 0x5F, 0x5F, 0x00, 0x5F, 0x5F,
	0x06, 0x09, 0x7F, 0x01, 0x7F, 0x00, 0x66, 0x89, 0x95, 0x6A,
	0x60, 0x60, 0x60, 0x60, 0x60, 0x94, 0xA2, 0xFF, 0xA2, 0x94,
	0x08, 0x04, 0x7E, 0x04, 0x08, 0x10, 0x20, 0x7E, 0x20, 0x10,
	0x08, 0x08, 0x2A, 0x1C, 0x08, 0x08, 0x1C, 0x2A, 0x08, 0x08,
	0x1E, 0x10, 0x10, 0x10, 0x10, 0x0C, 0x1E, 0x0C, 0x1E, 0x0C,
	0x30, 0x38, 0x3E, 0x38, 0x30, 0x06, 0x0E, 0x3E, 0x0E, 0x06,
	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x5F, 0x00, 0x00,
	0x00, 0x07, 0x00, 0x07, 0x00, 0x14, 0x7F, 0x14, 0x7F, 0x14,
	0x24, 0x2A, 0x7F, 0x2A, 0x12, 0x23, 0x13, 0x08, 0x64, 0x62,
	0x36, 0x49, 0x56, 0x20, 0x50, 0x00, 0x08, 0x07, 0x03, 0x00,
	0x00, 0x1C, 0x22, 0x41, 0x00, 0x00, 0x41, 0x22, 0x1C, 0x00,
	0x2A, 0x1C, 0x7F, 0x1C, 0x2A, 0x08, 0x08, 0x3E, 0x08, 0x08,
	0x00, 0x80, 0x70, 0x30, 0x00, 0x08, 0x08, 0x08, 0x08, 0x08,
	0x00, 0x00, 0x60, 0x60, 0x00, 0x20, 0x10, 0x08, 0x04, 0x02,
	0x3E, 0x51, 0x49, 0x45, 0x3E, 0x00, 0x42, 0x7F, 0x40, 0x00,
	0x72, 0x49, 0x49, 0x49, 0x46, 0x21, 0x41, 0x49, 0x4D, 0x33,
	0x18, 0x14, 0x12, 0x7F, 0x10, 0x27, 0x45, 0x45, 0x45, 0x39,
	0x3C, 0x4A, 0x49, 0x49, 0x31, 0x41, 0x21, 0x11, 0x09, 0x07,
	0x36, 0x49, 0x49, 0x49, 0x36, 0x46, 0x49, 0x49, 0x29, 0x1E,
	0x00, 0x00, 0x14, 0x00, 0x00, 0x00, 0x40, 0x34, 0x00, 0x00,
	0x00, 0x08, 0x14, 0x22, 0x41, 0x14, 0x14, 0x14, 0x14, 0x14,
	0x00, 0x41, 0x22, 0x14, 0x08, 0x02, 0x01, 0x59, 0x09, 0x06,
	0x3E, 0x41, 0x5D, 0x59, 0x4E, 0x7C, 0x12, 0x11, 0x12, 0x7C,
	0x7F, 0x49, 0x49, 0x49, 0x36, 0x3E, 0x41, 0x41, 0x41, 0x22,
	0x7F, 0x41, 0x41, 0x41, 0x3E, 0x7F, 0x49, 0x49, 0x49, 0x41,
	0x7F, 0x09, 0x09, 0x09, 0x01, 0x3E, 0x41, 0x41, 0x51, 0x73,
	0x7F, 0x08, 0x08, 0x08, 0x7F, 0x00, 0x41, 0x7F, 0x41, 0x00,
	0x20, 0x40, 0x41, 0x3F, 0x01, 0x7F, 0x08, 0x14, 0x22, 0x41,
	0x7F, 0x40, 0x40, 0x40, 0x40, 0x7F, 0x02, 0x1C, 0x02, 0x7F,
	0x7F, 0x04, 0x08, 0x10, 0x7F, 0x3E, 0x41, 0x41, 0x41, 0x3E,
	0x7F, 0x09, 0x09, 0x09, 0x06, 0x3E, 0x41, 0x51, 0x21, 0x5E,
	0x7F, 0x09, 0x19, 0x29, 0x46, 0x26, 0x49, 0x49, 0x49, 0x32,
	0x03, 0x01, 0x7F, 0x01, 0x03, 0x3F, 0x40, 0x40, 0x40, 0x3F,
	0x1F, 0x20, 0x40, 0x20, 0x1F, 0x3F, 0x40, 0x38, 0x40, 0x3F,
	0x63, 0x14, 0x08, 0x14, 0x63, 0x03, 0x04, 0x78, 0x04, 0x03,
	0x61, 0x59, 0x49, 0x4D, 0x43, 0x00, 0x7F, 0x41, 0x41, 0x41,
	0x02, 0x04, 0x08, 0x10, 0x20, 0x00, 0x41, 0x41, 0x41, 0x7F,
	0x04, 0x02, 0x01, 0x02, 0x04, 0x40, 0x40, 0x40, 0x40, 0x40,
	0x00, 0x03, 0x07, 0x08, 0x00, 0x20, 0x54, 0x54, 0x78, 0x40,
	0x7F, 0x28, 0x44, 0x44, 0x38, 0x38, 0x44, 0x44, 0x44, 0x28,
	0x38, 0x44, 0x44, 0x28, 0x7F, 0x38, 0x54, 0x54, 0x54, 0x18,
	0x00, 0x08, 0x7E, 0x09, 0x02, 0x18, 0xA4, 0xA4, 0x9C, 0x78,
	0x7F, 0x08, 0x04, 0x04, 0x78, 0x00, 0x44, 0x7D, 0x40, 0x00,
	0x20, 0x40, 0x40, 0x3D, 0x00, 0x7F, 0x10, 0x28, 0x44, 0x00,
	0x00, 0x41, 0x7F, 0x40, 0x00, 0x7C, 0x04, 0x78, 0x04, 0x78,
	0x7C, 0x08, 0x04, 0x04, 0x78, 0x38, 0x44, 0x44, 0x44, 0x38,
	0xFC, 0x18, 0x24, 0x24, 0x18, 0x18, 0x24, 0x24, 0x18, 0xFC,
	0x7C, 0x08, 0x04, 0x04, 0x08, 0x48, 0x54, 0x54, 0x54, 0x24,
	0x04, 0x04, 0x3F, 0x44, 0x24, 0x3C, 0x40, 0x40, 0x20, 0x7C,
	0x1C, 0x20, 0x40, 0x20, 0x1C, 0x3C, 0x40, 0x30, 0x40, 0x3C,
	0x44, 0x28, 0x10, 0x28, 0x44, 0x4C, 0x90, 0x90, 0x90, 0x7C,
	0x44, 0x64, 0x54, 0x4C, 0x44, 0x00, 0x08, 0x36, 0x41, 0x00,
	0x00, 0x00, 0x77, 0x00, 0x00, 0x00, 0x41, 0x36, 0x08, 0x00,
	0x02, 0x01, 0x02, 0x04, 0x02, 0x3C, 0x26, 0x23, 0x26, 0x3C,
	0x1E, 0xA1, 0xA1, 0x61, 0x12, 0x3A, 0x40, 0x40, 0x20, 0x7A,
	0x38, 0x54, 0x54, 0x55, 0x59, 0x21, 0x55, 0x55, 0x79, 0x41,
	0x22, 0x54, 0x54, 0x78, 0x42, 0x21, 0x55, 0x54, 0x78, 0x40,
	0x20, 0x54, 0x55, 0x79, 0x40, 0x0C, 0x1E, 0x52, 0x72, 0x12,
	0x39, 0x55, 0x55, 0x55, 0x59, 0x39, 0x54, 0x54, 0x54, 0x59,
	0x39, 0x55, 0x54, 0x54, 0x58, 0x00, 0x00, 0x45, 0x7C, 0x41,
	0x00, 0x02, 0x45, 0x7D, 0x42, 0x00, 0x01, 0x45, 0x7C, 0x40,
	0x7D, 0x12, 0x11, 0x12, 0x7D, 0xF0, 0x28, 0x25, 0x28, 0xF0,
	0x7C, 0x54, 0x55, 0x45, 0x00, 0x20, 0x54, 0x54, 0x7C, 0x54,
	0x7C, 0x0A, 0x09, 0x7F, 0x49, 0x32, 0x49, 0x49, 0x49, 0x32,
	0x3A, 0x44, 0x44, 0x44, 0x3A, 0x32, 0x4A, 0x48, 0x48, 0x30,
	0x3A, 0x41, 0x41, 0x21, 0x7A, 0x3A, 0x42, 0x40, 0x20, 0x78,
	0x00, 0x9D, 0xA0, 0xA0, 0x7D, 0x3D, 0x42, 0x42, 0x42, 0x3D,
	0x3D, 0x40, 0x40, 0x40, 0x3D, 0x3C, 0x24, 0xFF, 0x24, 0x24,
	0x48, 0x7E, 0x49, 0x43, 0x66, 0x2B, 0x2F, 0xFC, 0x2F, 0x2B,
	0xFF, 0x09, 0x29, 0xF6, 0x20, 0xC0, 0x88, 0x7E, 0x09, 0x03,
	0x20, 0x54, 0x54, 0x79, 0x41, 0x00, 0x00, 0x44, 0x7D, 0x41,
	0x30, 0x48, 0x48, 0x4A, 0x32, 0x38, 0x40, 0x40, 0x22, 0x7A,
	0x00, 0x7A, 0x0A, 0x0A, 0x72, 0x7D, 0x0D, 0x19, 0x31, 0x7D,
	0x26, 0x29, 0x29, 0x2F, 0x28, 0x26, 0x29, 0x29, 0x29, 0x26,
	0x30, 0x48, 0x4D, 0x40, 0x20, 0x38, 0x08, 0x08, 0x08, 0x08,
	0x08, 0x08, 0x08, 0x08, 0x38, 0x2F, 0x10, 0xC8, 0xAC, 0xBA,
	0x2F, 0x10, 0x28, 0x34, 0xFA, 0x00, 0x00, 0x7B, 0x00, 0x00,
	0x08, 0x14, 0x2A, 0x14, 0x22, 0x22, 0x14, 0x2A, 0x14, 0x08,
	0x55, 0x00, 0x55, 0x00, 0x55, 0xAA, 0x55, 0xAA, 0x55, 0xAA,
	0xFF, 0x55, 0xFF, 0x55, 0xFF, 0x00, 0x00, 0x00, 0xFF, 0x00,
	0x10, 0x10, 0x10, 0xFF, 0x00, 0x14, 0x14, 0x14, 0xFF, 0x00,
	0x10, 0x10, 0xFF, 0x00, 0xFF, 0x10, 0x10, 0xF0, 0x10, 0xF0,
	0x14, 0x14, 0x14, 0xFC, 0x00, 0x14, 0x14, 0xF7, 0x00, 0xFF,
	0x00, 0x00, 0xFF, 0x00, 0xFF, 0x14, 0x14, 0xF4, 0x04, 0xFC,
	0x14, 0x14, 0x17, 0x10, 0x1F, 0x10, 0x10, 0x1F, 0x10, 0x1F,
	0x14, 0x14, 0x14, 0x1F, 0x00, 0x10, 0x10, 0x10, 0xF0, 0x00,
	0x00, 0x00, 0x00, 0x1F, 0x10, 0x10, 0x10, 0x10, 0x1F, 0x10,
	0x10, 0x10, 0x10, 0xF0, 0x10, 0x00, 0x00, 0x00, 0xFF, 0x10,
	0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0xFF, 0x10,
	0x00, 0x00, 0x00, 0xFF, 0x14, 0x00, 0x00, 0xFF, 0x00, 0xFF,
	0x00, 0x00, 0x1F, 0x10, 0x17, 0x00, 0x00, 0xFC, 0x04, 0xF4,
	0x14, 0x14, 0x17, 0x10, 0x17, 0x14, 0x14, 0xF4, 0x04, 0xF4,
	0x00, 0x00, 0xFF, 0x00, 0xF7, 0x14, 0x14, 0x14, 0x14, 0x14,
	0x14, 0x14, 0xF7, 0x00, 0xF7, 0x14, 0x14, 0x14, 0x17, 0x14,
	0x10, 0x10, 0x1F, 0x10, 0x1F, 0x14, 0x14, 0x14, 0xF4, 0x14,
	0x10, 0x10, 0xF0, 0x10, 0xF0, 0x00, 0x00, 0x1F, 0x10, 0x1F,
	0x00, 0x00, 0x00, 0x1F, 0x14, 0x00, 0x00, 0x00, 0xFC, 0x14,
	0x00, 0x00, 0xF0, 0x10, 0xF0, 0x10, 0x10, 0xFF, 0x10, 0xFF,
	0x14, 0x14, 0x14, 0xFF, 0x14, 0x10, 0x10, 0x10, 0x1F, 0x00,
	0x00, 0x00, 0x00, 0xF0, 0x10, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
	0xF0, 0xF0, 0xF0, 0xF0, 0xF0, 0xFF, 0xFF, 0xFF, 0x00, 0x00,
	0x00, 0x00, 0x00, 0xFF, 0xFF, 0x0F, 0x0F, 0x0F, 0x0F, 0x0F,
	0x38, 0x44, 0x44, 0x38, 0x44, 0xFC, 0x4A, 0x4A, 0x4A, 0x34,
	0x7E, 0x02, 0x02, 0x06, 0x06, 0x02, 0x7E, 0x02, 0x7E, 0x02,
	0x63, 0x55, 0x49, 0x41, 0x63, 0x38, 0x44, 0x44, 0x3C, 0x04,
        0x40, 0x7E, 0x20, 0x1E, 0x20, 0x06, 0x02, 0x7E, 0x02, 0x02,
	0x99, 0xA5, 0xE7, 0xA5, 0x99, 0x1C, 0x2A, 0x49, 0x2A, 0x1C,
	0x4C, 0x72, 0x01, 0x72, 0x4C, 0x30, 0x4A, 0x4D, 0x4D, 0x30,
	0x30, 0x48, 0x78, 0x48, 0x30, 0xBC, 0x62, 0x5A, 0x46, 0x3D,
	0x3E, 0x49, 0x49, 0x49, 0x00, 0x7E, 0x01, 0x01, 0x01, 0x7E,
	0x2A, 0x2A, 0x2A, 0x2A, 0x2A, 0x44, 0x44, 0x5F, 0x44, 0x44,
	0x40, 0x51, 0x4A, 0x44, 0x40, 0x40, 0x44, 0x4A, 0x51, 0x40,
	0x00, 0x00, 0xFF, 0x01, 0x03, 0xE0, 0x80, 0xFF, 0x00, 0x00,
	0x08, 0x08, 0x6B, 0x6B, 0x08, 0x36, 0x12, 0x36, 0x24, 0x36,
	0x06, 0x0F, 0x09, 0x0F, 0x06, 0x00, 0x00, 0x18, 0x18, 0x00,
	0x00, 0x00, 0x10, 0x10, 0x00, 0x30, 0x40, 0xFF, 0x01, 0x01,
	0x00, 0x1F, 0x01, 0x01, 0x1E, 0x00, 0x19, 0x1D, 0x17, 0x12,
	0x00, 0x3C, 0x3C, 0x3C, 0x3C, 0x00, 0x00, 0x00, 0x00, 0x00
    ])

WIDTH = 144
HEIGHT = 168

SHARPMEM_BIT_WRITECMD = 0x80
SHARPMEM_BIT_VCOM = 0x40
SHARPMEM_BIT_CLEAR = 0x20

sharpmem_vcom = SHARPMEM_BIT_VCOM

def toggleVCOM():
    global sharpmem_vcom
    sharpmem_vcom = (0x00 if sharpmem_vcom else SHARPMEM_BIT_VCOM)

CS = 18
MOSI = 5
CLK = 6
buffer = bytearray(WIDTH * HEIGHT)

set = bytearray([1, 2, 4, 8, 16, 32, 64, 128])
clr = bytearray([254, 253, 251, 247, 239, 223, 191, 127])

RPi.GPIO.setmode(RPi.GPIO.BCM)

# Initialize GPIO Pins to correct state
RPi.GPIO.setup(CS, RPi.GPIO.OUT)
RPi.GPIO.setup(MOSI, RPi.GPIO.OUT)
RPi.GPIO.setup(CLK, RPi.GPIO.OUT)

def sendByte(data):
    for i in range(0, 8):
        RPi.GPIO.output(CLK, False)
        if data & 0x80:
            RPi.GPIO.output(MOSI, True)
        else:
            RPi.GPIO.output(MOSI, False)

        RPi.GPIO.output(CLK, True)
        data = (data << 1) & 0xff
    # Make sure clock ends low
    RPi.GPIO.output(CLK, False)

def sendByteLSB(data):
    for i in range(0, 8):
        RPi.GPIO.output(CLK, False)
        if data & 0x01:
            RPi.GPIO.output(MOSI, True)
        else:
            RPi.GPIO.output(MOSI, False)
        
        RPi.GPIO.output(CLK, True)
        data = data >> 1
    # Make sure clock ends low
    RPi.GPIO.output(CLK, False)

def setPixel(x, y, color):
    if x < 0 or y < 0 or x > WIDTH or y > HEIGHT:
        return
    if color:
        buffer[(int) ((y * WIDTH + x) / 8)] |= set[x & 7]
    else:
        buffer[(int) ((y * WIDTH + x) / 8)] &= clr[x & 7]

def drawVertLine(x, startY, endY, color):
    for y in range(startY, endY):
        setPixel(x, y, color)

def drawHorLine(startX, endX, y, color):
    for x in range(startX, endX):
        setPixel(x, y, color)

def drawLine(startX, startY, endX, endY, color):
    steep = abs(endY - startY) > abs(endX - startX)
    if steep:
        startX, startY = startY, startX
        endX, endY = endY, endX

    if startX > endX:
        startX, endX = endX, startX
        startY, endY = endY, startY

    dx = endX - startX
    dy = abs(endY - startY)

    err = dx/2
    ystep = 0

    if startY < endY:
        ystep = 1
    else:
        ystep = -1

    for startX in range(startX, endX):

        if steep:
            setPixel(startY, startX, color)
        else:
            setPixel(startX, startY, color)
        err -= dy
        if err < 0:
            startY += ystep
            err += dx

def drawRect(left, top, right, bottom, fill, color):
    if fill:
        for y in range(top, bottom):
            drawHorLine(left, right, y, color)
    else:
        drawVertLine(left, top, bottom, color)
        drawVertLine(right, top, bottom, color)
        drawHorLine(left, right, top, color)
        drawHorLine(left, right, bottom, color)

def drawCircle(x0, y0, r, color):
    f = 1-r
    ddF_x = 1
    ddF_y = -2 * r
    x = 0
    y = r
    setPixel(x0, y0+r, color)
    setPixel(x0, y0-r, color)
    setPixel(x0+r, y0, color)
    setPixel(x0-r, y0, color)

    while x < y:
        if f >= 0:
            y -= 1
            ddF_y += 2
            f += ddF_y
        x += 1
        ddF_x += 2
        f += ddF_x

        setPixel(x0 + x, y0 + y, color)
        setPixel(x0 - x, y0 + y, color)
        setPixel(x0 + x, y0 - y, color)
        setPixel(x0 - x, y0 - y, color)
        
        setPixel(x0 + y, y0 + x, color)
        setPixel(x0 - y, y0 + x, color)
        setPixel(x0 + y, y0 - x, color)
        setPixel(x0 - y, y0 - x, color)

    
def drawChar(x, y, c, size, color):
    for i in range(0, 5):
        line = font[c * 5 + i]
        for j in range(0, 8):
            if line & 1:
                if size == 1:
                    setPixel(x+i, y+j, color)
                else:
                    drawRect(x+i*size, y+j*size, (x+i*size)+size, (y+j*size)+size, True, color)
            line >>= 1


def drawString(x, y, string, size, color):
    strList = list(string)
    cursorX = x
    cursorY = y
    for i in range(0, len(strList)):
        if strList[i] == '\n':
            cursorX = 0
            cursorY += size * 8
        elif strList[i] != '\r':
            if ((cursorX + size * 6) > WIDTH):
                cursorX = 0
                cursorY += size * 8
            drawChar(cursorX, cursorY, ord(strList[i]), size, color)
            cursorX += size * 6

def fillScreen():
    for x in range(0, WIDTH):
        drawVertLine(x, 0, HEIGHT, True)
        

def clearDisplay():
    #TODO clear buffer
    # Send clear screen command
    RPi.GPIO.output(CS, True)
    sendByte(sharpmem_vcom | SHARPMEM_BIT_CLEAR)
    sendByteLSB(0x00)
    toggleVCOM()
    RPi.GPIO.output(CS, False)

def refresh():
    totalbytes = (int) ((HEIGHT * WIDTH) / 8)

    # Send the write command
    RPi.GPIO.output(CS, True)
    sendByte(SHARPMEM_BIT_WRITECMD | sharpmem_vcom);
    toggleVCOM()

    oldline = currentline = 1
    sendByteLSB(currentline)

    for i in range(0, totalbytes):
        sendByteLSB(buffer[i])
        currentline = (int) (((i+1)/(WIDTH/8)) + 1)
        if currentline != oldline:
            # Send end of line and address bytes
            sendByteLSB(0x00)
            if currentline <= HEIGHT:
                sendByteLSB(currentline)
            oldline = currentline

    # Send another trailing 8 bits for the last line
    sendByteLSB(0x00)
    RPi.GPIO.output(CS, False)

#
fillScreen()
drawString(0, 0, datetime.now().strftime("It is:  %I:%M %p"), 3, False)
refresh()
# drawVertLine((int) (WIDTH/2), 0, HEIGHT, True)
# drawHorLine(0, WIDTH, (int) (HEIGHT/2), True)
# refresh()
# drawLine(0, 0, WIDTH, HEIGHT, True)
# drawLine(WIDTH, 0, 0, HEIGHT, True)
# refresh()
# drawRect(100, 100, 125, 125, False, True)
# drawRect(25, 25, 50, 50, True, True)
# drawCircle((int)(WIDTH/2) - 1, (int)(HEIGHT/2), (int)(WIDTH/2) - 1, True)
# drawRect(0, 0, 9, 9, False, True)

