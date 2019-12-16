import wx
import json


class IdeenBox(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(1000, 500))

        self.MainSizer = wx.BoxSizer(wx.VERTICAL)

        self.TopSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.IdeenListe = wx.ListCtrl(self, style=wx.LC_REPORT | wx.LC_NO_HEADER)
        self.IdeenListe.InsertColumn(0, "Titel")
        self.TopSizer.Add(self.IdeenListe, 0, wx.ALL | wx.EXPAND)

        self.EintragSizer = wx.BoxSizer(wx.VERTICAL)

        self.EintragKopfSizer = wx.GridSizer(rows=4, cols=2, vgap=5, hgap=5)

        self.TitleStat = wx.StaticText(self, label="Titel")
        self.TitleText = wx.TextCtrl(self)
        self.TagsStat = wx.StaticText(self, label="Tags")
        self.TagsText = wx.TextCtrl(self)
        self.BeschreibungStat = wx.StaticText(self, label="Beschreibung")
        self.BeschreibungText = wx.TextCtrl(self)
        self.FarbeStat = wx.StaticText(self, label="Farbe")
        self.FarbButtonSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.WhiteButton = wx.ToggleButton(self, label="White")
        self.GrayButton = wx.ToggleButton(self, label="Gray")
        self.YellowButton = wx.ToggleButton(self, label="Yellow")
        self.PinkButton = wx.ToggleButton(self, label="Pink")
        self.FarbButtonSizer.Add(self.WhiteButton, 1, wx.ALL | wx.EXPAND)
        self.FarbButtonSizer.Add(self.GrayButton, 1, wx.ALL | wx.EXPAND)
        self.FarbButtonSizer.Add(self.YellowButton, 1, wx.ALL | wx.EXPAND)
        self.FarbButtonSizer.Add(self.PinkButton, 1, wx.ALL | wx.EXPAND)
        self.FarbButtonListe = {"white": self.WhiteButton,
                                "gray": self.GrayButton,
                                "yellow": self.YellowButton,
                                "pink": self.PinkButton}

        self.EintragKopfSizer.Add(self.TitleStat, 0, wx.ALL | wx.EXPAND)
        self.EintragKopfSizer.Add(self.TagsStat, 0, wx.ALL | wx.EXPAND)
        self.EintragKopfSizer.Add(self.TitleText, 1, wx.ALL | wx.EXPAND)
        self.EintragKopfSizer.Add(self.TagsText, 1, wx.ALL | wx.EXPAND)
        self.EintragKopfSizer.Add(self.BeschreibungStat, 0, wx.ALL | wx.EXPAND)
        self.EintragKopfSizer.Add(self.FarbeStat, 0, wx.ALL | wx.EXPAND)
        self.EintragKopfSizer.Add(self.BeschreibungText, 1, wx.ALL | wx.EXPAND)
        self.EintragKopfSizer.Add(self.FarbButtonSizer, 1, wx.ALL | wx.EXPAND)

        self.EintragSizer.Add(self.EintragKopfSizer, 0, wx.ALL | wx.EXPAND)

        self.EintragLangText = wx.TextCtrl(self, style=wx.TE_MULTILINE)

        self.EintragSizer.Add(self.EintragLangText, 1, wx.ALL | wx.EXPAND)

        self.TopSizer.Add(self.EintragSizer, 1, wx.ALL | wx.EXPAND)

        self.BottomSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.PlusButton = wx.Button(self, label="+")
        self.MinusButton = wx.Button(self, label="-")
        self.SaveButton = wx.Button(self, label="Speichern")

        self.BottomSizer.Add(self.PlusButton, 0, wx.ALL)
        self.BottomSizer.Add(self.MinusButton, 0, wx.ALL)
        self.BottomSizer.AddStretchSpacer()
        self.BottomSizer.Add(self.SaveButton, 0, wx.ALL | wx.ALIGN_RIGHT)

        self.MainSizer.Add(self.TopSizer, 1, wx.ALL | wx.EXPAND)
        self.MainSizer.Add(self.BottomSizer, 0, wx.ALL | wx.EXPAND)

        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.showEntry, self.IdeenListe)
        self.Bind(wx.EVT_BUTTON, self.writeJson, self.SaveButton)
        for _, button in self.FarbButtonListe.items():
            self.Bind(wx.EVT_TOGGLEBUTTON, self.toggleColor, button)
        self.Bind(wx.EVT_BUTTON, self.newEntry, self.PlusButton)

        self.NewEntryFlag = False

        self.SetSizer(self.MainSizer)
        self.Show()

        self.readJson(None)

    def readJson(self, event):
        with open("session5/ideen.json") as JsonFile:
            self.IdeenDict = json.load(JsonFile)
            self.updateList(None)

    def writeJson(self, event):
        title = self.TitleText.GetValue()
        if self.NewEntryFlag:
            color = "white"
            for label, button in self.FarbButtonListe.items():
                if button.GetValue():
                    color = label
                    break
            eintrag = {"title": self.TitleText.GetValue(),
                       "tags": self.TagsText.GetValue(),
                       "desc": self.BeschreibungText.GetValue(),
                       "longdesc": self.EintragLangText.GetValue(),
                       "color": color}
            self.IdeenDict["Ideen"].append(eintrag)
            self.NewEntryFlag = False
        elif title:
            for idee in self.IdeenDict["Ideen"]:
                if title == idee["title"]:
                    idee["tags"] = self.TagsText.GetValue()
                    idee["desc"] = self.BeschreibungText.GetValue()
                    idee["longdesc"] = self.EintragLangText.GetValue()
                    for label, button in self.FarbButtonListe.items():
                        if button.GetValue():
                            idee["color"] = label
                            break
                    break
        with open("session5/ideen.json", "w+") as JsonFile:
            json.dump(self.IdeenDict, JsonFile)
        self.readJson(None)

    def updateList(self, event):
        self.IdeenListe.DeleteAllItems()
        for idee in self.IdeenDict["Ideen"]:
            self.IdeenListe.Append([idee["title"]])

    def showEntry(self, event):
        self.NewEntryFlag = False
        for idee in self.IdeenDict["Ideen"]:
            if event.Label == idee["title"]:
                self.TitleText.SetValue(idee["title"])
                self.TagsText.SetValue(idee["tags"])
                self.BeschreibungText.SetValue(idee["desc"])
                self.EintragLangText.SetValue(idee["longdesc"])
                for label, button in self.FarbButtonListe.items():
                    if label == idee["color"]:
                        button.SetValue(True)
                    else:
                        button.SetValue(False)
                break

    def toggleColor(self, event):
        for label, button in self.FarbButtonListe.items():
            if not label == event.EventObject.Label.lower():
                button.SetValue(False)

    def newEntry(self, event):
        self.NewEntryFlag = True
        self.TitleText.SetValue("")
        self.TagsText.SetValue("")
        self.BeschreibungText.SetValue("")
        self.EintragLangText.SetValue("")
        for _, button in self.FarbButtonListe.items():
            button.SetValue(False)


app = wx.App()
frame = IdeenBox(None, "Ideen Box")
app.MainLoop()
