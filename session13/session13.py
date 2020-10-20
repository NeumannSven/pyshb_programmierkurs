# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Session 13", pos = wx.DefaultPosition, size = wx.Size( 547,450 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_genericDirCtrl1 = wx.GenericDirCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.DIRCTRL_3D_INTERNAL|wx.SUNKEN_BORDER, wx.EmptyString, 0 )

		self.m_genericDirCtrl1.ShowHidden( False )
		bSizer1.Add( self.m_genericDirCtrl1, 1, wx.EXPAND |wx.ALL, 5 )

		gSizer1 = wx.GridSizer( 0, 3, 0, 0 )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Parameter 1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		gSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )

		self.m_textCtrlParam1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_textCtrlParam1, 0, wx.ALL, 5 )

		self.m_buttonSet = wx.Button( self, wx.ID_ANY, u"set", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_buttonSet, 0, wx.ALL, 5 )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Parameter 2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		gSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.m_filePicker1 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		gSizer1.Add( self.m_filePicker1, 0, wx.ALL, 5 )


		bSizer1.Add( gSizer1, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menuFile = wx.Menu()
		self.m_menueFileNew = wx.MenuItem( self.m_menuFile, wx.ID_ANY, u"New", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuFile.Append( self.m_menueFileNew )

		self.m_menuFileSave = wx.MenuItem( self.m_menuFile, wx.ID_ANY, u"Save", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuFile.Append( self.m_menuFileSave )

		self.m_menuFileExit = wx.MenuItem( self.m_menuFile, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuFile.Append( self.m_menuFileExit )

		self.m_menubar1.Append( self.m_menuFile, u"File" )

		self.SetMenuBar( self.m_menubar1 )

		self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_buttonSet.Bind( wx.EVT_BUTTON, self.doButtonSet )
		self.Bind( wx.EVT_MENU, self.doFileNew, id = self.m_menueFileNew.GetId() )
		self.Bind( wx.EVT_MENU, self.doFileSave, id = self.m_menuFileSave.GetId() )
		self.Bind( wx.EVT_MENU, self.doFileExit, id = self.m_menuFileExit.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def doButtonSet( self, event ):
		event.Skip()

	def doFileNew( self, event ):
		event.Skip()

	def doFileSave( self, event ):
		event.Skip()

	def doFileExit( self, event ):
		event.Skip()


