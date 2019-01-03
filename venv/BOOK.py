import mysql.connector

class book:
    def __init__(self, mydb):
        self.__mydb = mydb
        self.window = None

    def createBook(self, No, Name, Author):
        self.__issued = 0
        self.__bookNo = No
        self.__bookName = Name
        self.__bookAuthor = Author

        mycursor = self.__mydb.cursor()
        sql = "INSERT INTO `book`(`No`, `Name`, `Author`, `Issued`) VALUES (%s, %s, %s, %s)"
        val = (self.__bookNo, self.__bookName, self.__bookAuthor, self.__issued)
        mycursor.execute(sql, val)

        self.__mydb.commit()
        self.window.SetStatusText("Book Added Successfully", 1)

    def fetchall(self):
        mycursor = self.__mydb.cursor()
        sql = "SELECT * FROM `book`"
        mycursor.execute(sql)

        output = mycursor.fetchall()

        print("Book No.\t\tName\t\tAuthor\t\tIssued")
        for row in output:
            print(str(row[0])+'\t\t'+row[1]+'\t\t'+row[2]+'\t\t'+str(bool(row[3])))


    def modifyBook(self, No, Name, Author, Issued):
        self.__bookNo = No
        self.__bookName = Name
        self.__bookAuthor = Author
        self.__issued = Issued

        mycursor = self.__mydb.cursor()
        sql = "UPDATE `book` SET `Name` = %s, `Author` = %s, `Issued`= %s WHERE `No` = %s"
        val = (self.__bookName, self.__bookAuthor, self.__issued, self.__bookNo)
        mycursor.execute(sql, val)

        self.__mydb.commit()
        self.window.SetStatusText("Book Modified Successfully", 1)

    def deleteBook(self, No):
        self.__bookNo = No

        mycursor = self.__mydb.cursor()
        sql = "DELETE FROM `book` WHERE `No` =" + self.__bookNo
        mycursor.execute(sql)

        self.__mydb.commit()
        self.window.SetStatusText("Book Deleted Successfully", 1)

    def truncateBook(self):

        mycursor = self.__mydb.cursor()
        sql = "TRUNCATE TABLE `book`"
        mycursor.execute(sql)

        self.__mydb.commit()

