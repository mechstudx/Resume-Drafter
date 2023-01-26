#   2023-01-04  SJ: The following application will encapulate several string
#                   formatted resumes to output
__author__='SJ Rex'

from typing import Final
import abc
import Jobseeker

class Resume(abc.ABC):
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
    REGULAR:Final[int]=1
    CONTEMPORARY:Final[int]=2
    ELEGANT:Final[int]=3
    PROFESSIONAL:Final[int]=4

    _resumeType:int  = None

    _jobseeker:Jobseeker = None

    def __init__(self, jobseeker: Jobseeker) -> None:
        self._jobseeker = jobseeker

    #   REFERENCE:  https://www.geeksforgeeks.org/getter-and-setter-in-python/
    #   2023-01-10  SJ: using property decorator
    #   getter functions
    @property
    def resumeType(self):
        return self._resumeType
    @property
    def jobseeker(self):
        return self._jobseeker

    #   setter functions
    @resumeType.setter
    def resumeType(self, rType: int) -> None:
        self._resumeType = rType
    def getResumeTypeName(self) -> str:
        switch={
            self.REGULAR:'regular',
            self.CONTEMPORARY:'contemporary',
            self.ELEGANT:'elegant',
            self.PROFESSIONAL:'professional'
        }
        return switch.get(self._resumeType, '')
    
    def HTMLStartTag(self) -> str:
        return '''<html xmlns:o="urn:schemas-microsoft-com:office:office"
            xmlns:w="urn:schemas-microsoft-com:office:word"
            xmlns="http://www.w3.org/TR/REC-html40">'''

    def HeadTag(self) -> str:
        return self.HeadStartTag() + self.MetaTags() + self.TitleTag() + self.IconTag() + self.StyleTag() + self.HeadEndTag()

    def HeadStartTag(self) -> str:
        return '<head>'

    def MetaTags(self):
        return '''<!--<meta charset="utf-8" content="application/msword" />-->
                <!--<meta charset="utf-8" content="application/msword" />-->
				<meta charset="utf-8" content="application/pdf" />
                <meta name=Generator content="Microsoft Word 11">
                <meta name=Originator content="Microsoft Word 11">
                <meta name="viewport" content="width=device-width, initial-scale=1">'''
    
    def TitleTag(self) -> str:
        return '<title>' + self._jobseeker.FirstName + ' ' + self._jobseeker.LastName + ': Resume' + '</title>'
    
    def IconTag(self) -> str:
        return '''<!--Icons-->
		        <link rel="icon" href="/images/icon.ico" type="image/x-icon" />
		        <link rel="shortcut icon" href="/images/icon.ico" type="image/x-icon" />
		        <!--End of Icons-->'''

    @abc.abstractmethod
    def StyleTag(self) -> str:
        pass

    def HeadEndTag(self) -> str:
        return '</head>'

    @abc.abstractmethod
    def BodyTag(self) -> str:
        pass

    def BodyStartTag(self) -> str:
        return '<body>'
    
    @abc.abstractmethod
    def BodyHeading(self) -> str:
        pass

    @abc.abstractmethod
    def BodyObj(self) -> str:
        pass

    @abc.abstractmethod
    def BodyPortfolio(self) -> str:
        pass

    @abc.abstractmethod
    def BodySkills(self) -> str:
        pass

    @abc.abstractmethod
    def BodyJobHistory(self) -> str:
        pass

    @abc.abstractmethod
    def BodyEducation(self) -> str:
        pass

    @abc.abstractmethod
    def BodyFooter(self) -> str:
        pass

    def BodyEndTag(self) -> str:
        return '</body>'
    def HTMLEndTag(self) -> str:
        return '</html>'
    def Resume(self) -> str:
        return self.HTMLStartTag() + self.HeadTag() + self.BodyTag() + self.HTMLEndTag() 