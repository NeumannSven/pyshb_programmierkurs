# GUI visual Editor



## Installation

https://github.com/wxFormBuilder/wxFormBuilder/releases


```console

>pip install wxwidgets

```

## Load XRC Datei

```python
import wx
import wx.xrc

class MainApp(wx.App):
    def OnInit(self):
        self.res = wx.xrc.XmlResource("session13.xrc")
        self.frame = self.res.LoadFrame(None, "MyFrame")
        self.frame.Show()
        return True

if __name__ == "__main__":
    app = MainApp()
    app.MainLoop()
```


## Load Python Datei

```python
import wx
import session13

class MainApp(wx.App):
    def OnInit(self):
        self.mainframe = session13.MyFrame(None)
        self.mainframe.Show(True)
        return True

if __name__ == "__main__":
        app = MainApp()
        app.MainLoop()
```

## Events

```python
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
```
