import time
import pychromecast
import json

from tkinter import *

cast_devices = {}

class app(object):
        def __init__(self):
                self.root = Tk()
                self.root.attributes('-zoomed', True)
                self.cast = None
                self.chromecasts = []
                self.volume = 0.0
                self.itemlist={}
                self.c_cast = StringVar(self.root)
                self.c_cast.set("None")


                self.display_app()

        def list_chromecasts(self):
                self.chromecasts, _ = pychromecast.get_chromecasts()
                self.itemlist = {}
                for  idx,dev in enumerate(self.chromecasts):
                        self.itemlist[dev.device.friendly_name] = dev
                print([cc.device.friendly_name for cc in self.chromecasts])

        def select_chromecast(self):
                self.cast = self.itemlist[self.c_cast.get()]
                self.cast.wait()
                print(self.cast.status)

        def vol_down(self):
                self.cast.volume_down(0.1)

        def vol_up(self):
                self.cast.volume_up(0.1)

        def c_play(self):
                mc = self.cast.media_controller
                self.cast.wait()
                time.sleep(1)
                mc.play()
        
        def c_pause(self):
                mc = self.cast.media_controller
                self.cast.wait()
                time.sleep(1)
                mc.pause()

        def cast_local_vid(self):
                mc = self.cast.media_controller
                mc.play_media("http://192.168.1.2:8000/aa.mp4", content_type = "video/mp4")
                mc.block_until_active()
                mc.play()

        def display_app(self):
                #self.root.geometry("200x200")
                self.list_chromecasts()

                values = [cc.device.friendly_name for cc in self.chromecasts]
                dd_menu = OptionMenu(self.root, self.c_cast, *values)
                dd_menu.config(font=('calibri',(19)),bg='white',width=12)
                dd_menu['menu'].config(font=('calibri',(19)),bg='white')
                dd_menu.grid(row=1, column=1, rowspan = 3, columnspan = 2, sticky = N+W+E+S)
                Label(self.root, text = "\t\t").grid(row=0, column=0)
                Label(self.root, text = "\t\t").grid(row=0, column=1)
                Label(self.root, text = "\t\t").grid(row=0, column=2)
                Label(self.root, text = "\t\t").grid(row=0, column=3)
                Label(self.root, text = "\t\t").grid(row=0, column=4)
                Label(self.root, text = "\t\t").grid(row=0, column=5)
                Label(self.root, text = "\t\t").grid(row=0, column=6)
                Label(self.root, text = "\t\t").grid(row=0, column=7)
                Label(self.root, text = "\t\t").grid(row=0, column=8)
                Label(self.root, text = "\t\t").grid(row=0, column=9)
                Label(self.root, text = "\t\t").grid(row=0, column=0)
                Label(self.root, text = "\t\t").grid(row=1, column=0)
                Label(self.root, text = "\t\t").grid(row=2, column=0)
                Label(self.root, text = "\t\t").grid(row=3, column=0)
                Label(self.root, text = "\t\t").grid(row=4, column=0)
                Label(self.root, text = "\t\t").grid(row=5, column=0)
                Label(self.root, text = "\t\t").grid(row=6, column=0)
                Label(self.root, text = "\t\t").grid(row=7, column=0)
                Label(self.root, text = "\t\t").grid(row=8, column=0)
                Label(self.root, text = "\t\t").grid(row=9, column=0)
                Label(self.root, text = "\t\t").grid(row=10, column=0)
                Label(self.root, text = "\t\t").grid(row=11, column=0)
                Label(self.root, text = "\t\t").grid(row=12, column=0)
                Label(self.root, text = "\t\t").grid(row=13, column=0)
                Label(self.root, text = "\t\t").grid(row=14, column=0)

                Button(self.root, text="Set", command=self.select_chromecast).grid(row=1, column=3, rowspan = 3, columnspan = 2, sticky = N+W+E+S)

                Button(self.root, text="+", command=self.vol_up).grid(row=6, column=2, rowspan = 3, columnspan = 2, sticky = N+W+E+S)

                Button(self.root, text="-", command=self.vol_down).grid(row=12, column=2, rowspan = 3, columnspan = 2, sticky = N+W+E+S)

                Button(self.root, text="Play", command=self.c_play).grid(row=9, column=1, rowspan = 3, columnspan = 2, sticky = N+W+E+S)
                Button(self.root, text="Pause", command=self.c_pause).grid(row=9, column=3, rowspan = 3, columnspan = 2, sticky = N+W+E+S)



                self.root.mainloop()

app()