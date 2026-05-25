# -*- coding: utf-8 -*-
# This file is part of the Horus Project

__author__ = 'Jesús Arroyo Torrens <jesus.arroyo@bq.com>'
__copyright__ = 'Copyright (C) 2014-2016 Mundo Reader S.L.\
                 Copyright (C) 2013 David Braam from Cura Project'
__license__ = 'GNU General Public License v2 http://www.gnu.org/licenses/gpl2.html'

import wx

from horus.util.resources import get_path_for_image


class SplashScreen(wx.Frame):

    def __init__(self, callback):
        self.callback = callback

        bitmap = wx.Image(get_path_for_image("splash.png"), wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        super(SplashScreen, self).__init__(
            None, style=wx.BORDER_NONE | wx.FRAME_NO_TASKBAR | wx.STAY_ON_TOP)

        w, h = bitmap.GetWidth(), bitmap.GetHeight()
        self.SetClientSize((w, h))
        self.Centre()

        panel = wx.StaticBitmap(self, bitmap=bitmap)
        self.Show()
        wx.CallAfter(self.do_callback)

    def do_callback(self):
        try:
            self.callback()
        finally:
            if self:
                self.Destroy()
