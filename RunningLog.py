"""Running Log

Scott Sikorski
University of Rochester Undergraduate '23
May 2020
Terminal based running log application

Features include:
Calendar using graphics.py that displays non-interactive run data.
Adding runs that are then stored in a .txt file.
Runs are sorted from oldest to newest.
Finding your longest run by distance.
Editing a run based on its date.

I created this project in about 15 hours of work as a side project because
I was bored during lockdown. I learnt Python during my Spring 2020 semester
at the University of Rochester. As well, this was created between second
semester ending and beginning summer work. I'm also a runner at the 
University of Rochester so I thought that this would be a good idea.
First time dedicating an extended amount of time to create a big project
that hasn't been assigned as school work. Turnt out pretty well and had some 
stumps especially with the sorting method but have been able to get the
methods created in good manner, at least to an undergraduate. 

Thank you for checking this code out and let me know if there are any bugs
or data that isn't calculated or displayed correctly.
"""


from graphics import GraphWin, Text, Point, Line


class Run:
    def __init__(self):
        self.date = input("Date (mm/dd/yyyy): ")
        self.date = list(self.date.split("/"))
        self.distance = float(input("Distance: "))
        self.time = input("Time (h:mm:ss): ")
        self.time = list(self.time.split(":"))
        Run.exceptions(self)
    
    def exceptions(self):
        if(len(self.date) != 3):
            print("Invalid date")
            Run()
        for i in range(3):
            if(len(self.time) == i + 1):
                if(int(self.time[i]) > 60):
                    print("Invalid time")
                    Run()
                    
    
    def printDate(self):
        return "{0}/{1}/{2}".format(self.date[0], self.date[1], self.date[2])
    
    def getDate(self):
        year = int(self.date[2])
        month = int(self.date[0])
        day= int(self.date[1])
        return month, day, year
 
    def printDistance(self):
        return self.distance
    
    def printTime(self):
        if(len(self.time) == 1):
            return "0:{0}".format(self.time[0])
        if(len(self.time) == 2):
            return "{0}:{1}".format(self.time[0], self.time[1])
        if(len(self.time) == 3):
            return "{0}:{1}:{2}".format(self.time[0], self.time[1], self.time[2])
    
    
    # Complete Pace calculator method
    def pacing(self):
        if(len(self.time) == 1):
            seconds = float(self.time[0])
            pace = seconds / self.distance
            pace = round(pace, 2)
            pace = list(str(pace).split("."))
            seconds = (int(pace[1]) * 60) / 100
            if(seconds < 10):
                seconds = "0{0}".format(seconds)
            pace.pop(1)
            pace.append(seconds)
            return "{0}:{1} per mile".format(pace[0], pace[1])
        if(len(self.time) == 2):
            minutes = float(self.time[0])
            seconds = (float(self.time[1]))/60
            total = minutes + seconds
            pace = total / self.distance
            pace = round(pace, 2)
            pace = list(str(pace).split("."))
            seconds = (int(pace[1]) * 60) / 100
            if(seconds < 10):
                seconds = "0{0}".format(seconds)
            pace.pop(1)
            pace.append(seconds)
            return "{0}:{1} per mile".format(pace[0], pace[1])
        if(len(self.time) == 3):
            hours = (float(self.time[0])) * 60
            minutes = float(self.time[1])
            seconds = (float(self.time[2])) / 60
            total = hours + minutes + seconds
            pace = total / self.distance
            pace = round(pace, 2)
            pace = list(str(pace).split("."))
            seconds = (int(pace[1]) * 60) / 100
            if(seconds < 10):
                seconds = "0{0}".format(seconds)
            pace.pop(1)
            pace.append(seconds)
            return "{0}:{1} per mile".format(pace[0], pace[1])
    



class calendar:
    def __init__(self):
        self.months = {0: "January", 1: "February", 2: "March", 3: "April",
                       4: "May", 5: "June", 6: "July", 7: "August", 
                       8: "September", 9: "October", 10: "November",
                       11: "December"
                      }
        self.file = open("RunningDatabase.txt", "r")
        self.days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        self.weekDays = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 
                         4: "Thursday", 5: "Friday", 6: "Saturday", 0: "Sunday"}
        self.yearDayStart = 0
 
# Cooresponds to weekDays{}
# What day Janruary 1st is
    def yearStartDay(self, year):
        if(year < 100):
            yearStart = 730500
            for i in range(year):
                yearStart = 365 * (year - 1) + ((year - 1) // 4)
        else:
            for i in range(year):
                yearStart = 365 * (year - 1) + ((year - 1) // 4)
    
        self.yearDayStart = yearStart % 7
        return self.yearDayStart
    
    def monthStartDay(self, year, month):
        yearDayStart = calendar().yearStartDay(year)
        monthDayStart = 0
        if(year % 4 == 0 and month > 2):
            monthDayStart = 1
        for i in range(month):
                monthDayStart = monthDayStart + self.days[i]
            
        monthDayStart = (yearDayStart + monthDayStart) % 7
        return monthDayStart
    
    def leapYearException(self, year, month):
        for i in range(13):
            if(i == 2 and year == 4):
                return 29
            elif(i == month):
                return self.days[i]
 
    def drawCalendar(self):
        win = GraphWin("Calendar", 700, 700)
        win.setCoords(0, 0, 700, 700)
        s = ""
        asking = input("When do you want to see? (mm/yyyy): ")
        date= asking.split("/")
        month = int(date[0])
        year = int(date[1])
        yearStartDay = calendar().yearStartDay(year)
 
        for i in range(12):
            if(month == (i + 1)):
                if(year < 100):
                    s = "{0} 20{1}".format(self.months.get(i), year)
                else:
                    s = "{0} {1}".format(self.months.get(i), year)
 
        print(s)
        calendar().frame(win, s)
        calendar().drawDays(win, year, month)
        calendar().drawData(win, year, month)
 
    def frame(self, win, s):
        header = Text(Point(350, 650), s)
        header.draw(win)
        for i in range(6):
            line = Line(Point(0, (i + 1) * 100), Point(700, (i + 1) * 100))
            line.draw(win)
        for i in range(7):
            horizontal = Line(Point((i + 1) * 100, 600), Point((i + 1) * 100, 0))
            horizontal.draw(win)
        for i in range(7):
            day = Text(Point((i * 100) + 50, 625), self.weekDays.get(i))
            day.draw(win)
    
    def drawDays(self, win, year, month):
        yearDayStart = calendar().yearStartDay(year)
        monthDayStart = calendar().monthStartDay(year, month)
        numDays = calendar().leapYearException(year, month)
            
        for i in range(numDays):
            # yearDayStart * 100
            if(i + monthDayStart < 7):
                day = Text(Point((i + monthDayStart) * 100 + 10, 590), i + 1)
                day.draw(win)
            
            if((i + monthDayStart) == 7):
                for j in range(5):
                    for k in range(7):
                        if(7 * j + k + i >= numDays):
                            break
                        day = Text(Point((k  * 100 + 10), ((500 - j * 100) - 10)), 7 * j + k + i + 1)
                        day.draw(win)
    
    # Drawing the data from the file
    def drawData(self, win, year, month):
        # year, month are the user requested date
        file = open("RunningDatabase.txt", "r")
        f = file.readlines()
        monthDayStart = calendar().monthStartDay(year, month)
 
        for i in range(len(f)):
            line = f[i].split(",")
            fileYear = int(line[2].replace(")", ""))
            fileMonth = int(line[0].replace("(", ""))
            fileDay = int(line[1])
            fileDate = [fileYear, fileMonth, fileDay]
 
            if(fileYear == year and fileMonth == month):
                numDays = calendar().leapYearException(year, month)
 
                for k in range(numDays):
                    if(fileDay == k):
                        if(k + monthDayStart <= 7):
                            for j in range(3):
                                data = Text(Point((k - 1) * 100 + 50,
                                575 - (j *25)), line[j + 3])
                                data.draw(win)
                        if(k + monthDayStart > 7 and k + monthDayStart <= 14):
                            for j in range(3):
                                data = Text(Point((k - 8) * 100 + 50, 
                                            475 - (j * 25)), line[j + 3])
                                data.draw(win)
                        if(k + monthDayStart > 14 and k + monthDayStart <= 21):
                            for j in range(3):
                                data = Text(Point((k - 15) * 100 + 50, 
                                            375 - (j * 25)), line[j + 3])
                                data.draw(win)
                        if(k + monthDayStart > 21 and k + monthDayStart <= 28):
                            for j in range(3):
                                data = Text(Point((k - 22) * 100 + 50, 
                                            275 - (j * 25)), line[j + 3])
                        if(k + monthDayStart > 28 and k + monthDayStart <= 37):
                            for j in range(3):
                                data = Text(Point((k - 29) * 100 + 50, 
                                            175 - (j * 25)), line[j + 3])
 
 
class database:
    def __init__(self, database1):
        self.database = database1
 
    def addRun(self, a):
        tdList = []
        tdList.append(a.printDistance())
        tdList.append(a.printTime())
        tdList.append(a.pacing())
        self.database.update({a.printDate(): tdList})
        f = open("RunningDatabase.txt" , "a")
        s = "{0},{1},{2},{3}\n".format(a.getDate(), a.printDistance(), a.printTime(), a.pacing())
        print(s)
        f.write(s)
        f.close()
        return self.database
    
    def editRun(self):
        s = ""
        findDate = input("What date do you want to edit? ")
        findDate = list(findDate.split("/"))
        year = int(findDate[2])
        month = int(findDate[0])
        day = int(findDate[1])

        file = open("RunningDatabase.txt", "r")
        f = file.readlines()
        for i in range(len(f)):
            line = f[i].split(",")
            year2 = int(line[2].replace(")", ""))
            month2 = int(line[0].replace("(", ""))
            day2 = int(line[1])
            print(year, month, day)
            print(year2, month2, day2)
            if(year == year2 and month == month2 and day == day2):
                f.pop(i)
        filing = f
        
        fileWrite = open("RunningDatabase.txt", "w")
        for i in range(len(f)):
            fileWrite.write(f[i])
        file.close()
        fileWrite.close()
        a = Run()
        database.addRun(self, a)


def findLongestRun():
    maxDistance = 0
    f = open("RunningDatabase.txt", "r")
    file = f.readlines()
    for i in range(len(file)):
        line = file[i].split(",")
        if(float(line[3]) > maxDistance):
            maxDistance = float(line[3])
    f.close()
    return maxDistance


def sortDatabase():
    # Uses bubble sort
 
    # Opens the .txt file of all the data
    f = open("RunningDatabase.txt", "r+")
    file = f.readlines()
 
    # If there are no runs, returns an error
    if(file == []):
        print("Add a run")
        return False
 
    for i in range(len(file)):
        
        # Bubble sort method that brings newest date to end of list
        for k in range(len(file) - i - 1):
            line = file[k].split(",")
            year = int(line[2].replace(")", ""))
            month = int(line[0].replace("(", ""))
            day = int(line[1])
            if(year < 100):
                year = 2000 + year
            date = [year, month, day]
 
            line2 = file[k + 1].split(",")
            year2 = int(line2[2].replace(")", ""))
            month2 = int(line2[0].replace("(", ""))
            day2 = int(line2[1])
            if(year < 100):
                year = 2000 + year
            date2 = [year2, month2, day2]
 
            if(year > year2):
                file[k], file[k + 1] = file[k + 1], file[k]
            elif(year == year2):
                if(month > month2):
                    file[k], file[k + 1] = file[k + 1], file[k]
                elif(month == month2):
                    if(day > day2):
                        file[k], file[k + 1] = file[k + 1], file[k]
    f.close()

    f = open("RunningDatabase.txt", "w")
                
    # File is from oldest at file[0] to newest at file[end]
    s = ""
    for i in range(len(file)):
        s = s + file[i]
    f.write(s)
    f.close()
 
 
def main():
    going = False
    database1 = {}
    while(going is False):
        print("What do you want to do? ")
        print("1: Calendar\n2: Add run\n3: Longest Run\n4: Edit a run\n5: Quit")
 
        method = int(input())
        if (method == 1):
            calendar().drawCalendar()
        elif (method == 2):
            a = Run()
            print(database(database1).addRun(a))
            #print("Date        Distance          Time          Pace")
            #print("-"*50)
            #print("{0}      {1} miles        {2}    {3}".format(a.printDate(), a.printDistance(), a.printTime(), a.pacing()))
        elif(method == 3):
            print("Your longest run is {0} miles".format(findLongestRun()))
        elif(method == 4):
            database(database1).editRun()
        elif(method == 5):
            break
        else:
            print("Option under development")
    sortDatabase()
 
if(__name__ == "__main__"):
    main()
