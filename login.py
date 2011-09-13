#!/usr/bin/env python
# -# -*- coding: utf-8 -*-

import pygtk
pygtk.require('2.0')
import gtk

class login:
    def get_window(self):
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_position(gtk.WIN_POS_CENTER_ALWAYS)
        window.connect('destroy', lambda w: gtk.main_quit())
        window.set_title("Ingresar la Sistema")
        window.set_icon_from_file("images/icono.ico")
        window.set_border_width(10)

        vbox = gtk.VBox()
        window.add(vbox)

        lblusuario = gtk.Label("Usuario")
        txtusuario = gtk.Entry()
        lblclave = gtk.Label("Contraseña")
        txtclave = gtk.Entry()
        txtclave.set_visibility(False)
        btnaceptar= gtk.Button("Aceptar")
        vbox.pack_start(lblusuario)
        vbox.pack_start(txtusuario)
        vbox.pack_start(lblclave)
        vbox.pack_start(txtclave)
        vbox.pack_start(btnaceptar)
        window.show_all()
        return window
