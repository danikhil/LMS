import mysql.connector
import datetime


class student:
    def __init__(self, mydb):
        self.__mydb = mydb
        self.window = None

    def createStudent(self, Id, Name):
        self.__stdId = Id
        self.__stdName = Name

        mycursor = self.__mydb.cursor()
        sql = "INSERT INTO `student`(`Id`, `Name`) VALUES (%s, %s)"
        val = (self.__stdId, self.__stdName)
        mycursor.execute(sql, val)

        self.__mydb.commit()
        self.window.SetStatusText("Student Added Successfully", 1)

    def modifyStudent(self, Id, Name):
        self.__stdId = Id
        self.__stdName = Name

        mycursor = self.__mydb.cursor()
        sql = "UPDATE `student` SET `Name` = %s WHERE `Id` = %s"
        val = (self.__stdName, self.__stdId)
        mycursor.execute(sql, val)

        self.__mydb.commit()
        self.window.SetStatusText("Student Modified Successfully", 1)

    def deleteStudent(self, Id):
        self.__stdId = Id

        mycursor = self.__mydb.cursor()
        sql = "DELETE FROM `student` WHERE `Id` = " + self.__stdId
        mycursor.execute(sql)

        self.__mydb.commit()
        self.window.SetStatusText("Student Deleted Successfully", 1)

    def truncateStudent(self):

        mycursor = self.__mydb.cursor()
        sql = "TRUNCATE TABLE `student`"
        mycursor.execute(sql)

        self.__mydb.commit()

    def issueBook(self, No, Id):

        bookNo = No

        mycursor = self.__mydb.cursor()
        sql = "SELECT `Issued` FROM `book` WHERE `No` =" + bookNo

        mycursor.execute(sql)
        output = mycursor.fetchone()

        if output[0] == 1:
            self.window.SetStatusText("Book is Already Issued", 1)

        else:
            self.__stdId = Id

            date = datetime.date.today()
            mycursor = self.__mydb.cursor()
            sql = "UPDATE `book` SET `Issued` = %s WHERE `No` = %s"
            val = ("1", bookNo)

            mycursor.execute(sql, val)

            sql = "INSERT INTO `issue record`(`Std Id`, `Book No`, `Issue Date`) VALUES (%s, %s, %s)"
            val = (self.__stdId, bookNo, date)

            mycursor.execute(sql, val)

            self.__mydb.commit()
            self.window.SetStatusText("Book Issued Successfully", 1)

    def returnBook(self, No, Id):
        self.__stdId = Id
        bookNo = No

        date = datetime.date.today()
        mycursor = self.__mydb.cursor()
        sql = "UPDATE `issue record` SET `Return Date`=%s WHERE `Std Id`=%s AND `Book No`=%s"
        val = (date, self.__stdId, bookNo)

        mycursor.execute(sql,val)

        sql = "UPDATE `book` SET `Issued`=%s WHERE `No`=%s"
        val = ("0", bookNo)

        mycursor.execute(sql, val)

        self.__mydb.commit()
        self.window.SetStatusText("Book Returned Successfully", 1)
