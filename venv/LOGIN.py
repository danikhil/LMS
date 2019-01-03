import mysql.connector
import getpass
import LOGIN_UI
import wx

class admin:
    def __init__(self, user, pswd):
        try:
            self.__mydb = mysql.connector.connect(
                host="localhost",
                user=user,
                passwd=pswd,
                database="library"
            )
        except:
            dialog = LOGIN_UI.loginError(None)
            dialog.ShowModal()

    def getDatabase(self):
        try:
            return self.__mydb
        except:
            return None
