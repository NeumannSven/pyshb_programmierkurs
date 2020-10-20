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
        self.res = wx.xrc.XmlResource("ibox.xrc")
        self.frame = self.res.LoadFrame(None, "MyFrame1")
        self.frame.Show()
        return True

        def OnOk(self, event):
                print(event)


if __name__ == "__main__":
    app = MainApp()
    app.MainLoop()

```


## Load Python Datei

```python
import wx
import wx.xrc
import ibox

class MainApp(wx.App):
    def OnInit(self):
        self.mainframe = ibox.MyFrame1(None)
        self.mainframe.Show(True)
        return True

if __name__ == "__main__":
        app = MainApp()
        app.MainLoop()
```


