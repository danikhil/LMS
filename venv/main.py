import mysql.connector
import LOGIN_UI
import wx
from BOOK import book
from STUDENT import student
from LOGIN import admin

if __name__ == '__main__':
    app = wx.App()
    window = LOGIN_UI.loginWindow(None)
    window.Show(True)
    app.MainLoop()
