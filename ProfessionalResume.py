#   2023-01-04  SJ: The following application will encapulate several string
#                   formatted resumes to output
__author__='SJ Rex'

import traceback
import sys
from JobResponsibility import JobResponsiblity
from Resume import Resume
from Portfolio import Portfolio
from Skills import Skill
from JobHistory import JobHistory
from Education import Education
from Jobseeker import Jobseeker

class ProfessionalResume(Resume):
    def __init__(self, jobseeker: Jobseeker) -> None:
        super().__init__(jobseeker)
        self.resumeType = Resume.PROFESSIONAL
    def StyleTag(self) -> str:
        return '''<!--Style Sheets-->
	  	          <style type="text/css">
			          p.Name, li.Name, div.Name
				          {mso-style-name:Name;
				          mso-style-next:Normal;
				          margin-top:0in;
				          margin-right:0in;
				          margin-bottom:22.0pt;
				          margin-left:0in;
				          mso-line-height-alt:12.0pt;
				          mso-pagination:widow-orphan;
				          border:none;
				          mso-border-bottom-alt:solid windowtext .75pt;
				          padding:0in;
				          mso-padding-alt:0in 0in 4.0pt 0in;
				          font-size:27.0pt;
				          mso-bidi-font-size:10.0pt;
				          font-family:"Arial Black";
				          mso-fareast-font-family:Batang;
				          mso-bidi-font-family:"Times New Roman";
				          letter-spacing:-1.75pt;}
			          /* Style Definitions */
			          table.MsoNormalTable
				          {mso-style-name:"Table Normal";
				          mso-tstyle-rowband-size:0;
				          mso-tstyle-colband-size:0;
				          mso-style-noshow:yes;
				          mso-style-parent:"";
				          mso-padding-alt:0in 5.4pt 0in 5.4pt;
				          mso-para-margin:0in;
				          mso-para-margin-bottom:.0001pt;
				          mso-pagination:widow-orphan;
				          font-size:10.0pt;
				          font-family:"Times New Roman";
				          mso-ansi-language:#0400;
				          mso-fareast-language:#0400;
				          mso-bidi-language:#0400;}
			          p.Address2, li.Address2, div.Address2
				          {mso-style-name:"Address 2";
				          margin:0in;
				          margin-bottom:.0001pt;
				          text-align:left;
				          text-justify:inter-ideograph;
				          line-height:8.0pt;
				          mso-pagination:widow-orphan;
				          font-size:7.0pt;
				          mso-bidi-font-size:10.0pt;
				          font-family:Arial;
				          mso-fareast-font-family:Batang;
				          mso-bidi-font-family:"Times New Roman";}
			          p.Address1, li.Address1, div.Address1
				          {mso-style-name:"Address 1";
				          margin:0in;
				          margin-bottom:.0001pt;
				          text-align:justify;
				          text-justify:inter-ideograph;
				          line-height:8.0pt;
				          mso-pagination:widow-orphan;
				          font-size:7.0pt;
				          mso-bidi-font-size:10.0pt;
				          font-family:Arial;
				          mso-fareast-font-family:Batang;
				          mso-bidi-font-family:"Times New Roman";}
			          /* Page Definitions */
			          div.Section1
				          {page:Section1;}
			          p.SectionTitle, li.SectionTitle, div.SectionTitle
				          {mso-style-name:"Section Title";
				          mso-style-update:auto;
				          mso-style-next:Normal;
				          margin-top:11.0pt;
				          margin-right:0in;
				          margin-bottom:0in;
				          margin-left:0in;
				          margin-bottom:.0001pt;
				          line-height:11.0pt;
				          mso-pagination:widow-orphan;
				          font-size:10.0pt;
				          font-family:"Arial Black";
				          mso-fareast-font-family:Batang;
				          mso-bidi-font-family:"Times New Roman";
				          letter-spacing:-.5pt;}
			          p.NoTitle, li.NoTitle, div.NoTitle
				          {mso-style-name:"No Title";
				          mso-style-parent:"Section Title";
				          margin-top:11.0pt;
				          margin-right:0in;
				          margin-bottom:0in;
				          margin-left:0in;
				          margin-bottom:.0001pt;
				          line-height:11.0pt;
				          mso-pagination:widow-orphan;
				          font-size:10.0pt;
				          font-family:"Arial Black";
				          mso-fareast-font-family:Batang;
				          mso-bidi-font-family:"Times New Roman";
				          letter-spacing:-.5pt;}
			          p.Objective, li.Objective, div.Objective
				          {mso-style-name:Objective;
				          mso-style-next:"Body Text";
				          margin-top:12.0pt;
				          margin-right:0in;
				          margin-bottom:11.0pt;
				          margin-left:0in;
				          line-height:11.0pt;
				          mso-pagination:widow-orphan;
				          font-size:10.0pt;
				          font-family:Arial;
				          mso-fareast-font-family:Batang;
				          mso-bidi-font-family:"Times New Roman";}
			          p.PersonalData, li.PersonalData, div.PersonalData
				          {mso-style-name:"Personal Data";
				          mso-style-parent:"Body Text";
				          margin-top:0in;
				          margin-right:.75in;
				          margin-bottom:6.0pt;
				          margin-left:-.75in;
				          text-align:justify;
				          text-justify:inter-ideograph;
				          line-height:12.0pt;
				          mso-line-height-rule:exactly;
				          mso-pagination:widow-orphan;
				          font-size:11.0pt;
				          mso-bidi-font-size:10.0pt;
				          font-family:Arial;
				          mso-fareast-font-family:Batang;
				          mso-bidi-font-family:"Times New Roman";
				          font-style:italic;
				          mso-bidi-font-style:normal;}
			          p.PersonalInfo, li.PersonalInfo, div.PersonalInfo
				          {mso-style-name:"Personal Info";
				          mso-style-parent:Achievement;
				          mso-style-next:Achievement;
				          margin-top:12.0pt;
				          margin-right:12.25pt;
				          margin-bottom:3.0pt;
				          margin-left:12.25pt;
				          text-align:justify;
				          text-justify:inter-ideograph;
				          text-indent:-12.25pt;
				          line-height:11.0pt;
				          mso-pagination:widow-orphan;
				          font-size:10.0pt;
				          font-family:Arial;
				          mso-fareast-font-family:Batang;
				          mso-bidi-font-family:"Times New Roman";
				          letter-spacing:-.25pt;}
			          p.SectionSubtitle, li.SectionSubtitle, div.SectionSubtitle
				          {mso-style-name:"Section Subtitle";
				          mso-style-parent:"Section Title";
				          mso-style-next:Normal;
				          margin-top:11.0pt;
				          margin-right:0in;
				          margin-bottom:0in;
				          margin-left:0in;
				          margin-bottom:.0001pt;
				          line-height:11.0pt;
				          mso-pagination:widow-orphan;
				          font-size:10.0pt;
				          font-family:"Arial Black";
				          mso-fareast-font-family:Batang;
				          mso-bidi-font-family:"Times New Roman";
				          font-weight:bold;
				          mso-bidi-font-weight:normal;}
			          p.CompanyName, li.CompanyName, div.CompanyName
				          {mso-style-name:"Company Name";
				          mso-style-update:auto;
				          mso-style-next:Normal;
				          margin-top:12.0pt;
				          margin-right:0in;
				          margin-bottom:2.0pt;
				          margin-left:0in;
				          line-height:11.0pt;
				          mso-pagination:widow-orphan;
				          tab-stops:1.5in right 4.5in;
				          font-size:10.0pt;
				          font-family:Arial;
				          mso-fareast-font-family:Batang;
				          mso-bidi-font-family:"Times New Roman";}
			          p.CompanyNameOne, div.CompanyNameOne, .CompanyTable
				          {mso-style-name:"Company Name One";
				          mso-style-update:auto;
				          mso-style-parent:"Company Name";
				          mso-style-next:Normal;
				          margin-top:12.0pt;
				          margin-right:0in;
				          margin-bottom:2.0pt;
				          margin-left:0in;
				          line-height:11.0pt;
				          mso-pagination:widow-orphan;
				          tab-stops:1.5in right 4.5in;
				          font-size:10.0pt;
				          font-family:Arial;
				          mso-fareast-font-family:Batang;
				          mso-bidi-font-family:"Times New Roman";}
			          p.JobTitle, li.JobTitle, div.JobTitle
				          {mso-style-name:"Job Title";
				          mso-style-parent:"";
				          mso-style-next:Achievement;
				          margin-top:0in;
				          margin-right:0in;
				          margin-bottom:3.0pt;
				          margin-left:0in;
				          line-height:11.0pt;
				          mso-pagination:widow-orphan;
				          font-size:10.0pt;
				          font-family:"Arial Black";
				          mso-fareast-font-family:Batang;
				          mso-bidi-font-family:"Times New Roman";
				          letter-spacing:-.5pt;}
			          p.Institution, li.Institution, div.Institution
				          {mso-style-name:Institution;
				          mso-style-update:auto;
				          mso-style-next:Achievement;
				          margin-top:12.0pt;
				          margin-right:0in;
				          margin-bottom:3.0pt;
				          margin-left:0in;
				          line-height:11.0pt;
				          mso-pagination:widow-orphan;
				          tab-stops:1.5in right 4.5in;
				          font-size:10.0pt;
				          font-family:Arial;
				          mso-fareast-font-family:Batang;
				          mso-bidi-font-family:"Times New Roman";}
			          p.Achievement, li.Achievement, div.Achievement, ul.Achievement
				          {list-style-type:	square;
				          mso-style-name:Achievement;
				          mso-style-parent:'Body Text';
				          font-size:10.0pt;
				          font-family:Arial;
				          text-indent:-36.0pt;
				          mso-list:l0 level1 lfo1;}
			          li           { list-style-type: square; text-align: left; font-family:Arial; font-size:10pt }
			          .RightSide
			          {
				          width:333.35pt;
				          padding:0in 5.4pt 0in 5.4pt;
				          vertical-align:top;
			          }
			          .CompanyDate
			          {
				          width:125;
			          }
			          .CompanyName
			          {
				          width:225;
			          }
			          .CompanyCityState
			          {
				          text-align:right;
			          }
			          .CompanyTable
			          {
				          width:375pt;
			          }
			          .Right
			          {
				          vertical-align:	top;
			          }
		          </style>
              <!--End of style sheets-->'''
    def BodyTag(self) -> str:
        return self.BodyStartTag() + '''
                <div class="Section1">
                    <table 
                        class="MsoNormalTable" 
                        border="0" 
                        cellspacing="0" 
                        cellpadding="0"
                        style='border-collapse:collapse;mso-padding-alt:0in 5.4pt 0in 5.4pt'>
                        ''' + self.BodyHeading() + self.BodyObj() + self.BodyPortfolio() + self.BodySkills() + self.BodyJobHistory() + self.BodyEducation() + self.BodyFooter() + '''
                    </table>
                </div>
            ''' + self.BodyEndTag()
    def BodyHeading(self):
        return '''
                <!--Heading information-->
                <tr style='mso-yfti-irow:0;mso-yfti-firstrow:yes;mso-yfti-lastrow:yes'>
                    <td width="144" valign="top" style='width:1.5in;padding:0in 5.4pt 0in 5.4pt'>
                        <p class="Address2">
                            ''' + self.jobseeker.Address + '''&nbsp;<br />
                            ''' + self.jobseeker.City + ''',&nbsp;''' + self.jobseeker.StateOrProvince + '''&nbsp;''' + self.jobseeker.PostalCode + '''&nbsp;
                        </p>
                    </td>
                    <td class="Right">
                        <p class="Address1">
                            ''' + self.jobseeker.HomePhone + '''&#149;<a href="mailto: ''' + self.jobseeker.EmailName + '''">''' + self.jobseeker.EmailName + '''</a>
                            <!--http://resumedrafter.somee.com/Jobseeker/View/@jobseeker.JobseekerID-->
                        </p>
                    </td>
                </tr>
            </table>
            <!--Jobseeker's Full Name-->
            <div 
                style=
                    '
                        mso-element:para-border-div;
                        border:none;
                        border-bottom:solid windowtext 1.0pt;
                        mso-border-bottom-alt:solid windowtext .75pt;
                        padding:0in 0in 4.0pt 0in
                    '>
                <p class="Name">
                <!--ENTER JOB SEEKER FULL NAME HERE...-->
                ''' + self.jobseeker.FirstName + '''&nbsp;''' + self.jobseeker.LastName + '''
                </p>
            </div>
            <!--End Jobseeker's Full Name-->
            <!--End of formating the heading information-->
        '''
    def BodyObj(self):
        return '''<!--Objective-->
	 				    <tr style='mso-yfti-irow:0;mso-yfti-firstrow:yes'>
					  	    <td width="144" valign="top" style='width:1.5in;padding:0in 5.4pt 0in 5.4pt'>
					  		    <p class="SectionTitle">Objective</p>
						    </td>
						    <td class="Right">
							    <p class="Objective">''' + self.jobseeker.objective.ObjectiveDescription + '''</p>
						    </td>
					    </tr>
					    <!--End of Objective-->'''
    def BodyPortfolio(self) -> str:
        ret:str = '''
                    <!--Portfolio-->
                    <tr valign="top">
                        <td width="144" style='width:1.5in;padding:0in 5.4pt 0in 5.4pt'>
                            <p class="SectionTitle" style="margin-top:0pt;">Portfolio</p>
                        </td>
                        <td class="Right">
                            <div>
                                <!--ENTER SKILLS DESCRIPTION HERE...-->
                                <ul>'''
        for val in self.jobseeker.portfolios:
            ret = ret + '''
                                    <li><a href="''' + val[Portfolio.SITE_ADDR] + '''">''' + val[Portfolio.SITE_ADDR] + '''</a></li>'''
        ret = ret + '''
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
                    <tr valign="top">
                        <td width="144" style='width:1.5in;padding:0in 5.4pt 0in 5.4pt'>
                            <p class="SectionTitle" style="margin-top:0pt;">Skills</p>
                        </td>
                        <td class="Right">
                            <div>
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
                    <tr style='mso-yfti-irow:1'>
                        <td width="144" valign="top" style='width:1.5in;padding:0in 5.4pt 0in 5.4pt'>
                            <p class="SectionTitle">Experience</p>
                        </td>
                        <td class="Right">'''
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
            try:
                ret = ret + '''
                            <table class="CompanyTable">
                                <tr>
                                    <td class="CompanyDate">
                                        <!--INSERT START AND END DATE HERE...-->
                                        ''' + startDate + '''&nbsp;-&nbsp;''' + endDate + '''    
                                    </td>
                                    <td class="CompanyName">
                                        ''' + var[JobHistory.COMPANY_NAME] + '''
                                    </td>
                                    <td class="CompanyCityState">
                                        <!--INSERT CITY AND STATE HERE...-->
                                        ''' + cityState + '''
                                    </td>
                                </tr>
                            </table>
                            <!--Job Title-->
                            <p class="JobTitle">
                                ''' + var[JobHistory.JOB_TITLE] + '''
                            </p>
                            <!--Job Responsibilities-->
                            
                            <div>
                                <ul>'''
            except:
                ret = ret + '''
							<!-- JOB HISTORY ERROR OCCURRED	-->
							'''
							
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
					    <tr style='mso-yfti-irow:5'>
						    <td width="144" valign="top" style='width:1.5in;padding:0in 5.4pt 0in 5.4pt'>
							    <p class="SectionTitle">Education</p></td><td width="444" valign="top" style='width:333.35pt;padding:0in 5.4pt 0in 5.4pt'>
                    '''
        for val in self.jobseeker.education:
            try:
                startDate:str = val[Education.START_DATE].strftime('%m/%d/%Y')
            except:
                startDate = val[Education.START_DATE]
            try:
                endDate:str = val[Education.END_DATE].strftime('%m/%d/%Y')
            except:
                endDate = Education.DEFAULT_ATTENDANCE_TXT

            ret = ret +         '''<table class="CompanyTable">
		    	 	 			    <tr>
		    	 	 				    <td class="CompanyDate">
		    	 	 					    <!--Date Range-->''' +	startDate + '''&nbsp;-&nbsp;''' + endDate  + '''
                          				</td>
		    	 	 				    <td class="CompanyName">
		    	 	 						<!--School Name-->
                                            ''' + val[Education.SCHOOL_NAME] + '''
                                        </td>
										<td class="CompanyCityState">
										    <!--City and State--> +
                                            ''' + val[Education.CITY] + ''',&nbsp;''' + val[Education.STATE] + '''
                                        </td>
		    	 	 			    </tr>
		    	 	 			</table>
								<!--Degrees and Honors-->
								<ul>
									<li>''' + val[Education.DEGREE] + '''</li>
		                        </ul>	'''
        ret = ret +	'''
                            </td>
					    </tr>
					    <!--End of Education-->'''
        return ret
    def BodyFooter(self) -> str:
        return ''''''