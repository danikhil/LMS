# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import mysql.connector
from LOGIN import admin
import wx
import wx.xrc
import MAIN_UI

wx.ID_Window = 1000
wx.ID_Menubar = 1001
wx.ID_Quit = 1002
wx.ID_MainPanel = 1003
wx.ID_AdminTextPanel = 1004
wx.ID_LoginMainPanel = 1005
wx.ID_UserText = 1006
wx.ID_InputUser = 1007
wx.ID_PassText = 1008
wx.ID_InputPass = 1009
wx.ID_LoginBtnPanel = 1010
wx.ID_LoginBtn = 1011

###########################################################################
## Class LoginWindow
###########################################################################

class loginWindow ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_Window, title = u"Library Management System", pos = wx.DefaultPosition, size = wx.Size( 450,400 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

        self.menuBar = wx.MenuBar( 0 )
        self.file = wx.Menu()
        self.file.Append( wx.ID_Quit, "&Quit", wx.EmptyString)

        self.menuBar.Append( self.file, u"File" )

        self.SetMenuBar( self.menuBar )

        verMainBox = wx.BoxSizer( wx.VERTICAL )

        self.mainPanel = wx.Panel( self, wx.ID_MainPanel, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.mainPanel.SetForegroundColour( wx.Colour( 6, 0, 0 ) )
        self.mainPanel.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

        verContBox = wx.BoxSizer( wx.VERTICAL )

        self.adminTextPanel = wx.Panel( self.mainPanel, wx.ID_AdminTextPanel, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.adminTextPanel.SetFont( wx.Font( 16, 72, 90, 90, False, "Constantia" ) )

        adminTextBox = wx.BoxSizer( wx.VERTICAL )


        adminTextBox.Add( 40, 1, wx.EXPAND, 5 )

        self.m_staticText5 = wx.StaticText( self.adminTextPanel, wx.ID_ANY, u"Admin Login", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
        self.m_staticText5.Wrap( -1 )
        self.m_staticText5.SetFont( wx.Font( 16, 72, 90, 90, False, "Constantia" ) )
        self.m_staticText5.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

        adminTextBox.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        adminTextBox.Add( 40, 1, wx.EXPAND, 5 )


        self.adminTextPanel.SetSizer( adminTextBox )
        self.adminTextPanel.Layout()
        adminTextBox.Fit( self.adminTextPanel )
        verContBox.Add( self.adminTextPanel, 1, wx.EXPAND |wx.ALL, 5 )

        loginMainBox = wx.BoxSizer( wx.VERTICAL )

        self.loginMainPanel = wx.Panel( self.mainPanel, wx.ID_LoginMainPanel, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        loginBoxGrid = wx.GridSizer( 2, 2, 0, 25 )

        self.userText = wx.StaticText( self.loginMainPanel, wx.ID_UserText, u"Username", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
        self.userText.Wrap( -1 )
        loginBoxGrid.Add( self.userText, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

        self.inputUser = wx.TextCtrl( self.loginMainPanel, wx.ID_InputUser, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.inputUser.SetMaxLength( 20 )
        loginBoxGrid.Add( self.inputUser, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.passText = wx.StaticText( self.loginMainPanel, wx.ID_PassText, u"Password", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
        self.passText.Wrap( -1 )
        loginBoxGrid.Add( self.passText, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

        self.inputPass = wx.TextCtrl( self.loginMainPanel, wx.ID_InputPass, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
        loginBoxGrid.Add( self.inputPass, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        self.loginMainPanel.SetSizer( loginBoxGrid )
        self.loginMainPanel.Layout()
        loginBoxGrid.Fit( self.loginMainPanel )
        loginMainBox.Add( self.loginMainPanel, 1, wx.EXPAND |wx.ALL, 5 )

        self.loginBtnPanel = wx.Panel( self.mainPanel, wx.ID_LoginBtnPanel, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        loginBtnBox = wx.BoxSizer( wx.VERTICAL )


        loginBtnBox.Add( 0, 1, wx.EXPAND, 5 )

        self.loginBtn = wx.Button( self.loginBtnPanel, wx.ID_LoginBtn, u"Login", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.loginBtn.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

        loginBtnBox.Add( self.loginBtn, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        loginBtnBox.Add( 0, 2, wx.EXPAND, 5 )


        self.loginBtnPanel.SetSizer( loginBtnBox )
        self.loginBtnPanel.Layout()
        loginBtnBox.Fit( self.loginBtnPanel )
        loginMainBox.Add( self.loginBtnPanel, 1, wx.EXPAND |wx.ALL, 5 )


        verContBox.Add( loginMainBox, 2, wx.EXPAND, 5 )


        self.mainPanel.SetSizer( verContBox )
        self.mainPanel.Layout()
        verContBox.Fit( self.mainPanel )
        verMainBox.Add( self.mainPanel, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        self.SetSizer( verMainBox )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        wx.EVT_MENU(self, wx.ID_Quit, self.quit)
        self.loginBtn.Bind( wx.EVT_BUTTON, self.login )

    def __del__( self ):
        pass

    # Virtual event handlers, overide them in your derived class
    def quit( self, event ):
        self.Destroy()

    def login( self, event ):
        Admin = admin(self.inputUser.GetValue(), self.inputPass.GetValue())
        if Admin.getDatabase() != None:
            self.mydb = Admin.getDatabase()
            self.Destroy()
            window = MAIN_UI.mainWindow(None)
            window.db = self.mydb
            window.Show()



class loginError ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Login Error", pos = wx.DefaultPosition, size = wx.Size( 245,169 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

        containerBox = wx.BoxSizer( wx.VERTICAL )


        containerBox.Add ( 0, 2, wx.EXPAND, 5 )

        self.errorInfo = wx.StaticText( self, wx.ID_ANY, u"Incorrect Username or Password\nTry again!", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
        self.errorInfo.Wrap( -1 )
        self.errorInfo.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

        containerBox.Add( self.errorInfo, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        containerBox.Add( 0, 1, wx.EXPAND, 5 )

        self.okBtn = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
        containerBox.Add( self.okBtn, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        containerBox.Add( 0, 2, wx.EXPAND, 5 )


        self.SetSizer( containerBox )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.okBtn.Bind( wx.EVT_BUTTON, self.OnExit )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def OnExit( self, event ):
        self.Destroy()

