#   2023-01-04  SJ: The following application will encapulate several string
#                   formatted resumes to output
__author__='SJ Rex'

from datetime import date
from JobResponsibility import JobResponsiblity
from Resume import Resume
from Portfolio import Portfolio
from Skills import Skill
from JobHistory import JobHistory
from Education import Education
from Jobseeker import Jobseeker

class RegResume(Resume):
    def __init__(self, jobseeker: Jobseeker) -> None:
        super().__init__(jobseeker)
        self.resumeType = Resume.REGULAR
    def StyleTag(self) -> str:
        return '''<!--Style Sheets-->
                <style type="text/css">
		            p, .Header, .schoolIndent, h1, li, td
		            {
			            FONT-FAMILY: Arial; 
			            WHITE-SPACE: normal
		            }
		            p, li, div, td, .Header, .schoolIndent
		            {
			            FONT-SIZE: 9pt
		            }
		            .Header
		            {
			            FONT-WEIGHT: bold; 
			            TEXT-TRANSFORM: uppercase; 
			            TEXT-ALIGN: center; 
			            TEXT-DECORATION: underline
		            }
		            .schoolIndent 
		            {
			            MARGIN: 0in 0in 0in 5%
		            }
	            </style>
                <!--End of style sheets-->'''
    def BodyTag(self) -> str:
        return self.BodyStartTag() + self.BodyHeading() + self.BodyObj() + self.BodyPortfolio() + self.BodySkills() + '''
                <table border="0" align="center">
	                <colgroup>
	                    <col align="left" span="1" />
	                </colgroup>
	                <tbody vAlign="top">
                    ''' + self.BodyJobHistory() + self.BodyEducation() + '''
			        </tbody>
	 	        </table>
                ''' + self.BodyFooter() + self.BodyEndTag()
    def BodyHeading(self):
        return '''<!--Heading information-->
	            <h1 style="TEXT-ALIGN: center">
		            <!--ENTER JOB SEEKER FULL NAME HERE...-->
                ''' +   self.jobseeker.FirstName + '&nbsp;' + self.jobseeker.LastName + '''
                </h1>
                <hr />
                <p style="TEXT-ALIGN: center">
                    ''' + self.jobseeker.Address + '&#149;' + self.jobseeker.City + ',&nbsp;' + self.jobseeker.StateOrProvince + '&nbsp;' + self.jobseeker.PostalCode + '&#149;' + self.jobseeker.HomePhone + '&#149;' + self.jobseeker.EmailName + '''
                    <!--&nbsp;&#149;&nbsp;http://resumedrafter.somee.com/Jobseeker/View/@jobseeker.JobseekerID-->
                </p>
                <!--End of formating the heading information-->'''
    def BodyObj(self):
        return '''<!--Objective-->
                <p class="Header">Objective:</p>
                <p>
                    ''' + self.jobseeker.objective.ObjectiveDescription + '''
                </p>
                <!--End of Objective-->'''
    def BodyPortfolio(self) -> str:
        ret:str = '''
            <!--Portfolio-->
            <p class="Header">Portfolio:</p>
            <div>
                <ul>
                '''
        for val in self.jobseeker.portfolios:
            ret = ret + '''
                ''' + '<li>' + val[Portfolio.SITE_ADDR]  + '</li>'
        ret = ret + '''
                </ul>
            </div>                            
            <!--End of Portfolio-->
            '''
        return ret
    def BodySkills(self) -> str:
        ret:str = '''
                    <!--Skills-->
                    <p class="Header">Skills:</p>
                    <div>
                        <!--ENTER SKILLS DESCRIPTION HERE...-->
                        <ul>'''
        for val in self.jobseeker.objective.skills:
            ret = ret + '''
                                <li>''' + val[Skill.SKILL_DESC] + '''</li>'''
        ret = ret + '''
                        </ul>    
                    </div>
                    <!--End of Skills-->
        '''
        return ret
    def BodyJobHistory(self) -> str:
        ret:str = '''       
                    <!--ACCESS JOB_HISTORY TABLE USING JOBSEEKERID HERE...-->
                    <!--Experience-->
                    <tr>
                        <td class="Header" colspan="2">Experience</td>
                    </tr>'''
        
        for var in self.jobseeker.objective.jobHistory:			
            try:
                startDate:str = var[JobHistory.START_DATE].strftime('%m/%d/%Y')
            except:
                startDate = var[JobHistory.START_DATE]
            if bool(var[JobHistory.IS_PRESENT]):
                endDate:str = JobHistory.PRESENT
            else:
                try:
                    endDate:str = var[JobHistory.END_DATE].strftime('%m/%d/%Y')
                except:
                    endDate = var[JobHistory.END_DATE]
            try:
                if var[JobHistory.CITY]=='Remote':
                    cityState:str = var[JobHistory.CITY]
                else:
                    cityState:str = var[JobHistory.CITY] + ''', &nbsp;''' + var[JobHistory.STATE]
            except:
                cityState = 'N/A'
                    
            ret = ret + '''
                        <tr valign="top">
                            <td>
                                <span tabIndex="-1" style="WIDTH: 100%">''' + var[JobHistory.COMPANY_NAME] + '''</span>
                                <br />
                                <span tabIndex="-1" style="WIDTH: 100%">
                                    <b><i>''' + var[JobHistory.JOB_TITLE] + '''</i></b>
                                </span>
                                <br />
                                <div>
                                    <ul>
						'''

            try:
                jrList:list = [list([j for j in i if i[:len(i)-1][JobResponsiblity.JOB_HISTORY_ID]==var[JobHistory.ID]]) for i in self.jobseeker.objective.jr]
                        
                for jr in jrList:                
                    if len(jr) > 0:
                        ret = ret + '''
                                            <li>
                                                ''' + jr[JobResponsiblity.RESPONSIBLITY] + '''              
                                            </li>
                                            '''
            except:
                ret = ret + '''<!--ERROR OCCURRED WHILE TRYING TO ACCESS JOB RESPONSIBLITIES    -->'''
            ret = ret + '''			
                                    </ul>
                                </div>
                                <!--ACCESS JOB_RESPONSIBILITIES TABLE HERE USING CURRENT JOB_HISTORY ID HERE...-->
                            </td>
                            <td align="right" style="width: 1.5in">
                                <!--INSERT CITY AND STATE HERE...-->
                                ''' + cityState + '''
                                <br />
                                <!--INSERT START AND END DATE HERE...-->
                                ''' + startDate + '''&nbsp;-&nbsp;''' + endDate + '''
                            </td>
                            </tr>
                    '''

        ret = ret + '''
                    <!--End of Experience-->
                    <!--ACCESS EDUCATION TABLE USING THE JOBSEEKER ID HERE...-->
        '''
        return ret
    def BodyEducation(self) -> str:
        ret:str = '''
                        <!--Education-->
	                    <tr>
	            	         <td class="Header" colspan="2">Education</td>
	                    </tr>
                    '''

        for val in self.jobseeker.education:
            try:
                endDate:date = val[Education.END_DATE]
                yrAttended:str = str(endDate.strftime('%Y'))
            except:
                yrAttended = Education.DEFAULT_ATTENDANCE_TXT
            ret = ret + '''
                        <tr valign="top">
						        <td>
							        ''' + val[Education.SCHOOL_NAME] + '''
							        <br />
							        <div class="schoolIndent">
								        <u>
									        <i>
										        <b>''' + val[Education.DEGREE] + '''</b>
									        </i>
								        </u>								
							        </div>
							        <br /> 
						        </td>
						        <td align="right">
							        ''' + val[Education.CITY] + ''',&nbsp;''' + val[Education.STATE] + '''
							        <br />
							        '''+ yrAttended + '''
							        <br />
						        </td>
					        </tr>
	                    <!--End of Education--> '''
        return ret
    def BodyFooter(self) -> str:
        return '''<center><p><b>References: </b>Available upon request</p></center>
    	        <!--<br style="page-break-after: always;" />	-->'''