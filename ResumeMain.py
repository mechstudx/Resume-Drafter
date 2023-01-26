#   2023-01-04  SJ: The following application will access the Resume Drafter Access Database and output resume as Regular format.
__author__='SJ Rex'

#   Reference:  https://pythoninoffice.com/python-ms-access-database-pyodbc/
#   How To Connect And Work With MS Access Database Using Python pyodbc

#   Python can connect to and work with a wide variety of database applications, MS Access database is one of them. 
#   We’ll walk through how to use the pyodbc library to interact with an Access database.

#   Install pyodbc and check ODBC driver version

#   pip install pyodbc

#   TL;DR – You need 32-bit Python for 32-bit Access, or 64-bit Python for 64-bit Access.

#   One thing to note upfront, if you have 64-bit MS Access, you’ll want to use the 64-bit Python for this exercise. 
#   Mixing up a 64-bit Python with 32-bit Access will throw an error when you try to connect. The reason is that there 
#   are two different Access ODBC drivers from Microsoft:

#    Old Driver (32-bit) – Microsoft Access Driver (*.mdb): works with 32-bit Python
#    New Driver (64-bit) – Microsoft Access Driver (*.mdb, *.accdb): works with 64-bit Python

#   Your machine should already have one of the drivers if you have MS Office installed. In case 
#   you don’t have the driver, you can download a standalone version on Microsoft’s website: 
#   https://www.microsoft.com/en-US/download/details.aspx?id=13255

#   To check which version of the Access ODBC driver is on your computer, do the following in Python:

#   >>>import pyodbc
#   >>>[i for i in pyodbc.drivers() if i.startswith('Microsoft Access Driver')]
#   ['Microsoft Access Driver (*.mdb, *.accdb)']

#   This list comprehension iterates through all available ODBC drivers and only returns the ones that 
#   start with “Microsoft Access Driver”. The above result shows that my computer has the new 64-bit 
#   Access (and driver).

from sqlite3 import Connection
import sys
import pyodbc
from typing import Final
import re
from ContemporaryResume import ContemporaryResume
from ElegantResume import ElegantResume
from ProfessionalResume import ProfessionalResume
from RegResume import RegResume
from Resume import Resume
from Jobseeker import Jobseeker

class ResumeMain:
    '''
        2022-11-30  SJ: The following are constants to index the Data Dictionary List.

        REFERENCE: https://stackoverflow.com/questions/2682745/how-do-i-create-a-constant-in-python
        You cannot declare a variable or value as constant in Python.

        To indicate to programmers that a variable is a constant, one usually writes it in upper case:

        CONST_NAME = "Name"

        To raise exceptions when constants are changed, see Constants in Python by Alex Martelli. Note that this is not commonly used in 
        practice.

        As of Python 3.8, there's a typing.Final variable annotation that will tell static type checkers (like mypy) that your variable 
        shouldn't be reassigned. This is the closest equivalent to Java's final. However, it does not actually prevent reassignment:

        from typing import Final

        a: Final[int] = 1

        # Executes fine, but mypy will report an error if you run mypy on this:
        a = 2
    '''
    APP_PATH_INDEX:Final[int]=0
    OBJ_ID_INDEX:Final[int]= 1
    OUTPUT_FILE_PATH_INDEX:Final[int]=2
    RESUME_FILE_TYPE_INDEX:Final[int]=3
    DB_FILE_PATH_INDEX:Final[int]=4

    
    _db_file_path:str = None
    _objectiveID:int = None
    _resumeType:int = None
    _filePath:str = None
    _resume:Resume = None
    _jobseeker:Jobseeker = Jobseeker()
    _conn:Connection = None
    _cursor:any = None

    def __init__(self) -> None:
        print("Creating instance:\t{0}".format(type(self)))
        self._objectiveID = int(sys.argv[ResumeMain.OBJ_ID_INDEX])
        self._db_file_path = str(sys.argv[ResumeMain.OUTPUT_FILE_PATH_INDEX])
        self._resumeType = int(sys.argv[ResumeMain.RESUME_FILE_TYPE_INDEX])
        self._db_file_path=str(sys.argv[ResumeMain.DB_FILE_PATH_INDEX])
        self._filePath = str(sys.argv[ResumeMain.OUTPUT_FILE_PATH_INDEX])
        print("{0} has successfully created.".format(type(self)))

    #   REFERENCE:  https://www.geeksforgeeks.org/getter-and-setter-in-python/
    #   2023-01-10  SJ: using property decorator
    #   getter functions
    @property
    def objectiveID(self)->int:
        return self._objectiveID
    @property
    def db_file_path(self)->str:
        return self._db_file_path
    @property
    def resumeType(self)->int:
        return self._resumeType
    @property
    def jobseeker(self)->Jobseeker:
        return self._jobseeker

    #   Connect Python to MS Access Database

    #   To connect to a database, we need a connection string, basically a text pointer that tells Python 
    #   where to find the database. For MS Access, we also need to specify the type of ODBC driver 
    #   (32bit vs 64bit) in the connection string.

    #   Also make sure you close the MS Access database before making the connection, otherwise there will 
    #   be an error.
    def openDB(self)->None:
        print("Opening database...")
        conn_str = (r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=' + self._db_file_path + ';')
        print(self._db_file_path)
        self._conn = pyodbc.connect(conn_str)
        print("Database connection opened.")
        self._cursor = self._conn.cursor()
        print("Database successfully opened:\t{0}".format(self._db_file_path))

    def setJobseeker(self):
        self._cursor.execute('''
            SELECT Jobseekers.JobseekerID, Jobseekers.FirstName, Jobseekers.LastName, Jobseekers.Address, Jobseekers.City, Jobseekers.StateOrProvince, Jobseekers.PostalCode, Jobseekers.HomePhone, Jobseekers.EmailName
            FROM Jobseekers INNER JOIN Objectives ON Jobseekers.JobseekerID = Objectives.JobseekerID
            WHERE (((Objectives.ObjectiveID)=''' + str(self._objectiveID) + '''));
            ''')
        curr_row = self._cursor.fetchone()
        self._jobseeker.setVals(curr_row)

    def setObjective(self):
        self._cursor.execute('''
            SELECT Objectives.ObjectiveID, Objectives.ObjectiveName, Objectives.ObjectiveDescription, Objectives.JobseekerID
            FROM Objectives
            WHERE (((Objectives.ObjectiveID)=''' +  str(self._objectiveID) + '''));
            ''')
        curr_row=self._cursor.fetchone()
        self._jobseeker.objective.setVals(vals=curr_row)

    def setPortfolio(self):
        self._cursor.execute('''
            SELECT Portfolio.ID, Portfolio.SiteName, Portfolio.SiteAddress, Portfolio.Jobseeker
            FROM (Jobseekers INNER JOIN Objectives ON Jobseekers.JobseekerID = Objectives.JobseekerID) 
                INNER JOIN Portfolio ON Jobseekers.JobseekerID = Portfolio.Jobseeker
            WHERE (((Objectives.ObjectiveID)=''' +  str(self._objectiveID) + '''));
            ''')
        all_rows=[list(x) for x in self._cursor.fetchall()]
        self._jobseeker.portfolios = all_rows

    def setEducation(self):
        self._cursor.execute('''
            SELECT Education.Education_ID, Education.School_Name, Education.Degree, Education.City, Education.State, 
                Education.Jobseeker_ID, Education.gpa, Education.Address, Education.ZipCode, Education.StartDate, 
                Education.EndDate, Education.PhoneNumber
            FROM (Jobseekers INNER JOIN Objectives ON Jobseekers.JobseekerID = Objectives.JobseekerID) 
                INNER JOIN Education ON Jobseekers.JobseekerID = Education.Jobseeker_ID
            WHERE (((Objectives.ObjectiveID)=''' +  str(self._objectiveID) + '''))
            ORDER BY Education.EndDate DESC;
            ''')
        all_rows=[list(x) for x in self._cursor.fetchall()]
        self._jobseeker.education = all_rows

    def setSkills(self):
        self._cursor.execute('''
            SELECT Skills.Skill_ID, Skills.skillDescr
            FROM Skills INNER JOIN (Objectives INNER JOIN Objective_Skills ON Objectives.ObjectiveID = Objective_Skills.ObjectiveID) ON Skills.Skill_ID = Objective_Skills.SkillsID
            WHERE (((Objectives.ObjectiveID)=''' +  str(self._objectiveID) + '''));
            ''')
        all_rows=[list(x) for x in self._cursor.fetchall()]
        self._jobseeker.objective.skills= all_rows

    def setJobHistory(self):
        self._cursor.execute('''
            SELECT Job_History.Job_History_ID, Job_History.Company_Name, Job_History.Job_Title, Job_History.Street, Job_History.City, Job_History.State, Job_History.ZipCode, Job_History.Start_Date, Job_History.End_Date, Job_History.IsPresent
            FROM Job_History INNER JOIN (Objectives INNER JOIN Objective_Job_History ON Objectives.ObjectiveID = Objective_Job_History.ObjectiveID) ON Job_History.Job_History_ID = Objective_Job_History.JobHistoryID
            WHERE (((Objectives.ObjectiveID)=''' +  str(self._objectiveID) + '''))
            ORDER BY Job_History.Start_Date DESC , Job_History.End_Date;
            ''')
        all_rows=[list(x) for x in self._cursor.fetchall()]
        self._jobseeker.objective.jobHistory= all_rows
    def setJobHistoryResponsiblities(self):
        self._cursor.execute('''
            SELECT Job_Responsibilities.Job_Responsibility_ID, Job_Responsibilities.Job_History_ID, 
                Job_Responsibilities.Job_Rsponsibility
            FROM (Job_History INNER JOIN (Objectives INNER JOIN Objective_Job_History ON Objectives.ObjectiveID = Objective_Job_History.ObjectiveID) ON Job_History.Job_History_ID = Objective_Job_History.JobHistoryID) INNER JOIN Job_Responsibilities ON Job_History.Job_History_ID = Job_Responsibilities.Job_History_ID
            WHERE (((Objectives.ObjectiveID)=''' +  str(self._objectiveID) + '''));
            ''')
        all_rows:list=[list(x) for x in self._cursor.fetchall()]
        #all_rows=self._cursor.fetchall()
        self._jobseeker.objective.jobResponsiblities =  all_rows
        #self._jobseeker.objective.jr = all_rows
        #print("{0}\t{1}".format(type(all_rows), all_rows))

    def saveToFile(self, resume:Resume)->None:
        print("Saving resume...\n{0}".format(self._db_file_path))
        #   2023-01-19  SJ: REFERENCE:  https://www.tutorialspoint.com/regular-expression-in-python-with-examples#:~:text=Regular%20Expression%20in%20Python%20with%20Examples%3F%20RegEx%20Module,Metacharacters%20Special%20Sequences%20Sets%20Example%20-%20findall%20%28%29
        origFileName:str=self._filePath.split('\\')[len(self._filePath.split('\\'))-1]
        newFileName:str = self._filePath.split('\\')[len(self._filePath.split('\\'))-1].replace('.html', '')
        #print(newFileName)
        specChr:list = re.findall("\W+", newFileName)
        #print(specChr)
        for val in specChr:
            newFileName = newFileName.replace(val, '')
            #print(newFileName)
        newFileName = newFileName + ".html"
        w = open(self._filePath.replace(origFileName,newFileName), mode="w")

        w.write(resume.Resume())

        w.close()
        print("File successfully saved.")

    def closeDB(self)->None:
        print("Closing database connection.")
        self._conn.close()
        print("Database connection closed.")




def main():
    print("Running main...")
    rm:ResumeMain = ResumeMain()
    resume:Resume = None

    rm.openDB()
    rm.setJobseeker()
    rm.setObjective()
    rm.setSkills()
    rm.setJobHistory()
    rm.setJobHistoryResponsiblities()
    rm.setPortfolio()
    rm.setEducation()
    rm.closeDB()

    switch={
        Resume.REGULAR: RegResume(rm.jobseeker),
        Resume.CONTEMPORARY: ContemporaryResume(rm.jobseeker),
        Resume.ELEGANT: ElegantResume(rm.jobseeker),
        Resume.PROFESSIONAL:ProfessionalResume(rm.jobseeker)
    }

    resume = switch.get(rm.resumeType, None)

    rm.saveToFile(resume=resume)



if __name__=="__main__":
    main()