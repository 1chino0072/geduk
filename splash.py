#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygtk
pygtk.require('2.0')
import gtk
import gobject

class Splash:
    
    def close_application(self, widget, event, data=None):
        gtk.main_quit()
        return gtk.FALSE

    def __init__(self):
        
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_position(gtk.WIN_POS_CENTER_ALWAYS)
        self.window.connect("delete_event", self.close_application)
        self.window.set_title("Bienvenido")
        self.window.set_icon_from_file("icono.ico")
        self.window.set_decorated(True)

        vbox = gtk.VBox()
        vbox.show()
        self.window.add(vbox)

        image = gtk.Image()
        image.set_from_file("splash.png")
        image.show()
        vbox.pack_start(image)

        self.pbar = gtk.ProgressBar()
        self.pbar.show()
        self.pbar.set_pulse_step(0.01)
        self.pbar.set_text("Ingresando al sistema espere por favor")
        vbox.pack_start(self.pbar)
        self.window.show_all()
        
        gobject.timeout_add(25,self.aumentar_progreso)

    def aumentar_progreso(self):
        if self.pbar.get_fraction() >= 0.99:
            self.pbar.set_text("Bienvenido al Sistema de Gestion Educativa GEDUK")
            self.window.hide()
            import login
            ventana_login = login.login().get_window()
            ventana_login.show_all()
            
            return False
        else:
            self.pbar.set_fraction(self.pbar.get_fraction() + 0.01)
            return True

    def main(self):
        gtk.main()
        return 0

if __name__ == "__main__":
    splash = Splash()
    splash.main()
