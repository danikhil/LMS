# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

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
wx.ID_Logout = 1012
wx.ID_TextPanel = 1013
wx.ID_IssuePanel = 1014
wx.ID_IssueBook = 1015
wx.ID_ReturnBook = 1016
wx.ID_CreateBook = 1017
wx.ID_CreateStudent = 1018
wx.ID_ModifyBook = 1019
wx.ID_FetchallBook = 1020
wx.ID_fetchallStudent = 1021
wx.ID_DeleteBook = 1022
wx.ID_DeleteStudent = 1023
wx.ID_TruncateBook = 1024
wx.ID_TruncateStudent = 1025
wx.ID_Statusbar = 1026

###########################################################################
## Class loginWindow
###########################################################################

class loginWindow ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_Window, title = u"Library Management System", pos = wx.DefaultPosition, size = wx.Size( 491,393 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		
		self.menuBar = wx.MenuBar( 0 )
		self.file = wx.Menu()
		self.quit = wx.MenuItem( self.file, wx.ID_Quit, u"Quit", wx.EmptyString, wx.ITEM_NORMAL )
		self.file.AppendItem( self.quit )
		
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
		
		
		adminTextBox.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText5 = wx.StaticText( self.adminTextPanel, wx.ID_ANY, u"Admin Login", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText5.Wrap( -1 )
		self.m_staticText5.SetFont( wx.Font( 16, 72, 90, 90, False, "Constantia" ) )
		self.m_staticText5.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		adminTextBox.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		adminTextBox.AddSpacer( ( 0, 40), 1, wx.EXPAND, 5 )
		
		
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
		
		
		loginBtnBox.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.loginBtn = wx.Button( self.loginBtnPanel, wx.ID_LoginBtn, u"Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.loginBtn.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
		
		loginBtnBox.Add( self.loginBtn, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		loginBtnBox.AddSpacer( ( 0, 0), 2, wx.EXPAND, 5 )
		
		
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
		self.Bind( wx.EVT_MENU, self.quit, id = self.quit.GetId() )
		self.loginBtn.Bind( wx.EVT_BUTTON, self.login )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def quit( self, event ):
		event.Skip()
	
	def login( self, event ):
		event.Skip()
	

###########################################################################
## Class loginError
###########################################################################

class loginError ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Login Error", pos = wx.DefaultPosition, size = wx.Size( 245,169 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		
		containerBox = wx.BoxSizer( wx.VERTICAL )
		
		
		containerBox.AddSpacer( ( 0, 0), 2, wx.EXPAND, 5 )
		
		self.errorInfo = wx.StaticText( self, wx.ID_ANY, u"Incorrect Username or Password\nTry again!", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.errorInfo.Wrap( -1 )
		self.errorInfo.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		
		containerBox.Add( self.errorInfo, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		containerBox.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.okBtn = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		containerBox.Add( self.okBtn, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		containerBox.AddSpacer( ( 0, 0), 2, wx.EXPAND, 5 )
		
		
		self.SetSizer( containerBox )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class mainWindow
###########################################################################

class mainWindow ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Library Management System", pos = wx.DefaultPosition, size = wx.Size( 566,437 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )
		
		self.menuBar = wx.MenuBar( 0 )
		self.file = wx.Menu()
		self.logout = wx.MenuItem( self.file, wx.ID_Logout, u"Logout", wx.EmptyString, wx.ITEM_NORMAL )
		self.file.AppendItem( self.logout )
		
		self.menuBar.Append( self.file, u"File" ) 
		
		self.SetMenuBar( self.menuBar )
		
		mainBox = wx.BoxSizer( wx.VERTICAL )
		
		self.textPanel = wx.Panel( self, wx.ID_TextPanel, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		textBox = wx.BoxSizer( wx.VERTICAL )
		
		self.text = wx.StaticText( self.textPanel, wx.ID_ANY, u"Library Management System", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text.Wrap( -1 )
		self.text.SetFont( wx.Font( 16, 74, 90, 92, False, wx.EmptyString ) )
		self.text.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_CAPTIONTEXT ) )
		
		textBox.Add( self.text, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.textPanel.SetSizer( textBox )
		self.textPanel.Layout()
		textBox.Fit( self.textPanel )
		mainBox.Add( self.textPanel, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.IssuePanel = wx.Panel( self, wx.ID_IssuePanel, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer3 = wx.GridSizer( 1, 2, 0, 0 )
		
		self.issueBookBtn = wx.Button( self.IssuePanel, wx.ID_IssueBook, u"Issue Book", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.issueBookBtn, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.returnBookBtn = wx.Button( self.IssuePanel, wx.ID_ReturnBook, u"Return Book", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.returnBookBtn, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.IssuePanel.SetSizer( gSizer3 )
		self.IssuePanel.Layout()
		gSizer3.Fit( self.IssuePanel )
		mainBox.Add( self.IssuePanel, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.mainPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gridBox = wx.GridSizer( 5, 2, 0, 0 )
		
		self.createBookBtn = wx.Button( self.mainPanel, wx.ID_CreateBook, u"Add New Book", wx.DefaultPosition, wx.DefaultSize, 0 )
		gridBox.Add( self.createBookBtn, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.createStudentBtn = wx.Button( self.mainPanel, wx.ID_CreateStudent, u"Add New Student", wx.DefaultPosition, wx.DefaultSize, 0 )
		gridBox.Add( self.createStudentBtn, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.modifyBookBtn = wx.Button( self.mainPanel, wx.ID_ModifyBook, u"Update Book Details", wx.DefaultPosition, wx.DefaultSize, 0 )
		gridBox.Add( self.modifyBookBtn, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.modifyStudentBtn = wx.Button( self.mainPanel, wx.ID_ModifyBook, u"Update Student Details", wx.DefaultPosition, wx.DefaultSize, 0 )
		gridBox.Add( self.modifyStudentBtn, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.fetchallBookBtn = wx.Button( self.mainPanel, wx.ID_FetchallBook, u"View All Books", wx.DefaultPosition, wx.DefaultSize, 0 )
		gridBox.Add( self.fetchallBookBtn, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.fetchallStudentBtn = wx.Button( self.mainPanel, wx.ID_fetchallStudent, u"View All Student", wx.DefaultPosition, wx.DefaultSize, 0 )
		gridBox.Add( self.fetchallStudentBtn, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.deleteBookBtn = wx.Button( self.mainPanel, wx.ID_DeleteBook, u"Remove Book", wx.DefaultPosition, wx.DefaultSize, 0 )
		gridBox.Add( self.deleteBookBtn, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.deleteStudentBtn = wx.Button( self.mainPanel, wx.ID_DeleteStudent, u"Remove Student", wx.DefaultPosition, wx.DefaultSize, 0 )
		gridBox.Add( self.deleteStudentBtn, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.trucateBookBtn = wx.Button( self.mainPanel, wx.ID_TruncateBook, u"Clear Book Record", wx.DefaultPosition, wx.DefaultSize, 0 )
		gridBox.Add( self.trucateBookBtn, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.trucateStudentBtn = wx.Button( self.mainPanel, wx.ID_TruncateStudent, u"Clear Student Record", wx.DefaultPosition, wx.DefaultSize, 0 )
		gridBox.Add( self.trucateStudentBtn, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.mainPanel.SetSizer( gridBox )
		self.mainPanel.Layout()
		gridBox.Fit( self.mainPanel )
		mainBox.Add( self.mainPanel, 6, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( mainBox )
		self.Layout()
		self.statusBar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_Statusbar )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_MENU, self.logout, id = self.logout.GetId() )
		self.issueBookBtn.Bind( wx.EVT_BUTTON, self.issueBook )
		self.returnBookBtn.Bind( wx.EVT_BUTTON, self.returnBook )
		self.createBookBtn.Bind( wx.EVT_BUTTON, self.createBook )
		self.createStudentBtn.Bind( wx.EVT_BUTTON, self.createStudent )
		self.modifyBookBtn.Bind( wx.EVT_BUTTON, self.modifyBook )
		self.modifyStudentBtn.Bind( wx.EVT_BUTTON, self.modifyStudent )
		self.fetchallBookBtn.Bind( wx.EVT_BUTTON, self.fetchallBook )
		self.fetchallStudentBtn.Bind( wx.EVT_BUTTON, self.fetchallStudent )
		self.deleteBookBtn.Bind( wx.EVT_BUTTON, self.deleteBook )
		self.deleteStudentBtn.Bind( wx.EVT_BUTTON, self.deleteStudent )
		self.trucateBookBtn.Bind( wx.EVT_BUTTON, self.truncateBook )
		self.trucateStudentBtn.Bind( wx.EVT_BUTTON, self.truncateStudent )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def logout( self, event ):
		event.Skip()
	
	def issueBook( self, event ):
		event.Skip()
	
	def returnBook( self, event ):
		event.Skip()
	
	def createBook( self, event ):
		event.Skip()
	
	def createStudent( self, event ):
		event.Skip()
	
	def modifyBook( self, event ):
		event.Skip()
	
	def modifyStudent( self, event ):
		event.Skip()
	
	def fetchallBook( self, event ):
		event.Skip()
	
	def fetchallStudent( self, event ):
		event.Skip()
	
	def deleteBook( self, event ):
		event.Skip()
	
	def deleteStudent( self, event ):
		event.Skip()
	
	def truncateBook( self, event ):
		event.Skip()
	
	def truncateStudent( self, event ):
		event.Skip()
	

###########################################################################
## Class addBookDialog
###########################################################################

class addBookDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Add Book", pos = wx.DefaultPosition, size = wx.Size( 326,199 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer4 = wx.GridSizer( 1, 2, 0, 0 )
		
		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		gSizer4.Add( self.m_staticText8, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.m_textCtrl4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer9.Add( gSizer4, 1, wx.EXPAND, 5 )
		
		gSizer5 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		gSizer5.Add( self.m_staticText9, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.m_textCtrl5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer9.Add( gSizer5, 1, wx.EXPAND, 5 )
		
		gSizer6 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		gSizer6.Add( self.m_staticText10, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl6 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.m_textCtrl6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer9.Add( gSizer6, 1, wx.EXPAND, 5 )
		
		bSizer11 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button16 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_button16, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer9.Add( bSizer11, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer9 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

