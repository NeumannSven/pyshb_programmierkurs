import wx
import session13


class Frame(session13.MainFrame):
    def doButtonSet( self, event ):
        self.m_textCtrlParam1.SetValue("Hallo Welt!")

    
    def doFileExit( self, event ):
        self.Destroy()



class MainApp(wx.App):
    def OnInit(self):
        self.mainframe = Frame(None)
        self.mainframe.Show(True)
        return True

if __name__ == "__main__":
        app = MainApp()
        app.MainLoop()

