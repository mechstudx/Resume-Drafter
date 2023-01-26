#   2023-01-04  SJ: The following application will encapulate several string
#                   formatted resumes to output
__author__='SJ Rex'

from JobResponsibility import JobResponsiblity
from Resume import Resume
from Portfolio import Portfolio
from Skills import Skill
from JobHistory import JobHistory
from Education import Education
from Jobseeker import Jobseeker

class ContemporaryResume(Resume):
    def __init__(self, jobseeker: Jobseeker) -> None:
        super().__init__(jobseeker)
        self.resumeType = Resume.CONTEMPORARY
    def StyleTag(self) -> str:
        return '''<!--Style Sheets-->
	  	          <style type="text/css">
		                .schoolIndent 
		                {
			                margin-left: 0.25in;
		                }
		                P, li, div
		                {
			                FONT-FAMILY: Times New Roman; WHITE-SPACE: normal
		                }					
		                P, li, div, td, .jobtitle
		                {
			                FONT-SIZE: 10pt;
		                }
		                li, .schoolIndent 
		                {
			                margin-top:		2pt;
			                margin-bottom:	2pt;
		                }
		                .sectiontitle
		                {
			                border-right-style: solid;
			
		                }
		                .sectiontitle div 
		                {
			
			                font-family:		Arial;
			                FONT-WEIGHT: 		bold; 
			                TEXT-ALIGN: 		left; 
			                font-size: 			10pt;
			                background-color: #C0C0C0;
	
		                }
		                .right {
			                TEXT-ALIGN: 	right;
			                margin-left:	0.25in;
		                }
		                .pageBreak
		                {
			                page-break-after: always;
		                }
		                tr
		                {
			                vertical-align:	top;
		                }
		                .name
		                {
			                font-family:		Times New Roman;
			                font-size:			24pt;
			                margin-top:			18pt;
			                margin-bottom:		22pt;
			                margin-left:		0.25in;
		                }
		                .left, .address1, .sectiontitle div 
		                {
			                text-align:		left;
			                width:			2in;
		                }
		                .address1, .address2
		                {
			                font-family:	Times New Roman;
			                font-size:		8pt;
		                }
		                .address2
		                {
			                TEXT-ALIGN: 	right;
		                }
		                .address2, .right
		                {
			                margin-top:		2pt;
			                margin-bottom:	12pt;
		                }
		                .right
		                {
			                text-align:		left;
		                }
		                .jobtitle
		                {
			                font-family:	Arial;
		                }
		                .date
		                {
			                width: 2in;					
		                }
		                .company
		                {
			                width: 2in; 
			                text-align: center; 					
		                }		
		          </style>
              <!--End of style sheets-->'''
    def BodyTag(self) -> str:
        return self.BodyStartTag() + '''
                <table border="0">
                    ''' + self.BodyHeading() + self.BodyObj() + self.BodyPortfolio() + self.BodySkills() + self.BodyJobHistory() + self.BodyEducation()  + '''
                </table>
            ''' + self.BodyFooter() + self.BodyEndTag()
    def BodyHeading(self):
        return '''<!--Heading information-->
		            <tr>
				        <td style="border-right-style: solid;">
					        <div class="address1">
		                        ''' + self.jobseeker.Address + '''
		                        <br />
		                        ''' + self.jobseeker.City + ',&nbsp;' + self.jobseeker.StateOrProvince + '&nbsp;' + self.jobseeker.PostalCode + '''
		                    </div> 					
		                </td>
				        <td>
					        <div class="address2">
	    				        ''' + self.jobseeker.HomePhone + '''&nbsp;&#149;&nbsp;
                                <a href="mailto: ''' + self.jobseeker.EmailName + '''">''' + self.jobseeker.EmailName + '''</a>
                                <!--&nbsp;&#149;&nbsp;http://resumedrafter.somee.com/Jobseeker/View/@jobseeker.JobseekerID	-->
	    			        </div>
				        </td>
			        </tr>
			        <!--Jobseeker's Full Name-->
			        <tr>
	    		        <td style="border-right-style: solid;"></td>
	    		        <td width="444" valign="top" style='width:333.35pt;padding:0in 5.4pt 0in 5.4pt'>
	    			            <div class="name">
		                        ''' + self.jobseeker.FirstName + '&nbsp;' + self.jobseeker.LastName + '''         
		                    </div>
	    		        </td>
	    	        </tr>
			        <!--End Jobseeker's Full Name-->
			        <!--End of formating the heading information-->'''
    def BodyObj(self):
        return '''<!--Objective-->
	    	        <tr>
	    		        <td class="sectiontitle"><div>Objective</div></td>
	    		        <td width="444" valign="top" style='width:333.35pt;padding:0in 5.4pt 0in 5.4pt'>
	    			        <div class="right">
                                ''' + self.jobseeker.objective.ObjectiveDescription + '''           
		                    </div>
	    		        </td>
	    	        </tr>
	    	        <!--End of Objective--> '''
    def BodyPortfolio(self) -> str:
        ret:str = '''
            <!--Portfolio-->
            <tr>
                <td class="sectiontitle"><div>Portfolio</div></td>
                <td width="444" valign="top" style='width:333.35pt;padding:0in 5.4pt 0in 5.4pt'>
                    <div class="right">
                        <!--ENTER SKILLS DESCRIPTION HERE...-->
                        <ul>'''
        for val in self.jobseeker.portfolios:
            ret = ret + '''
                            <li><a href="''' + val[Portfolio.SITE_ADDR] + '''">''' + val[Portfolio.SITE_ADDR] + '''</a></li>'''
        ret =   ret + '''
                        </ul>           
                    </div>
                </td>
            </tr>
            <!--End of Portfolio-->
        '''
        return ret
    def BodySkills(self) -> str:
        ret:str = '''
                    <!--Skills-->
	    	        <tr>
	    		        <td class="sectiontitle"><div>Skills</div></td>
	    		        <td width="444" valign="top" style='width:333.35pt;padding:0in 5.4pt 0in 5.4pt'>
	    			        <div class="right">
		                        <!--ENTER SKILLS DESCRIPTION HERE...-->
			        	        <ul>'''
        for val in self.jobseeker.objective.skills:
            ret = ret + '''
                                        <li>''' + val[Skill.SKILL_DESC] + '''</li>'''
        ret = ret + '''
    	                        </ul>    
		                    </div>
	    		        </td>
	    	        </tr>
			        <!--End of Skills-->
        '''
        return ret
    def BodyJobHistory(self) -> str:
        ret:str = '''
                    <!--Experience-->
			        <tr>
	    		        <td class="sectiontitle"><div>Experience</div></td>            		
	    		        <td width="444" valign="top" style='width:333.35pt;padding:0in 5.4pt 0in 5.4pt'>
                        '''
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
	    		            <div class="right">
	                    	    <div style="tab-stops:1.5in right 4.5in;">
								    <table width="415">
									    <tr>
										    <td width="125">
                                                ''' + startDate + '''&nbsp;-&nbsp;''' + endDate + '''
										    </td>
										    <td width="205">
											    ''' + var[JobHistory.COMPANY_NAME] + '''
										    </td>
										    <td align="right">
											    ''' + cityState + '''
										    </td>
									    </tr>
								    </table>
							    </div>
							    <!--Job Title-->
                        	    <div class="jobtitle">
                        		    <b>
                        			    <i>
                        				    ''' + var[JobHistory.JOB_TITLE] + '''
                        			    </i>
                        		    </b>
                        	    </div>
                        	    <!--Job Responsibilities-->		                  	    
								<div>
                                    <ul>'''
            try:
                jrList:list = [[j for j in i if i[:len(i)-1][JobResponsiblity.JOB_HISTORY_ID]==var[JobHistory.ID]] for i in self.jobseeker.objective.jr]
            			
                for jr in jrList:                
                    if len(jr) > 0:
                        ret = ret + '''
                                        <li>
                                        ''' + jr[JobResponsiblity.RESPONSIBLITY] + '''
                                        </li>
                                        '''
            except:
                ret = ret + '''
                                        <!--ERROR OCCURRED WHILE TRYING TO ACCESS JOB RESPONSIBLITIES    -->
                                        '''
            ret = ret + '''
                                    </ul>
                                </div>    
                            </div>        
                '''
        ret = ret + '''
	    		        </td>
	    	        </tr>
	    	        <!--End of Experience-->
            '''
        return ret
    def BodyEducation(self) -> str:
        ret:str = '''
                    <!--Education-->
	                <tr>
	       		        <td class="sectiontitle"><div>Education</div></td>
	       		        <td width="444" valign="top" style='width:333.35pt;padding:0in 5.4pt 0in 5.4pt'>
                    '''
        for val in self.jobseeker.education:
            try:
                endDate:str = val[Education.END_DATE].strftime('%m/%d/%Y')
            except:
                endDate = Education.DEFAULT_ATTENDANCE_TXT
            try:
                startDate:str = val[Education.START_DATE].strftime('%m/%d/%Y')
            except:
                startDate = val[Education.START_DATE]
            ret = ret + '''
                            <div class="right">
                                <p>
                                    <div style="tab-stops:1.5in right 4.5in;">
                                        <table width="415">
                                            <tr>
                                                <td width="125">
                                                    <!--Date Range-->
                                                    ''' + startDate + '''&nbsp;-&nbsp;''' + str(endDate) + '''
                                                </td>
                                                <td width="205">
                                                    <!--School Name-->
                                                    ''' + val[Education.SCHOOL_NAME] + '''
                                                </td>
                                                <td align="right">
                                                    <!--City and State-->
                                                    '''+ val[Education.CITY] + ''',&nbsp;''' + val[Education.STATE] 	+ '''
                                                </td>
                                            </tr>
                                        </table>
                                        <ul>
                                            <li>''' + val[Education.DEGREE] + '''</li>
                                        </ul>
                                    </div>
                                </p>
                            </div>
                        '''
        ret = ret + '''   		
	       		        </td> 
	                </tr>
	                <!--End of Education-->	
        '''
        return ret
    def BodyFooter(self) -> str:
        return '''
                <div style="margin-top: 24pt">
		            <p><center><b>References: </b>Available upon request</center></p>
	            </div>
	            <!--<br style="page-break-after: always;" />-->'''