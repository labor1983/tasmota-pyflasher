
# coding=utf-8

import sys
import os
import wx
import wx.html
import wx.lib.wxpTag
import webbrowser
from Main import __version__

# ---------------------------------------------------------------------------

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, wx.ID_ANY, "About Tasmota PyFlasher")
        html = HtmlWindow(self, wx.ID_ANY, size=(420, -1))
        if "gtk2" in wx.PlatformInfo or "gtk3" in wx.PlatformInfo:
            html.SetStandardFonts()
        txt = self.text.format(self._get_bundle_dir(), __version__)
        html.SetPage(txt)
        ir = html.GetInternalRepresentation()
        html.SetSize((ir.GetWidth() + 25, ir.GetHeight() + 25))
        self.SetClientSize(html.GetSize())
        self.CentreOnParent(wx.BOTH)

    @staticmethod
    def _get_bundle_dir():
        # set by PyInstaller, see http://pyinstaller.readthedocs.io/en/v3.2/runtime-information.html
        if getattr(sys, 'frozen', False):
            # noinspection PyUnresolvedReferences,PyProtectedMember
            return sys._MEIPASS
        else:
            return os.path.dirname(os.path.abspath(__file__))


class HtmlWindow(wx.html.HtmlWindow):
    def OnLinkClicked(self, link):
        webbrowser.open(link.GetHref())

# ---------------------------------------------------------------------------
