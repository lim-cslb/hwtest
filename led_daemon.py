import time
from rpi_ws281x import Color, PixelStrip, ws

LED_COUNT = 8
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 16
LED_INVERT = False
LED_CHANNEL = 0
LED_STRIP = ws.WS2812_STRIP

FILE_PREFIX = "/tmp/led"

if __name__ == '__main__':
    strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    strip.begin()

    col_off = [Color(0, 0, 0)]
    col_green_slow_blink = [Color(0, 0, 0), Color(0, 0, 0), Color(0, 255, 0), Color(0, 255, 0)]
    col_green_fast_blink = [Color(0, 0, 0), Color(0, 255, 0)]

    colors = [col_green_slow_blink, col_off, col_off, col_off, col_off, col_off, col_off, col_off]

    for i in range(LED_COUNT):
        fn = "%s%s" % (FILE_PREFIX, i)
        f = open(fn, "w")
        for d in colors[i]:
            f.write("%0.6X" % d)
        f.close()

    tick = 0
    while True:
        for i in range(LED_COUNT):
            fn = "%s%s" % (FILE_PREFIX, i)
            f = open(fn, "r")
            data = f.read()
            collist = [(data[j:j+6]) for j in range(0, len(data), 6)]
            col = []
            for cs in collist:
                ci = int(cs, 16)
                col.append(ci)
            colors[i] = col
            f.close()
        
        for i in range(strip.numPixels()):
            if len(colors[i]) > 0:
                strip.setPixelColor(i, colors[i][tick % len(colors[i])])
        strip.show()
        time.sleep(0.25)
        tick = tick + 1
