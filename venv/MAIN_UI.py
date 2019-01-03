# -*- coding: utf-8 -*-
import wx
import wx.xrc
import wx.grid
import LOGIN_UI
import mysql.connector
import datetime
from BOOK import book
from STUDENT import student

wx.ID_Menubar = 1000
wx.ID_Logout = 1001
wx.ID_TextPanel = 1002
wx.ID_IssuePanel = 1003
wx.ID_IssueBook = 1004
wx.ID_ReturnBook = 1005
wx.ID_CreateBook = 1006
wx.ID_CreateStudent = 1007
wx.ID_ModifyBook = 1008
wx.ID_FetchallBook = 1009
wx.ID_fetchallStudent = 1010
wx.ID_DeleteBook = 1011
wx.ID_DeleteStudent = 1012
wx.ID_TruncateBook = 1013
wx.ID_TruncateStudent = 1014
wx.ID_Statusbar = 1015
wx.ID_History = 1016

###########################################################################
## Class mainWindow
###########################################################################

class mainWindow ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Library Management System", pos = wx.DefaultPosition, size = wx.Size( 566,437 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

        self.menuBar = wx.MenuBar( 0 )
        self.file = wx.Menu()
        self.history = wx.Menu()
        self.file.Append( wx.ID_Logout, "&Logout", wx.EmptyString)
        self.history.Append( wx.ID_History, "&Issue History", wx.EmptyString)

        self.menuBar.Append( self.file, u"File" )
        self.menuBar.Append( self.history, u"History" )

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
        self.statusBar = self.CreateStatusBar( 2, wx.STB_SIZEGRIP, wx.ID_Statusbar )
        self.SetStatusText("Admin Logged In")

        self.Centre( wx.BOTH )

        self.db = None

        # Connect Events
        wx.EVT_MENU(self, wx.ID_History, self.viewHistory )
        wx.EVT_MENU(self, wx.ID_Logout, self.logout )
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
        self.Destroy()
        window = LOGIN_UI.loginWindow(None)
        window.Show()

    def issueBook( self, event ):
        dialog = issueBookDialog(None)
        dialog.db = self.db
        dialog.window = self
        self.SetStatusText("Issusing Book", 1)
        dialog.ShowModal()

    def returnBook( self, event ):
        dialog = returnBookDialog(None)
        dialog.db = self.db
        dialog.window = self
        self.SetStatusText("Returning Book", 1)
        dialog.ShowModal()

    def createBook( self, event ):
        dialog = addBookDialog(None)
        dialog.db = self.db
        dialog.window = self
        self.SetStatusText("Adding Book", 1)
        dialog.ShowModal()

    def createStudent( self, event ):
        dialog = addStudentDialog(None)
        dialog.db = self.db
        dialog.window = self
        self.SetStatusText("Adding Student", 1)
        dialog.ShowModal()

    def modifyBook( self, event ):
        dialog = modifyBookDialog(None)
        dialog.db = self.db
        dialog.window = self
        self.SetStatusText("Updating Book Details", 1)
        dialog.ShowModal()

    def modifyStudent( self, event ):
        dialog = modifyStudentDialog(None)
        dialog.db = self.db
        dialog.window = self
        self.SetStatusText("Updating Student Details", 1)
        dialog.ShowModal()

    def fetchallBook( self, event ):
        dialog = bookRecordDialog(None)
        dialog.db = self.db
        dialog.window = self
        self.SetStatusText("Displaying Records", 1)
        dialog.ShowModal()

    def viewHistory(self, event):
        dialog = issueRecordDialog(None)
        dialog.window = self
        self.SetStatusText("Displaying Records", 1)
        dialog.ShowModal()

    def fetchallStudent( self, event ):
        dialog = studentRecordDialog(None)
        dialog.db = self.db
        dialog.window = self
        self.SetStatusText("Displaying Records", 1)
        dialog.ShowModal()

    def deleteBook( self, event ):
        dialog = deleteBookDialog(None)
        dialog.db = self.db
        dialog.window = self
        self.SetStatusText("Deleting Book", 1)
        dialog.ShowModal()

    def deleteStudent( self, event ):
        dialog = deleteStudentDialog(None)
        dialog.db = self.db
        dialog.window = self
        self.SetStatusText("Deleting Student", 1)
        dialog.ShowModal()

    def truncateBook( self, event ):
        B = book(self.db)
        self.SetStatusText("Book Records Resetted Succesfully", 1)
        B.truncateBook()

    def truncateStudent( self, event ):
        S = student(self.db)
        self.SetStatusText("Student Records Resetted Succesfully", 1)
        S.truncateStudent()


wx.ID_Submit = 1016

###########################################################################
## Class addBookDialog
###########################################################################

class addBookDialog ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Add Book", pos = wx.DefaultPosition, size = wx.Size( 326,199 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

        mainBox = wx.BoxSizer( wx.VERTICAL )

        inputBox1 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer141 = wx.BoxSizer( wx.VERTICAL )

        self.bookNo = wx.StaticText( self, wx.ID_ANY, u"Book No.", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.bookNo.Wrap( -1 )
        bSizer141.Add( self.bookNo, 0, wx.ALL, 5 )


        inputBox1.Add( bSizer141, 1, wx.ALIGN_CENTER_VERTICAL, 5 )

        bSizer151 = wx.BoxSizer( wx.VERTICAL )

        self.inputBookNo = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.inputBookNo.SetMaxLength( 9 )
        bSizer151.Add( self.inputBookNo, 1, wx.ALL|wx.EXPAND, 5 )


        inputBox1.Add( bSizer151, 3, wx.ALIGN_CENTER_VERTICAL, 5 )


        mainBox.Add( inputBox1, 1, wx.EXPAND, 5 )

        inputBox2 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer1411 = wx.BoxSizer( wx.VERTICAL )

        self.bookName = wx.StaticText( self, wx.ID_ANY, u"Book Name", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.bookName.Wrap( -1 )
        bSizer1411.Add( self.bookName, 0, wx.ALL, 5 )


        inputBox2.Add( bSizer1411, 1, wx.ALIGN_CENTER_VERTICAL, 5 )

        bSizer1511 = wx.BoxSizer( wx.VERTICAL )

        self.inputBookName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.inputBookName.SetMaxLength( 20 )
        bSizer1511.Add( self.inputBookName, 0, wx.ALL|wx.EXPAND, 5 )


        inputBox2.Add( bSizer1511, 3, wx.ALIGN_CENTER_VERTICAL, 5 )


        mainBox.Add( inputBox2, 1, wx.EXPAND, 5 )

        inputBox3 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer14111 = wx.BoxSizer( wx.VERTICAL )

        self.bookAuthor = wx.StaticText( self, wx.ID_ANY, u"Book Author", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.bookAuthor.Wrap( -1 )
        bSizer14111.Add( self.bookAuthor, 0, wx.ALL, 5 )


        inputBox3.Add( bSizer14111, 1, wx.ALIGN_CENTER_VERTICAL, 5 )

        bSizer15111 = wx.BoxSizer( wx.VERTICAL )

        self.inputBookAuthor = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.inputBookAuthor.SetMaxLength( 20 )
        bSizer15111.Add( self.inputBookAuthor, 0, wx.ALL|wx.EXPAND, 5 )


        inputBox3.Add( bSizer15111, 3, wx.ALIGN_CENTER_VERTICAL, 5 )


        mainBox.Add( inputBox3, 1, wx.EXPAND, 5 )

        submitBox = wx.BoxSizer( wx.VERTICAL )

        self.submitBtn = wx.Button( self, wx.ID_Submit, u"Submit", wx.DefaultPosition, wx.DefaultSize, 0 )
        submitBox.Add( self.submitBtn, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        mainBox.Add( submitBox, 1, wx.EXPAND, 5 )


        self.SetSizer( mainBox )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.submitBtn.Bind( wx.EVT_BUTTON, self.createBook )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def createBook( self, event ):
        B = book(self.db)
        B.window = self.window
        B.createBook(self.inputBookNo.GetValue(), self.inputBookName.GetValue(), self.inputBookAuthor.GetValue())
        self.Destroy()



###########################################################################
## Class addStudentDialog
###########################################################################

class addStudentDialog ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Add Student", pos = wx.DefaultPosition, size = wx.Size( 360,199 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

        mainBox = wx.BoxSizer( wx.VERTICAL )

        inputBox1 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer141 = wx.BoxSizer( wx.VERTICAL )

        self.stdId = wx.StaticText( self, wx.ID_ANY, u"Student ID", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.stdId.Wrap( -1 )
        bSizer141.Add( self.stdId, 0, wx.ALL, 5 )


        inputBox1.Add( bSizer141, 1, wx.ALIGN_CENTER_VERTICAL, 5 )

        bSizer151 = wx.BoxSizer( wx.VERTICAL )

        self.inputStdId = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.inputStdId.SetMaxLength( 9 )
        bSizer151.Add( self.inputStdId, 1, wx.ALL|wx.EXPAND, 5 )


        inputBox1.Add( bSizer151, 3, wx.ALIGN_CENTER_VERTICAL, 5 )


        mainBox.Add( inputBox1, 1, wx.EXPAND, 5 )

        inputBox2 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer1411 = wx.BoxSizer( wx.VERTICAL )

        self.stdName = wx.StaticText( self, wx.ID_ANY, u"Student Name", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.stdName.Wrap( -1 )
        bSizer1411.Add( self.stdName, 0, wx.ALL, 5 )


        inputBox2.Add( bSizer1411, 1, wx.ALIGN_CENTER_VERTICAL, 5 )

        bSizer1511 = wx.BoxSizer( wx.VERTICAL )

        self.inputStdName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.inputStdName.SetMaxLength( 20 )
        bSizer1511.Add( self.inputStdName, 0, wx.ALL|wx.EXPAND, 5 )


        inputBox2.Add( bSizer1511, 3, wx.ALIGN_CENTER_VERTICAL, 5 )


        mainBox.Add( inputBox2, 1, wx.EXPAND, 5 )

        submitBox = wx.BoxSizer( wx.VERTICAL )

        self.submitBtn = wx.Button( self, wx.ID_Submit, u"Submit", wx.DefaultPosition, wx.DefaultSize, 0 )
        submitBox.Add( self.submitBtn, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        mainBox.Add( submitBox, 1, wx.EXPAND, 5 )


        self.SetSizer( mainBox )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.submitBtn.Bind( wx.EVT_BUTTON, self.createStudent )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def createStudent( self, event ):
        S = student(self.db)
        S.window = self.window
        S.createStudent(self.inputStdId.GetValue(), self.inputStdName.GetValue())
        self.Destroy()

###########################################################################
## Class deleteStudent
###########################################################################

class deleteStudentDialog ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Delete Student", pos = wx.DefaultPosition, size = wx.Size( 254,141 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

        mainBox = wx.BoxSizer( wx.VERTICAL )

        inputBox1 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer141 = wx.BoxSizer( wx.VERTICAL )

        self.stdId = wx.StaticText( self, wx.ID_ANY, u"Student ID", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.stdId.Wrap( -1 )
        bSizer141.Add( self.stdId, 0, wx.ALL, 5 )


        inputBox1.Add( bSizer141, 1, wx.ALIGN_CENTER_VERTICAL, 5 )

        bSizer151 = wx.BoxSizer( wx.VERTICAL )

        self.inputStdId = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.inputStdId.SetMaxLength( 9 )
        bSizer151.Add( self.inputStdId, 1, wx.ALL|wx.EXPAND, 5 )


        inputBox1.Add( bSizer151, 3, wx.ALIGN_CENTER_VERTICAL, 5 )


        mainBox.Add( inputBox1, 2, wx.EXPAND, 5 )

        submitBox = wx.BoxSizer( wx.VERTICAL )

        self.submitBtn = wx.Button( self, wx.ID_Submit, u"Submit", wx.DefaultPosition, wx.DefaultSize, 0 )
        submitBox.Add( self.submitBtn, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        mainBox.Add( submitBox, 1, wx.EXPAND, 5 )


        self.SetSizer( mainBox )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.submitBtn.Bind( wx.EVT_BUTTON, self.deleteStudent )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def deleteStudent( self, event ):
        S = student(self.db)
        S.window = self.window
        S.deleteStudent(self.inputStdId.GetValue())
        self.Destroy()


###########################################################################
## Class deleteBookDialog
###########################################################################

class deleteBookDialog ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Delete Book", pos = wx.DefaultPosition, size = wx.Size( 267,181 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

        mainBox = wx.BoxSizer( wx.VERTICAL )

        inputBox1 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer141 = wx.BoxSizer( wx.VERTICAL )

        self.bookNo = wx.StaticText( self, wx.ID_ANY, u"Book No.", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.bookNo.Wrap( -1 )
        bSizer141.Add( self.bookNo, 0, wx.ALL, 5 )


        inputBox1.Add( bSizer141, 1, wx.ALIGN_CENTER_VERTICAL, 5 )

        bSizer151 = wx.BoxSizer( wx.VERTICAL )

        self.inputBookNo = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.inputBookNo.SetMaxLength( 9 )
        bSizer151.Add( self.inputBookNo, 1, wx.ALL|wx.EXPAND, 5 )


        inputBox1.Add( bSizer151, 3, wx.ALIGN_CENTER_VERTICAL, 5 )


        mainBox.Add( inputBox1, 2, wx.EXPAND, 5 )

        submitBox = wx.BoxSizer( wx.VERTICAL )

        self.submitBtn = wx.Button( self, wx.ID_Submit, u"Submit", wx.DefaultPosition, wx.DefaultSize, 0 )
        submitBox.Add( self.submitBtn, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        mainBox.Add( submitBox, 1, wx.EXPAND, 5 )


        self.SetSizer( mainBox )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.submitBtn.Bind( wx.EVT_BUTTON, self.deleteBook )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def deleteBook( self, event ):
        B = book(self.db)
        B.window = self.window
        B.deleteBook(self.inputBookNo.GetValue())
        self.Destroy()


###########################################################################
## Class modifyBookDialog
###########################################################################

class modifyBookDialog ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Update Book Details", pos = wx.DefaultPosition, size = wx.Size( 326,199 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

        mainBox = wx.BoxSizer( wx.VERTICAL )

        inputBox1 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer141 = wx.BoxSizer( wx.VERTICAL )

        self.bookNo = wx.StaticText( self, wx.ID_ANY, u"Book No.", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.bookNo.Wrap( -1 )
        bSizer141.Add( self.bookNo, 0, wx.ALL, 5 )


        inputBox1.Add( bSizer141, 1, wx.ALIGN_CENTER_VERTICAL, 5 )

        bSizer151 = wx.BoxSizer( wx.VERTICAL )

        self.inputBookNo = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.inputBookNo.SetMaxLength( 9 )
        bSizer151.Add( self.inputBookNo, 1, wx.ALL|wx.EXPAND, 5 )


        inputBox1.Add( bSizer151, 3, wx.ALIGN_CENTER_VERTICAL, 5 )


        mainBox.Add( inputBox1, 1, wx.EXPAND, 5 )

        inputBox2 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer1411 = wx.BoxSizer( wx.VERTICAL )

        self.bookName = wx.StaticText( self, wx.ID_ANY, u"Book Name", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.bookName.Wrap( -1 )
        bSizer1411.Add( self.bookName, 0, wx.ALL, 5 )


        inputBox2.Add( bSizer1411, 1, wx.ALIGN_CENTER_VERTICAL, 5 )

        bSizer1511 = wx.BoxSizer( wx.VERTICAL )

        self.inputBookName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.inputBookName.SetMaxLength( 20 )
        bSizer1511.Add( self.inputBookName, 0, wx.ALL|wx.EXPAND, 5 )


        inputBox2.Add( bSizer1511, 3, wx.ALIGN_CENTER_VERTICAL, 5 )


        mainBox.Add( inputBox2, 1, wx.EXPAND, 5 )

        inputBox3 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer14111 = wx.BoxSizer( wx.VERTICAL )

        self.bookAuthor = wx.StaticText( self, wx.ID_ANY, u"Book Author", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.bookAuthor.Wrap( -1 )
        bSizer14111.Add( self.bookAuthor, 0, wx.ALL, 5 )


        inputBox3.Add( bSizer14111, 1, wx.ALIGN_CENTER_VERTICAL, 5 )

        bSizer15111 = wx.BoxSizer( wx.VERTICAL )

        self.inputBookAuthor = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.inputBookAuthor.SetMaxLength( 20 )
        bSizer15111.Add( self.inputBookAuthor, 0, wx.ALL|wx.EXPAND, 5 )


        inputBox3.Add( bSizer15111, 3, wx.ALIGN_CENTER_VERTICAL, 5 )


        mainBox.Add( inputBox3, 1, wx.EXPAND, 5 )

        inputBox31 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer141111 = wx.BoxSizer( wx.VERTICAL )

        self.issueStatus = wx.StaticText( self, wx.ID_ANY, u"Issued", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.issueStatus.Wrap( -1 )
        bSizer141111.Add( self.issueStatus, 0, wx.ALL, 5 )


        inputBox31.Add( bSizer141111, 1, wx.ALIGN_CENTER_VERTICAL, 5 )

        bSizer151111 = wx.BoxSizer( wx.VERTICAL )

        self.inputIssueStatus = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.inputIssueStatus.SetMaxLength( 20 )
        bSizer151111.Add( self.inputIssueStatus, 0, wx.ALL|wx.EXPAND, 5 )


        inputBox31.Add( bSizer151111, 3, wx.ALIGN_CENTER_VERTICAL, 5 )


        mainBox.Add( inputBox31, 1, wx.EXPAND, 5 )

        submitBox = wx.BoxSizer( wx.VERTICAL )

        self.submitBtn = wx.Button( self, wx.ID_Submit, u"Submit", wx.DefaultPosition, wx.DefaultSize, 0 )
        submitBox.Add( self.submitBtn, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        mainBox.Add( submitBox, 1, wx.EXPAND, 5 )


        self.SetSizer( mainBox )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.submitBtn.Bind( wx.EVT_BUTTON, self.modifyBook )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def modifyBook( self, event ):
        B = book(self.db)
        B.window = self.window
        B.modifyBook(self.inputBookNo.GetValue(), self.inputBookName.GetValue(), self.inputBookAuthor.GetValue(), self.inputIssueStatus.GetValue())
        self.Destroy()


###########################################################################
## Class modifyStudentDialog
###########################################################################

class modifyStudentDialog ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Update Student Details", pos = wx.DefaultPosition, size = wx.Size( 360,199 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

        mainBox = wx.BoxSizer( wx.VERTICAL )

        inputBox1 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer141 = wx.BoxSizer( wx.VERTICAL )

        self.stdId = wx.StaticText( self, wx.ID_ANY, u"Student ID", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.stdId.Wrap( -1 )
        bSizer141.Add( self.stdId, 0, wx.ALL, 5 )


        inputBox1.Add( bSizer141, 1, wx.ALIGN_CENTER_VERTICAL, 5 )

        bSizer151 = wx.BoxSizer( wx.VERTICAL )

        self.inputStdId = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.inputStdId.SetMaxLength( 9 )
        bSizer151.Add( self.inputStdId, 1, wx.ALL|wx.EXPAND, 5 )


        inputBox1.Add( bSizer151, 3, wx.ALIGN_CENTER_VERTICAL, 5 )


        mainBox.Add( inputBox1, 1, wx.EXPAND, 5 )

        inputBox2 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer1411 = wx.BoxSizer( wx.VERTICAL )

        self.stdName = wx.StaticText( self, wx.ID_ANY, u"Student Name", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.stdName.Wrap( -1 )
        bSizer1411.Add( self.stdName, 0, wx.ALL, 5 )


        inputBox2.Add( bSizer1411, 1, wx.ALIGN_CENTER_VERTICAL, 5 )

        bSizer1511 = wx.BoxSizer( wx.VERTICAL )

        self.inputStdName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.inputStdName.SetMaxLength( 20 )
        bSizer1511.Add( self.inputStdName, 0, wx.ALL|wx.EXPAND, 5 )


        inputBox2.Add( bSizer1511, 3, wx.ALIGN_CENTER_VERTICAL, 5 )


        mainBox.Add( inputBox2, 1, wx.EXPAND, 5 )

        submitBox = wx.BoxSizer( wx.VERTICAL )

        self.submitBtn = wx.Button( self, wx.ID_Submit, u"Submit", wx.DefaultPosition, wx.DefaultSize, 0 )
        submitBox.Add( self.submitBtn, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        mainBox.Add( submitBox, 1, wx.EXPAND, 5 )


        self.SetSizer( mainBox )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.submitBtn.Bind( wx.EVT_BUTTON, self.modifyStudent )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def modifyStudent(self, event):
        S = student(self.db)
        S.window = self.window
        S.modifyStudent(self.inputStdId.GetValue(), self.inputStdName.GetValue())
        self.Destroy()

###########################################################################
## Class issueBookDialog
###########################################################################

class issueBookDialog ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Issue Book", pos = wx.DefaultPosition, size = wx.Size( 279,168 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

        mainBox = wx.BoxSizer( wx.VERTICAL )

        inputBox1 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer141 = wx.BoxSizer( wx.VERTICAL )

        self.bookNo = wx.StaticText( self, wx.ID_ANY, u"Book No.", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.bookNo.Wrap( -1 )
        bSizer141.Add( self.bookNo, 0, wx.ALL, 5 )


        inputBox1.Add( bSizer141, 1, wx.ALIGN_CENTER_VERTICAL, 5 )

        bSizer151 = wx.BoxSizer( wx.VERTICAL )

        self.inputBookNo = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.inputBookNo.SetMaxLength( 9 )
        bSizer151.Add( self.inputBookNo, 1, wx.ALL|wx.EXPAND, 5 )


        inputBox1.Add( bSizer151, 3, wx.ALIGN_CENTER_VERTICAL, 5 )


        mainBox.Add( inputBox1, 1, wx.EXPAND, 5 )

        inputBox3 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer14111 = wx.BoxSizer( wx.VERTICAL )

        self.stdId = wx.StaticText( self, wx.ID_ANY, u"Student Id", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.stdId.Wrap( -1 )
        bSizer14111.Add( self.stdId, 0, wx.ALL, 5 )


        inputBox3.Add( bSizer14111, 1, wx.ALIGN_CENTER_VERTICAL, 5 )

        bSizer15111 = wx.BoxSizer( wx.VERTICAL )

        self.inputStudentId = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.inputStudentId.SetMaxLength( 20 )
        bSizer15111.Add( self.inputStudentId, 0, wx.ALL|wx.EXPAND, 5 )


        inputBox3.Add( bSizer15111, 3, wx.ALIGN_CENTER_VERTICAL, 5 )


        mainBox.Add( inputBox3, 1, wx.EXPAND, 5 )

        submitBox = wx.BoxSizer( wx.VERTICAL )

        self.submitBtn = wx.Button( self, wx.ID_Submit, u"Submit", wx.DefaultPosition, wx.DefaultSize, 0 )
        submitBox.Add( self.submitBtn, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        mainBox.Add( submitBox, 1, wx.EXPAND, 5 )


        self.SetSizer( mainBox )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.submitBtn.Bind( wx.EVT_BUTTON, self.issueBook )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def issueBook( self, event ):
        S = student(self.db)
        S.window = self.window
        S.issueBook(self.inputBookNo.GetValue(), self.inputStudentId.GetValue())
        self.Destroy()


###########################################################################
## Class returnBookDialog
###########################################################################

class returnBookDialog ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Return Book", pos = wx.DefaultPosition, size = wx.Size( 279,168 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

        mainBox = wx.BoxSizer( wx.VERTICAL )

        inputBox1 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer141 = wx.BoxSizer( wx.VERTICAL )

        self.bookNo = wx.StaticText( self, wx.ID_ANY, u"Book No.", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.bookNo.Wrap( -1 )
        bSizer141.Add( self.bookNo, 0, wx.ALL, 5 )


        inputBox1.Add( bSizer141, 1, wx.ALIGN_CENTER_VERTICAL, 5 )

        bSizer151 = wx.BoxSizer( wx.VERTICAL )

        self.inputBookNo = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.inputBookNo.SetMaxLength( 9 )
        bSizer151.Add( self.inputBookNo, 1, wx.ALL|wx.EXPAND, 5 )


        inputBox1.Add( bSizer151, 3, wx.ALIGN_CENTER_VERTICAL, 5 )


        mainBox.Add( inputBox1, 1, wx.EXPAND, 5 )

        inputBox3 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer14111 = wx.BoxSizer( wx.VERTICAL )

        self.studentdId = wx.StaticText( self, wx.ID_ANY, u"Student Id", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.studentdId.Wrap( -1 )
        bSizer14111.Add( self.studentdId, 0, wx.ALL, 5 )


        inputBox3.Add( bSizer14111, 1, wx.ALIGN_CENTER_VERTICAL, 5 )

        bSizer15111 = wx.BoxSizer( wx.VERTICAL )

        self.inputStudentId = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.inputStudentId.SetMaxLength( 20 )
        bSizer15111.Add( self.inputStudentId, 0, wx.ALL|wx.EXPAND, 5 )


        inputBox3.Add( bSizer15111, 3, wx.ALIGN_CENTER_VERTICAL, 5 )


        mainBox.Add( inputBox3, 1, wx.EXPAND, 5 )

        submitBox = wx.BoxSizer( wx.VERTICAL )

        self.submitBtn = wx.Button( self, wx.ID_Submit, u"Submit", wx.DefaultPosition, wx.DefaultSize, 0 )
        submitBox.Add( self.submitBtn, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        mainBox.Add( submitBox, 1, wx.EXPAND, 5 )


        self.SetSizer( mainBox )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.submitBtn.Bind( wx.EVT_BUTTON, self.returnBook )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def returnBook( self, event ):
        S = student(self.db)
        S.window = self.window
        S.returnBook(self.inputBookNo.GetValue(), self.inputStudentId.GetValue())
        self.Destroy()

###########################################################################
## Class studentRecordDialog
###########################################################################

class studentRecordDialog ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Student Records", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

        mainBox = wx.BoxSizer( wx.VERTICAL )

        self.textPanel = wx.Panel( self, wx.ID_TextPanel, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        textBox = wx.BoxSizer( wx.VERTICAL )

        self.text = wx.StaticText( self.textPanel, wx.ID_ANY, u"Student Records", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.text.Wrap( -1 )
        self.text.SetFont( wx.Font( 16, 74, 90, 92, False, wx.EmptyString ) )
        self.text.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_CAPTIONTEXT ) )

        textBox.Add( self.text, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        self.textPanel.SetSizer( textBox )
        self.textPanel.Layout()
        textBox.Fit( self.textPanel )
        mainBox.Add( self.textPanel, 0, wx.EXPAND |wx.ALL, 5 )

        studentTable = wx.GridSizer( 0, 3, 0, 0 )

        self.sno = wx.StaticText( self, wx.ID_ANY, u"S No.", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.sno.Wrap( -1 )
        studentTable.Add( self.sno, 1, wx.ALL, 5 )

        self.stdId = wx.StaticText( self, wx.ID_ANY, u"Std Id", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.stdId.Wrap( -1 )
        studentTable.Add( self.stdId, 1, wx.ALL, 5 )

        self.name = wx.StaticText( self, wx.ID_ANY, u"Std Name", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.name.Wrap( -1 )
        studentTable.Add( self.name, 1, wx.ALL, 5 )


        db = LOGIN_UI.admin("root","").getDatabase()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM student")

        data = cursor.fetchall()

        c=0

        for row in data:
            c+=1
            self.one = wx.StaticText( self, wx.ID_ANY, str(c), wx.DefaultPosition, wx.DefaultSize, 1 )
            self.one.Wrap( -1 )
            studentTable.Add( self.one, 1, wx.ALL, 5 )
            self.two = wx.StaticText( self, wx.ID_ANY, str(row[0]), wx.DefaultPosition, wx.DefaultSize, 1 )
            self.two.Wrap( -1 )
            studentTable.Add( self.two, 1, wx.ALL, 5 )
            self.three = wx.StaticText( self, wx.ID_ANY, str(row[1]), wx.DefaultPosition, wx.DefaultSize, 1 )
            self.three.Wrap( -1 )
            studentTable.Add( self.three, 1, wx.ALL, 5 )

        mainBox.Add( studentTable, 1, wx.EXPAND, 5 )


        self.SetSizer( mainBox )
        self.Layout()
        mainBox.Fit( self )

        self.Centre( wx.BOTH )

def __del__( self ):
    pass

###########################################################################
## Class bookRecordDialog
###########################################################################

class bookRecordDialog ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Book Records", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

        mainBox = wx.BoxSizer( wx.VERTICAL )

        self.textPanel = wx.Panel( self, wx.ID_TextPanel, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        textBox = wx.BoxSizer( wx.VERTICAL )

        self.text = wx.StaticText( self.textPanel, wx.ID_ANY, u"Book Records", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.text.Wrap( -1 )
        self.text.SetFont( wx.Font( 16, 74, 90, 92, False, wx.EmptyString ) )
        self.text.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_CAPTIONTEXT ) )

        textBox.Add( self.text, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        self.textPanel.SetSizer( textBox )
        self.textPanel.Layout()
        textBox.Fit( self.textPanel )
        mainBox.Add( self.textPanel, 0, wx.EXPAND |wx.ALL, 5 )

        studentTable = wx.GridSizer( 0, 5, 0, 0 )

        self.sno = wx.StaticText( self, wx.ID_ANY, u"S No.", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.sno.Wrap( -1 )
        studentTable.Add( self.sno, 0, wx.ALL, 5 )

        self.bookNo = wx.StaticText( self, wx.ID_ANY, u"Book No.", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.bookNo.Wrap( -1 )
        studentTable.Add( self.bookNo, 1, wx.ALL, 5 )

        self.name = wx.StaticText( self, wx.ID_ANY, u"Book Name", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.name.Wrap( -1 )
        studentTable.Add( self.name, 1, wx.ALL, 5 )

        self.author = wx.StaticText( self, wx.ID_ANY, u"Author", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.author.Wrap( -1 )
        studentTable.Add( self.author, 1, wx.ALL, 5 )

        self.status = wx.StaticText( self, wx.ID_ANY, u"Issued", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.status.Wrap( -1 )
        studentTable.Add( self.status, 1, wx.ALL, 5 )

        db = LOGIN_UI.admin("root","").getDatabase()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM book")

        data = cursor.fetchall()

        c=0

        for row in data:
            c+=1
            self.one = wx.StaticText( self, wx.ID_ANY, str(c), wx.DefaultPosition, wx.DefaultSize, 1 )
            self.one.Wrap( -1 )
            studentTable.Add( self.one, 1, wx.ALL, 5 )
            self.two = wx.StaticText( self, wx.ID_ANY, str(row[0]), wx.DefaultPosition, wx.DefaultSize, 1 )
            self.two.Wrap( -1 )
            studentTable.Add( self.two, 1, wx.ALL, 5 )
            self.three = wx.StaticText( self, wx.ID_ANY, str(row[1]), wx.DefaultPosition, wx.DefaultSize, 1 )
            self.three.Wrap( -1 )
            studentTable.Add( self.three, 1, wx.ALL, 5 )
            self.four = wx.StaticText( self, wx.ID_ANY, str(row[2]), wx.DefaultPosition, wx.DefaultSize, 1 )
            self.four.Wrap( -1 )
            studentTable.Add( self.four, 1, wx.ALL, 5 )
            self.five = wx.StaticText( self, wx.ID_ANY, str(row[3]), wx.DefaultPosition, wx.DefaultSize, 1 )
            self.five.Wrap( -1 )
            studentTable.Add( self.five, 1, wx.ALL, 5 )

        mainBox.Add( studentTable, 1, wx.EXPAND, 5 )


        self.SetSizer( mainBox )
        self.Layout()
        mainBox.Fit( self )

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass

###########################################################################
## Class issueRecordDialog
###########################################################################

class issueRecordDialog ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Issue Records", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

        mainBox = wx.BoxSizer( wx.VERTICAL )

        self.textPanel = wx.Panel( self, wx.ID_TextPanel, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        textBox = wx.BoxSizer( wx.VERTICAL )

        self.text = wx.StaticText( self.textPanel, wx.ID_ANY, u"Issue Records", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.text.Wrap( -1 )
        self.text.SetFont( wx.Font( 16, 74, 90, 92, False, wx.EmptyString ) )
        self.text.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_CAPTIONTEXT ) )

        textBox.Add( self.text, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        self.textPanel.SetSizer( textBox )
        self.textPanel.Layout()
        textBox.Fit( self.textPanel )
        mainBox.Add( self.textPanel, 0, wx.EXPAND |wx.ALL, 5 )

        studentTable = wx.GridSizer( 0, 5, 0, 0 )

        self.sno = wx.StaticText( self, wx.ID_ANY, u"S No.", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.sno.Wrap( -1 )
        studentTable.Add( self.sno, 0, wx.ALL, 5 )

        self.stdId = wx.StaticText( self, wx.ID_ANY, u"Std. Id", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.stdId.Wrap( -1 )
        studentTable.Add( self.stdId, 1, wx.ALL, 5 )

        self.bookNo = wx.StaticText( self, wx.ID_ANY, u"Book No.", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.bookNo.Wrap( -1 )
        studentTable.Add( self.bookNo, 1, wx.ALL, 5 )

        self.issueDate = wx.StaticText( self, wx.ID_ANY, u"Issue Date", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.issueDate.Wrap( -1 )
        studentTable.Add( self.issueDate, 1, wx.ALL, 5 )

        self.returnDate = wx.StaticText( self, wx.ID_ANY, u"Return Date", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.returnDate.Wrap( -1 )
        studentTable.Add( self.returnDate, 1, wx.ALL, 5 )


        db = LOGIN_UI.admin("root","").getDatabase()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM `issue record`")

        data = cursor.fetchall()

        c=0

        for row in data:
            c+=1
            self.one = wx.StaticText( self, wx.ID_ANY, str(c), wx.DefaultPosition, wx.DefaultSize, 1 )
            self.one.Wrap( -1 )
            studentTable.Add( self.one, 1, wx.ALL, 5 )
            self.two = wx.StaticText( self, wx.ID_ANY, str(row[0]), wx.DefaultPosition, wx.DefaultSize, 1 )
            self.two.Wrap( -1 )
            studentTable.Add( self.two, 1, wx.ALL, 5 )
            self.three = wx.StaticText( self, wx.ID_ANY, str(row[1]), wx.DefaultPosition, wx.DefaultSize, 1 )
            self.three.Wrap( -1 )
            studentTable.Add( self.three, 1, wx.ALL, 5 )
            self.four = wx.StaticText( self, wx.ID_ANY, str(row[2]), wx.DefaultPosition, wx.DefaultSize, 1 )
            self.four.Wrap( -1 )
            studentTable.Add( self.four, 1, wx.ALL, 5 )
            self.five = wx.StaticText( self, wx.ID_ANY, str(row[3]), wx.DefaultPosition, wx.DefaultSize, 1 )
            self.five.Wrap( -1 )
            studentTable.Add( self.five, 1, wx.ALL, 5 )


        mainBox.Add( studentTable, 1, wx.EXPAND, 5 )


        self.SetSizer( mainBox )
        self.Layout()
        mainBox.Fit( self )

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass



