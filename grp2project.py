#!/usr/bin/env python
#Group 2
#Eric La Rue
#Tina Stahlstedt
#Yong Lee

import curses
import MySQLdb 

# Init screen with global var:
screen = curses.initscr()
#curses.noecho()
#curses.cbreak()
#screen.keypad(1)
screen.border(0)


#Show Tables
def showT():
  screen.clear()
  screen.border(0)
  screen.refresh()
  
  line = 4
  x = 1  
  
  cursor = db.cursor()
  cursor.execute('SHOW TABLES')
  data = cursor.fetchall()
  results = []

  for row in data :
    results.append(row[0])  

  # print
  for item in results :
    screen.addstr(line, 4, str(x))
    screen.addstr(line, 8, item)
    line += 1
    x += 1
    
  screen.addstr(2, 2, 'Table in this database (Press any key to go back): ')
  screen.refresh()
  screen.getch()
  
  

#Show Data
def showD():
  c = 'y'
  
  while c != ord('n'):
    screen.clear()
    screen.border(0)
    screen.refresh()
    
    screen.addstr(2, 2, 'Enter The Name Of The Table You Wish To See: ')
    screen.refresh()
    x = screen.getstr()
    
    try:
      line = 4
      column = 4
      n = 1  
      
      cursor = db.cursor()
      cursor.execute('SELECT * from ' + x)
      db.commit()

      desc = cursor.description
            
      w = 0
            
      for des in desc:
        screen.addstr(line, column, desc[w][0])
        column += 20
        w = w+1
        
      nrow = cursor.rowcount
      line += 2
      column = 4
      
      for a in range(0, nrow):
        rows = cursor.fetchone()
        ncol = len(rows)
        for a in range(0, ncol):
          screen.addstr(line, column, str(rows[a]))
          column += 20
        column = 4
        line += 1
      
    except:
      db.rollback()
      screen.addstr(5, 2, "Invalid Query!\n")    

    screen.addstr(line + 1, 2, 'See Another? (press n to go back) :')
    screen.refresh()
    c = screen.getch()
    


#Add Table
def addT():
  c = 'y'
  
  while c != ord('n'):
    screen.clear()
    screen.border(0)
    screen.refresh()
    
    screen.addstr(2, 2, 'Enter Your Query Here (e.g CREATE TABLE Persons (PersonID int, LastName varchar(255)) : ')
    screen.refresh()
    x = screen.getstr()
    
    try:
      cursor = db.cursor()
      cursor.execute(x)
      db.commit()
      screen.addstr(5, 2, 'Query Successful!')
      
    except:
      db.rollback()
      screen.addstr(5, 2, "Invalid Query!\n")    

    screen.addstr(7, 2, 'Another Query? (press n to go back) :')
    screen.refresh()
    c = screen.getch()
 
 
    
#Delete Table
def deleteT():
  c = 'y'
  
  while c != ord('n'):
    screen.clear()
    screen.border(0)
    screen.refresh()
    
    screen.addstr(2, 2, 'Enter The Name Of The Table You Wish To Delete: ')
    screen.refresh()
    x = screen.getstr()
    
    try:
      cursor = db.cursor()
      cursor.execute('DROP TABLE ' + x)
      db.commit()
      screen.addstr(5, 2, 'Delete Successful!')
      
    except:
      db.rollback()
      screen.addstr(5, 2, "Invalid Query!\n")    

    screen.addstr(7, 2, 'Another Delete? (press n to go back) :')
    screen.refresh()
    c = screen.getch()
    
    
    
#Truncate Table
def truncateT():
  c = 'y'
  
  while c != ord('n'):
    screen.clear()
    screen.border(0)
    screen.refresh()
    
    screen.addstr(2, 2, 'Enter The Name Of The Table You Wish To Truncate: ')
    screen.refresh()
    x = screen.getstr()
    
    try:
      cursor = db.cursor()
      cursor.execute('TRUNCATE TABLE ' + x)
      db.commit()
      screen.addstr(5, 2, 'Truncate Successful!')
      
    except:
      db.rollback()
      screen.addstr(5, 2, "Invalid Query!\n")    

    screen.addstr(7, 2, 'Another Truncate? (press n to go back) :')
    screen.refresh()
    c = screen.getch()
    
    

#See Tables
def seeT():
  c = 'y'
  
  while c != ord('n'):
    screen.clear()
    screen.border(0)
    screen.refresh()
    
    screen.addstr(2, 2, 'Enter The Name Of The Table You Wish To See In More Detail: ')
    screen.refresh()
    x = screen.getstr()
    
    try:
      line = 4
      column = 4
      n = 1  
      
      cursor = db.cursor()
      cursor.execute('DESC ' + x)
      db.commit()

      desc = cursor.description
            
      w = 0
           
      for des in desc:
        screen.addstr(line, column, desc[w][0])
        column += 20
        w = w+1
       
      nrow = cursor.rowcount
      line += 2
      column = 4
      
      for a in range(0, nrow):
        rows = cursor.fetchone()
        ncol = len(rows)
        for a in range(0, ncol):
          screen.addstr(line, column, str(rows[a]))
          column += 20
        column = 4
        line += 1
      
    except:
      db.rollback()
      screen.addstr(line+1, 2, "Invalid Query!\n")    

    screen.addstr(line+3, 2, 'See Another? (press n to go back) :')
    screen.refresh()
    c = screen.getch()  
  
  
  
#Rename Table
def renameTa():
  c = 'y'
  
  while c != ord('n'):
    screen.clear()
    screen.border(0)
    screen.refresh()
    
    screen.addstr(2, 2, 'Enter The Name Of The Table You Wish To Rename: ')
    screen.refresh()
    x = screen.getstr()
    
    screen.addstr(3, 2, 'Enter New Name: ')
    screen.refresh()
    y = screen.getstr()
    
    try:
      cursor = db.cursor()
      cursor.execute('ALTER TABLE ' + x + ' RENAME TO ' + y)
      db.commit()
      screen.addstr(5, 2, 'Rename Successful!')
      
    except:
      db.rollback()
      screen.addstr(5, 2, "Invalid Query!\n")    

    screen.addstr(7, 2, 'Another Rename? (press n to go back) :')
    screen.refresh()
    c = screen.getch()
    
    

#Rename Column
def renameCo():
  c = 'y'
  
  while c != ord('n'):
    screen.clear()
    screen.border(0)
    screen.refresh()
    
    screen.addstr(2, 2, 'Enter The Name Of The Table: ')
    screen.refresh()
    x = screen.getstr()
    
    screen.addstr(3, 2, 'Enter The Name Of The Column You Wish To Change: ')
    screen.refresh()
    y = screen.getstr()

    screen.addstr(4, 2, 'Enter New Name And Column Definition (e.g. New_Name varchar(50)): ')
    screen.refresh()
    z = screen.getstr()
    
    try:
      cursor = db.cursor()
      cursor.execute('ALTER TABLE ' + x + ' CHANGE ' + y + ' ' + z)
      db.commit()
      screen.addstr(5, 2, 'Rename Successful!')
      
    except:
      db.rollback()
      screen.addstr(5, 2, "Invalid Query!\n")    

    screen.addstr(7, 2, 'Another Rename? (press n to go back) :')
    screen.refresh()
    c = screen.getch()
    
    

#Add Column
def addCo():
  c = 'y'
  
  while c != ord('n'):
    screen.clear()
    screen.border(0)
    screen.refresh()
    
    screen.addstr(2, 2, 'Enter The Name Of The Table: ')
    screen.refresh()
    x = screen.getstr()
    
    screen.addstr(3, 2, 'Enter The Name Of The Column You Wish To Add: ')
    screen.refresh()
    y = screen.getstr()

    screen.addstr(4, 2, 'Enter Column-Definition (e.g. VARCHAR(20)): ')
    screen.refresh()
    z = screen.getstr()
    
    try:
      cursor = db.cursor()
      cursor.execute('ALTER TABLE ' + x + ' ADD ' + y + ' ' + z)
      db.commit()
      screen.addstr(5, 2, 'Add Successful!')
      
    except:
      db.rollback()
      screen.addstr(5, 2, "Invalid Query!\n")    

    screen.addstr(7, 2, 'Another Add? (press n to go back) :')
    screen.refresh()
    c = screen.getch()
    
    
    
#Delete Column
def deleteCo():
  c = 'y'
  
  while c != ord('n'):
    screen.clear()
    screen.border(0)
    screen.refresh()
    
    screen.addstr(2, 2, 'Enter The Name Of The Table: ')
    screen.refresh()
    x = screen.getstr()
    
    screen.addstr(3, 2, 'Enter The Name Of The Column You Wish To Delete: ')
    screen.refresh()
    y = screen.getstr()
    
    try:
      cursor = db.cursor()
      cursor.execute('ALTER TABLE ' + x + ' DROP COLUMN ' + y)
      db.commit()
      screen.addstr(5, 2, 'Delete Successful!')
      
    except:
      db.rollback()
      screen.addstr(5, 2, "Invalid Query!\n")    

    screen.addstr(7, 2, 'Another Delete? (press n to go back) :')
    screen.refresh()
    c = screen.getch()
    
    

#Modify Column
def modifyCo():
  c = 'y'
  
  while c != ord('n'):
    screen.clear()
    screen.border(0)
    screen.refresh()
    
    screen.addstr(2, 2, 'Enter The Name Of The Table: ')
    screen.refresh()
    x = screen.getstr()
    
    screen.addstr(3, 2, 'Enter The Name Of The Column You Wish To Modify: ')
    screen.refresh()
    y = screen.getstr()

    screen.addstr(4, 2, 'Enter New Column-Definition (e.g. VARCHAR(20) not null) - Do Not Change Type (e.g. From Varchar to Int): ')
    screen.refresh()
    z = screen.getstr()
    
    try:
      cursor = db.cursor()
      cursor.execute('ALTER TABLE ' + x + ' MODIFY ' + y + ' ' + z)
      db.commit()
      screen.addstr(5, 2, 'Modify Successful!')
      
    except:
      db.rollback()
      screen.addstr(5, 2, "Invalid Query!\n")    

    screen.addstr(7, 2, 'Another Modify? (press n to go back) :')
    screen.refresh()
    c = screen.getch()
    
    
    
#Alter Table
def alterT():
  screen.clear()
  screen.border(0)
  screen.refresh()
  c = 0
  
  while c != ord('9'):
    
    screen.addstr(4, 4, "1")
    screen.addstr(4, 8, "Rename Table")
  
    screen.addstr(5, 4, "2")
    screen.addstr(5, 8, "Rename Column")
  
    screen.addstr(6, 4, "3")
    screen.addstr(6, 8, "Add Column")
  
    screen.addstr(7, 4, "4")
    screen.addstr(7, 8, "Delete Column")
    
    screen.addstr(8, 4, "5")
    screen.addstr(8, 8, "Modify Column")
    
    screen.addstr(9, 4, "6")
    screen.addstr(9, 8, "Show Tables")
  
    screen.addstr(10, 4, "7")
    screen.addstr(10, 8, "Show Rows In A Table")
    
    screen.addstr(11, 4, "8")
    screen.addstr(11, 8, "See Table Definition")
    
    screen.addstr(12, 4, "9")
    screen.addstr(12, 8, "Go Back")
  
  
    # draw the list on the screen  
    screen.addstr(2, 2, 'What do you want to do? ')
    screen.refresh()
    c = screen.getch() 
    
    if c == ord('1'):
      renameTa()
      screen.clear()
      
    if c == ord('2'):
      renameCo()
      screen.clear()
      
    if c == ord('3'):
      addCo()
      screen.clear()
      
    if c == ord('4'):
      deleteCo()
      screen.clear()
      
    if c == ord('5'):
      modifyCo()
      screen.clear()
      
    if c == ord('6'):
      showT()
      screen.clear()
      
    if c == ord('7'):
      showD()
      screen.clear()

    if c == ord('8'):
      seeT()
      screen.clear()
    
  
   
#Table Page
def tablePage():
  c = 0
  
  while c != ord('8'):
    screen.clear()
    screen.border(0)
    screen.refresh()
    
    screen.addstr(4, 4, "1")
    screen.addstr(4, 8, "Show Tables")
  
    screen.addstr(5, 4, "2")
    screen.addstr(5, 8, "Show Rows In A Table")
  
    screen.addstr(6, 4, "3")
    screen.addstr(6, 8, "Add Table")
  
    screen.addstr(7, 4, "4")
    screen.addstr(7, 8, "Delete Table")
    
    screen.addstr(8, 4, "5")
    screen.addstr(8, 8, "Delete All Rows In A Table")
    
    screen.addstr(9, 4, "6")
    screen.addstr(9, 8, "Alter Table")
    
    screen.addstr(10, 4, "7")
    screen.addstr(10, 8, "See Table Definition")
  
    screen.addstr(11, 4, "8")
    screen.addstr(11, 8, "Go Back")
  
    # draw the list on the screen  
    screen.addstr(2, 2, 'What do you want to do? ')
    screen.refresh()
    c = screen.getch() 
    
    if c == ord('1'):
      showT()
      screen.clear()
      
    if c == ord('2'):
      showD()
      screen.clear()
      
    if c == ord('3'):
      addT()
      screen.clear()
      
    if c == ord('4'):
      deleteT()
      screen.clear()
      
    if c == ord('5'):
      truncateT()
      screen.clear()
  
    if c == ord('6'):
      alterT()
      screen.clear()
  
    if c == ord('7'):
      seeT()
      screen.clear()




#Search Database
def qData():
  c = 'y'
  
  while c != ord('n'):
    screen.clear()
    screen.border(0)
    screen.refresh()
    
    screen.addstr(2, 2, "Enter Your Whole Query Here (e.g INSERT INTO CUSTOMERS VALUES (7, 'Muffy', 10000.00 )) : ")
    screen.refresh()
    x = screen.getstr()
    
    try:
      cursor = db.cursor()
      cursor.execute(x)
      db.commit()
      screen.addstr(5, 2, 'Query Successful!')
      
    except:
      db.rollback()
      screen.addstr(5, 2, "Invalid Query!\n")    

    screen.addstr(7, 2, 'Another Query? (press n to go back) : ')
    screen.refresh()
    c = screen.getch()

    
    

    


#Data Page
def dataPage():
  c = 0
  
  while c != ord('4'):
    screen.clear()
    screen.border(0)
    screen.refresh()
    
    screen.addstr(4, 4, "1")
    screen.addstr(4, 8, "Show Tables")
  
    screen.addstr(5, 4, "2")
    screen.addstr(5, 8, "Show Data In A Table")
  
    screen.addstr(6, 4, "3")
    screen.addstr(6, 8, "Enter Query")
  
    screen.addstr(7, 4, "4")
    screen.addstr(7, 8, "Go Back")
  
    # draw the list on the screen  
    screen.addstr(2, 2, 'What do you want to do? ')
    screen.refresh()
    c = screen.getch() 
    
    if c == ord('1'):
      showT()
      screen.clear()
      
    if c == ord('2'):
      showD()
      screen.clear()
      
    if c == ord('3'):
      qData()
      screen.clear()

      
   

#Search Database
def searchData():
  c = 'y'
  
  while c != ord('n'):
    screen.clear()
    screen.border(0)
    screen.refresh()
    
    screen.addstr(2, 2, 'Enter Your Search Query Here (e.g. SELECT CustomerName,City FROM Customers) : ')
    screen.refresh()
    x = screen.getstr()
    
    try:
      line = 4
      column = 4
      n = 1  
      
      cursor = db.cursor()
      cursor.execute(x)
      db.commit()

      desc = cursor.description
            
      w = 0
            
      for des in desc:
        screen.addstr(line, column, desc[w][0])
        column += 20
        w = w+1
        
      nrow = cursor.rowcount
      line += 2
      column = 4
      
      for a in range(0, nrow):
        rows = cursor.fetchone()
        ncol = len(rows)
        for a in range(0, ncol):
          screen.addstr(line, column, str(rows[a]))
          column += 20
        column = 4
        line += 1
      
    except:
      db.rollback()
      screen.addstr(5, 2, "Invalid Query!\n")    

    screen.addstr(line + 1, 2, 'Search Another? (press n to go back) :')
    screen.refresh()
    c = screen.getch()
    

    
    
    

#Selct Screen after Home Screen
def selectPage():
  c = 0
  while c != ord('4'):
    screen.clear()
    screen.border(0)
    screen.refresh()
  
    screen.addstr(4, 4, "1")
    screen.addstr(4, 8, "Tables")
  
    screen.addstr(5, 4, "2")
    screen.addstr(5, 8, "Data")
  
    screen.addstr(6, 4, "3")
    screen.addstr(6, 8, "Search")
  
    screen.addstr(7, 4, "4")
    screen.addstr(7, 8, "Go Back to Change Database or Quit")

    
    # draw the list on the screen  
    screen.addstr(2, 2, 'What do you want to do? ')
    screen.refresh()
    c = screen.getch() 

    if c == ord('1'):
      tablePage()
      screen.clear()
      
    if c == ord('2'):
      dataPage()
      screen.clear()
      
    if c == ord('3'):
      searchData()
      screen.clear()



# Init screen with global var:
screen = curses.initscr()
#curses.noecho()
#curses.cbreak()
screen.keypad(1)
screen.border(0)
  

#Get info to connect to MySql
screen.addstr(2, 2, 'Enter The Hostname: ')
hostN = screen.getstr()
  
screen.addstr(4, 2, 'Enter The Username: ')
userN = screen.getstr()
  
screen.addstr(6, 2, 'Enter The Password: ')
passW = screen.getstr()
screen.refresh()

db = MySQLdb.connect(host=hostN, user=userN, passwd=passW)



  

while(1):
  screen.clear()
  screen.border(0)
  screen.refresh()

  line = 6
  x = 1
  # prepare a cursor object using cursor() method
  cursor = db.cursor()
  cursor.execute('SHOW DATABASES')
  
  # fetch all of the rows from the query
  data = cursor.fetchall()
  results = []
  
  # move data to array
  for row in data :
    results.append(row[0])  
  
  # print list
  for item in results :
    screen.addstr(line, 4, str(x))
    screen.addstr(line, 8, item)
    line += 1
    x += 1
  # draw the list on the screen  
  screen.addstr(2, 2, 'Type In The Name Of The Database To Use? (Enter quit to exit) ')
  #screen.refresh()
  x = screen.getstr()
  
  if (x == "quit"):
    break
  try:
    cursor = db.cursor()
    cursor.execute('use ' + x)
    db.commit()
    screen.clear()
    selectPage()
          
  except:
    db.rollback()
 
 
#exit gracefully
screen.keypad(0)
curses.echo()
curses.nocbreak()
screen.clear()
curses.endwin()