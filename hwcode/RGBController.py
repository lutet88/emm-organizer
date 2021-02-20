"""
# RGBController.py
# github.com/lutet88
#
# a library to communicate with rgbController.ino
# with some nice asynchronous functions
#
# should be pretty fast
#
"""


from serial import Serial
from serial.serialutil import SerialException
from queue import Queue
import threading
import time


# hardware info
DEFAULT_HEADER = 0xCD
NUM_PIXELS = 7
NUM_STRIPS = 20

# command info
CMD_CLEAR = 0x14
CMD_REFRESH = 0x15
PIXEL_ALL = 0xAA


class RGBController:
        
    def __init__(self, port, baudrate=115200, timeout=0, feedback=False):
        """
        Constructor.

        Parameters:
        port: port to open on
        baudrate: expected baudrate (115200 default)
        timeout: pySerial timeout (0 default)
        feedback: whether to start a thread to print out Serial reads (False default)
        """
        self.baudrate = baudrate
        self.port = port
        self.timeout = timeout
        try:
            self.ser = Serial(port, baudrate, timeout=timeout)
        except SerialException:
            self.ser = None
        self.read_thread = threading.Thread(target=self.__read_all, args=[self.ser]) if feedback else None
        self.write_queue = Queue()
        self.write_thread = threading.Thread(target=self.__write_all, args=[self.write_queue])
        self.write_thread.start()


    def __write_all(self, queue):
        while True:
            data = queue.get()
            if data:
                self.__async_write(data)
            time.sleep(0.001)


    def __async_write(self, data):
        self.__connect()
        try:
            for byte in data:
                self.ser.write(chr(byte).encode("latin"))
            return True
        except SerialException:
            return False


    def __write(self, header, strip, pixel, r, g, b):
        self.write_queue.put((header, strip, pixel, r, g, b))


    def __connect(self):
        """__connect() - will attempt to connect to serial. called every __write or __async_write"""
        while True:
            try:
                if self.ser == None:
                    self.ser = Serial(self.port, self.baudrate, timeout=self.timeout)
                else:
                    if not self.ser.is_open:
                        self.ser.open()
                    self.ser.reset_input_buffer()
                break
            except SerialException:
                if not self.ser == None:
                    try:
                        self.ser.close()
                    except:
                        pass
                    self.ser = None
                time.sleep(0.5)

    
    def __read_all(self, ser):
        while True:
            print(ser.readline())
            time.sleep(0.01)

    def __detect_anomalies(self, strip, pixel, r, g, b):
        if strip < 0 or (strip >= NUM_STRIPS and not strip in [CMD_CLEAR, CMD_REFRESH]):
            raise Exception("Invalid strip: "+str(strip))
        if pixel < 0 or (pixel >= NUM_PIXELS and not strip in [PIXEL_ALL]):
            raise Exception("Invalid pixel: "+str(pixel))
        r = 255 if r > 255 else r
        g = 255 if g > 255 else g
        b = 255 if b > 255 else b
        return strip, pixel, r, g, b


    def refresh(self):
        """refresh() - Refreshes all LEDs. """
        self.__write(DEFAULT_HEADER, CMD_REFRESH, 0, 0, 0, 0)


    def setPixel(self, strip, pixel, r, g, b, refresh=False):
        """setPixel(strip, pixel, r, g, b, refresh=False) - sets a single pixel in the setup."""
        strip, pixel, r, g, b = self.__detect_anomalies(strip, pixel, r, g, b)
        self.__write(DEFAULT_HEADER, strip, pixel, r, g, b)
        if refresh:
            self.refresh()


    def fillStrip(self, strip, r, g, b, refresh=False):
        """fillStrip(strip, r, g, b, refresh=False) - fills an entire strip with a single color."""
        strip, _, r, g, b = self.__detect_anomalies(strip, 0, r, g, b)
        self.__write(DEFAULT_HEADER, strip, PIXEL_ALL, r, g, b)
        if refresh:
            self.refresh()


    def fillAll(self, r, g, b, refresh=False):
        """fillAll(r, g, b, refresh=False) - fills all pixels with a single color."""
        for i in range(NUM_STRIPS):
            self.fillStrip(i, r, g, b)
        if refresh:
            self.refresh()
    

    def clear(self):
        """clear() - clears all LEDs. """
        self.__write(DEFAULT_HEADER, CMD_CLEAR, 0, 0, 0, 0)


    def __del__(self):
        self.write_thread.join()
        if self.read_thread:
            self.read_thread.join()
        
        
        
