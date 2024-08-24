#DellDisplayManagerLite for linux
#by manu treguer

#Version 1: select entry and preset for Model: DELL U3421WE ok/ colored power off button ok /app icon in tack bar ok


#!/usr/bin/env python3
# coding: utf-8

import subprocess
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk


class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="DELL Display Manager Lite")

        self.box = Gtk.Box(spacing=6)
        self.add(self.box)

        self.button_standard = Gtk.Button(label="Standard")
        self.button_standard.connect('clicked', self.on_button_standard_clicked)
        self.box.pack_start(self.button_standard, True, True, 0)

        self.button_cfrtview = Gtk.Button(label="ConfortView")
        self.button_cfrtview.connect('clicked', self.on_button_cfrtview_clicked)
        self.box.pack_start(self.button_cfrtview, True, True, 0)

        self.button_game = Gtk.Button(label="Game")
        self.button_game.connect('clicked', self.on_button_game_clicked)
        self.box.pack_start(self.button_game, True, True, 0)

        self.button_usb = Gtk.Button(label="Entrée USB")
        self.button_usb.connect('clicked', self.on_button_usb_clicked)
        self.box.pack_start(self.button_usb, True, True, 0)

        self.button_Off = Gtk.Button(label="ETEINDRE" )
        self.button_Off.connect('clicked', self.on_button_Off_clicked)
        self.box.pack_start(self.button_Off, True, True, 0)
        self.color = Gdk.color_parse('#ff9c33')
        self.color2 = Gdk.color_parse('#f02312')
        """deprecié mais marche tjrs: https://stackoverflow.com/questions/25492122/gtk3-python-change-single-button-color"""
        self.button_Off.modify_bg(Gtk.StateFlags.NORMAL, self.color)
        self.button_Off.modify_bg(Gtk.StateFlags.PRELIGHT, self.color2)
 #       self.button_Off.override_background_color(button_Off, GTK_STATE_NORMAL, self.color);
 #       self.button_Off.override_background_color(button_Off, GTK_STATE_PRELIGHT, self.color);


    def on_button_standard_clicked(self, widget):
        subprocess.run("ddcutil setvcp DC 0x00 --bus 8", shell=True )

    def on_button_cfrtview_clicked(self, widget):
        subprocess.run("ddcutil setvcp F0 0x0C --bus 8", shell=True )

    def on_button_game_clicked(self, widget):
        subprocess.run("ddcutil setvcp DC 0x05 --bus 8", shell=True )

    def on_button_usb_clicked(self, widget):
        subprocess.run("ddcutil setvcp 60 0x1b --bus 8", shell=True )

    def on_button_Off_clicked(self, widget):
        subprocess.run("ddcutil setvcp D6 0x05 --bus 8", shell=True )




win = MyWindow()
"""definit l'icone de l'application en une simple ligne, l'icone doit etre dans le meme dossier que le fichier py de l'application
trouvé ici https://stackoverflow.com/questions/4416336/adding-a-program-icon-in-python-gtk"""
win.set_icon_from_file("dellicon.png")

win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()


"""ddcutil capabilities --verbose
Feature definition file not found: DEL-DELL_U3421WE-41345.mccs
Read cached capabilities string from /home/manu/.cache/ddcutil/capabilities
Unparsed capabilities string: (prot(monitor)type(lcd)model(U3421WE)cmds(01 02 03 07 0C E3 F3)vcp(02 04 05 08 10 12 14(01 04 05 06 08 09 0B 0C) 16 18 1A 52 60( 1B 0F 11 12) 62 AC AE B2 B6 C6 C8 C9 CC(02 03 04 06 09 0A 0D 0E) D6(01 04 05) DC(00 03 05) DF E0 E1 E2(00 1D 02 04 0C 0D 0F 10 11 13 0B 1B 14) E4 E5 E7(00 02) E8 E9(00 01 02 21 22 24 2B 2C) F0(00 05 06 0A 0C) F1 F2 FD)mccs_ver(2.1)mswhql(1))
Model: U3421WE
MCCS version: 2.1
Commands:
   Op Code: 01 (VCP Request)
   Op Code: 02 (VCP Response)
   Op Code: 03 (VCP Set)
   Op Code: 07 (Timing Request)
   Op Code: 0C (Save Settings)
   Op Code: E3 (Capabilities Reply)
   Op Code: F3 (Capabilities Request)
VCP Features:
   Feature: 02 (New control value)
   Feature: 04 (Restore factory defaults)
   Feature: 05 (Restore factory brightness/contrast defaults)
   Feature: 08 (Restore color defaults)
   Feature: 10 (Brightness)
   Feature: 12 (Contrast)
   Feature: 14 (Select color preset)
      Values (unparsed): 01 04 05 06 08 09 0B 0C
      Values (  parsed):
         01: sRGB
         04: 5000 K
         05: 6500 K
         06: 7500 K
         08: 9300 K
         09: 10000 K
         0b: User 1
         0c: User 2
   Feature: 16 (Video gain: Red)
   Feature: 18 (Video gain: Green)
   Feature: 1A (Video gain: Blue)
   Feature: 52 (Active control)
   Feature: 60 (Input Source)
      Values (unparsed):  1B 0F 11 12
      Values (  parsed):
         1b: Unrecognized value
         0f: DisplayPort-1
         11: HDMI-1
         12: HDMI-2
   Feature: 62 (Audio speaker volume)
   Feature: AC (Horizontal frequency)
   Feature: AE (Vertical frequency)
   Feature: B2 (Flat panel sub-pixel layout)
   Feature: B6 (Display technology type)
   Feature: C6 (Application enable key)
   Feature: C8 (Display controller type)
   Feature: C9 (Display firmware level)
   Feature: CC (OSD Language)
      Values (unparsed): 02 03 04 06 09 0A 0D 0E
      Values (  parsed):
         02: English
         03: French
         04: German
         06: Japanese
         09: Russian
         0a: Spanish
         0d: Chinese (simplified / Kantai)
         0e: Portuguese (Brazil)
   Feature: D6 (Power mode)
      Values (unparsed): 01 04 05
      Values (  parsed):
         01: DPM: On,  DPMS: Off
         04: DPM: Off, DPMS: Off
         05: Write only value to turn off display
   Feature: DC (Display Mode)
      Values (unparsed): 00 03 05
      Values (  parsed):
         00: Standard/Default mode
         03: Movie
         05: Games
   Feature: DF (VCP Version)
   Feature: E0 (Manufacturer specific feature)
   Feature: E1 (Manufacturer specific feature)
   Feature: E2 (Manufacturer specific feature)
      Values (unparsed): 00 1D 02 04 0C 0D 0F 10 11 13 0B 1B 14
      Values (  parsed): 00 1D 02 04 0C 0D 0F 10 11 13 0B 1B 14 (interpretation unavailable)
   Feature: E4 (Manufacturer specific feature)
   Feature: E5 (Manufacturer specific feature)
   Feature: E7 (Manufacturer specific feature)
      Values (unparsed): 00 02
      Values (  parsed): 00 02 (interpretation unavailable)
   Feature: E8 (Manufacturer specific feature)
   Feature: E9 (Manufacturer specific feature)
      Values (unparsed): 00 01 02 21 22 24 2B 2C
      Values (  parsed): 00 01 02 21 22 24 2B 2C (interpretation unavailable)
   Feature: F0 (Manufacturer specific feature)
      Values (unparsed): 00 05 06 0A 0C
      Values (  parsed): 00 05 06 0A 0C (interpretation unavailable)
   Feature: F1 (Manufacturer specific feature)
   Feature: F2 (Manufacturer specific feature)
   Feature: FD (Manufacturer specific feature)
manu@PC-solus ~/Programmation/Pyhon $ ^C
manu@PC-solus ~/Programmation/Pyhon $ ddcutil detect
Invalid display
   I2C bus:  /dev/i2c-3
   DRM connector:           card0-HDMI-A-1
   EDID synopsis:
      Mfg id:               SNY - Sony
      Model:                AV Receiver
      Product code:         20995  (0x5203)
      Serial number:        
      Binary serial number: 16843009 (0x01010101)
      Manufacture year:     2013,  Week: 41
   DDC communication failed. (getvcp of feature x10 returned Error_Info[ENXIO in ddc_write_read_with_retry, causes: ENXIO])

Display 1
   I2C bus:  /dev/i2c-8
   DRM connector:           card0-DP-1
   EDID synopsis:
      Mfg id:               DEL - Dell Inc.
      Model:                DELL U3421WE
      Product code:         41345  (0xa181)
      Serial number:        8HBB753
      Binary serial number: 809584204 (0x3041464c)
      Manufacture year:     2022,  Week: 25
   VCP version:         2.1
"""