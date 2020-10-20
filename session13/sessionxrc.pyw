
import wx
import wx.xrc

class MainApp(wx.App):
    def OnInit(self):
        self.res = wx.xrc.XmlResource("session13.xrc")
        self.frame = self.res.LoadFrame(None, "MainFrame")
        self.frame.Show()
        return True


if __name__ == "__main__":
    app = MainApp()
    app.MainLoop()