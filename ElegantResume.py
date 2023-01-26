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

class ElegantResume(Resume):
    def __init__(self, jobseeker: Jobseeker) -> None:
        super().__init__(jobseeker)
        self.resumeType=Resume.ELEGANT
    def StyleTag(self) -> str:
        return '''<!--Style Sheets-->
	  	          <style type="text/css">
			            p.MsoNormal, li.MsoNormal, div.MsoNormal
				            {mso-style-parent:"";
				            margin:0in;
				            margin-bottom:.0001pt;
				            text-align:justify;
				            mso-pagination:widow-orphan;
				            font-size:11.0pt;
				            mso-bidi-font-size:10.0pt;
				            font-family:Garamond;
				            mso-fareast-font-family:"Times New Roman";
				            mso-bidi-font-family:"Times New Roman";}
			            h1
				            {mso-style-parent:"Heading Base";
				            mso-style-next:"Body Text";
				            margin-top:12.0pt;
				            margin-right:0in;
				            margin-bottom:12.0pt;
				            margin-left:-1.5in;
				            line-height:12.0pt;
				            mso-pagination:widow-orphan lines-together;
				            page-break-after:avoid;
				            mso-outline-level:1;
				            font-size:11.5pt;
				            mso-bidi-font-size:10.0pt;
				            font-family:Garamond;
				            text-transform:uppercase;
				            letter-spacing:1.0pt;
				            mso-font-kerning:14.0pt;
				            font-weight:normal;}
			            h2
				            {mso-style-parent:"Heading Base";
				            mso-style-next:"Body Text";
				            margin-top:12.0pt;
				            margin-right:0in;
				            margin-bottom:12.0pt;
				            margin-left:0in;
				            line-height:12.0pt;
				            mso-pagination:widow-orphan lines-together;
				            page-break-after:avoid;
				            mso-outline-level:2;
				            font-size:10.0pt;
				            font-family:Garamond;
				            text-transform:uppercase;
				            letter-spacing:.25pt;
				            font-weight:normal;}
			            h3
				            {mso-style-parent:"Heading Base";
				            mso-style-next:"Body Text";
				            margin-top:12.0pt;
				            margin-right:0in;
				            margin-bottom:11.0pt;
				            margin-left:0in;
				            line-height:12.0pt;
				            mso-pagination:widow-orphan lines-together;
				            page-break-after:avoid;
				            mso-outline-level:3;
				            font-size:10.0pt;
				            font-family:Garamond;
				            text-transform:uppercase;
				            letter-spacing:-.1pt;
				            font-weight:normal;
				            font-style:italic;
				            mso-bidi-font-style:normal;}
			            h4
				            {mso-style-parent:"Heading Base";
				            mso-style-next:"Body Text";
				            margin-top:12.0pt;
				            margin-right:0in;
				            margin-bottom:0in;
				            margin-left:0in;
				            margin-bottom:.0001pt;
				            line-height:12.0pt;
				            mso-pagination:widow-orphan lines-together;
				            page-break-after:avoid;
				            mso-outline-level:4;
				            font-size:12.0pt;
				            mso-bidi-font-size:10.0pt;
				            font-family:Garamond;
				            letter-spacing:.25pt;
				            font-weight:normal;
				            font-style:italic;
				            mso-bidi-font-style:normal;}
			            h5
				            {mso-style-parent:"Heading Base";
				            mso-style-next:"Body Text";
				            margin-top:12.0pt;
				            margin-right:0in;
				            margin-bottom:11.0pt;
				            margin-left:0in;
				            line-height:12.0pt;
				            mso-pagination:widow-orphan lines-together;
				            page-break-after:avoid;
				            mso-outline-level:5;
				            font-size:9.0pt;
				            mso-bidi-font-size:10.0pt;
				            font-family:Garamond;
				            text-transform:uppercase;
				            letter-spacing:1.0pt;
				            mso-bidi-font-weight:normal;}
			            h6
				            {mso-style-next:Normal;
				            margin-top:12.0pt;
				            margin-right:0in;
				            margin-bottom:0in;
				            margin-left:0in;
				            margin-bottom:.0001pt;
				            text-align:justify;
				            line-height:12.0pt;
				            mso-pagination:widow-orphan;
				            mso-outline-level:6;
				            font-size:11.0pt;
				            mso-bidi-font-size:10.0pt;
				            font-family:Garamond;
				            mso-bidi-font-weight:normal;}
			            p.MsoHeader, li.MsoHeader, div.MsoHeader
				            {mso-style-parent:"Header Base";
				            margin-top:11.0pt;
				            margin-right:0in;
				            margin-bottom:11.0pt;
				            margin-left:-1.5in;
				            text-align:justify;
				            line-height:11.0pt;
				            mso-pagination:widow-orphan;
				            font-size:11.0pt;
				            mso-bidi-font-size:10.0pt;
				            font-family:Garamond;
				            mso-fareast-font-family:"Times New Roman";
				            mso-bidi-font-family:"Times New Roman";
				            text-transform:uppercase;}
			            p.MsoFooter, li.MsoFooter, div.MsoFooter
				            {mso-style-parent:"Header Base";
				            margin-top:11.0pt;
				            margin-right:-42.0pt;
				            margin-bottom:11.0pt;
				            margin-left:-1.5in;
				            line-height:12.0pt;
				            mso-pagination:widow-orphan;
				            tab-stops:right 366.0pt;
				            font-size:11.0pt;
				            mso-bidi-font-size:10.0pt;
				            font-family:Garamond;
				            mso-fareast-font-family:"Times New Roman";
				            mso-bidi-font-family:"Times New Roman";
				            text-transform:uppercase;}
			            span.MsoPageNumber
				            {mso-style-parent:"";
				            mso-ansi-font-size:12.0pt;}
			            p.MsoBodyText, li.MsoBodyText, div.MsoBodyText
				            {margin-top:0in;
				            margin-right:0in;
				            margin-bottom:11.0pt;
				            margin-left:0in;
				            text-align:justify;
				            line-height:12.0pt;
				            mso-pagination:widow-orphan;
				            font-size:11.0pt;
				            mso-bidi-font-size:10.0pt;
				            font-family:Garamond;
				            mso-fareast-font-family:"Times New Roman";
				            mso-bidi-font-family:"Times New Roman";}
			            p.MsoBodyTextIndent, li.MsoBodyTextIndent, div.MsoBodyTextIndent
				            {mso-style-parent:"Body Text";
				            margin-top:0in;
				            margin-right:0in;
				            margin-bottom:11.0pt;
				            margin-left:.5in;
				            text-align:justify;
				            line-height:12.0pt;
				            mso-pagination:widow-orphan;
				            font-size:11.0pt;
				            mso-bidi-font-size:10.0pt;
				            font-family:Garamond;
				            mso-fareast-font-family:"Times New Roman";
				            mso-bidi-font-family:"Times New Roman";}
			            p.MsoDate, li.MsoDate, div.MsoDate
				            {mso-style-parent:"Body Text";
				            margin-top:0in;
				            margin-right:0in;
				            margin-bottom:11.0pt;
				            margin-left:0in;
				            text-align:justify;
				            line-height:12.0pt;
				            mso-pagination:widow-orphan;
				            page-break-after:avoid;
				            font-size:11.0pt;
				            mso-bidi-font-size:10.0pt;
				            font-family:Garamond;
				            mso-fareast-font-family:"Times New Roman";
				            mso-bidi-font-family:"Times New Roman";}
			            em
				            {mso-style-parent:"";
				            mso-ansi-font-size:9.0pt;
				            font-family:Garamond;
				            mso-ascii-font-family:Garamond;
				            mso-hansi-font-family:Garamond;
				            text-transform:uppercase;
				            letter-spacing:0pt;
				            font-style:normal;}
			            p.MsoAcetate, li.MsoAcetate, div.MsoAcetate
				            {mso-style-noshow:yes;
				            margin:0in;
				            margin-bottom:.0001pt;
				            text-align:justify;
				            mso-pagination:widow-orphan;
				            font-size:8.0pt;
				            font-family:Tahoma;
				            mso-fareast-font-family:"Times New Roman";}
			            p.HeadingBase, li.HeadingBase, div.HeadingBase
				            {mso-style-name:"Heading Base";
				            mso-style-parent:"Body Text";
				            mso-style-next:"Body Text";
				            margin-top:12.0pt;
				            margin-right:0in;
				            margin-bottom:12.0pt;
				            margin-left:0in;
				            text-align:justify;
				            line-height:12.0pt;
				            mso-pagination:widow-orphan lines-together;
				            page-break-after:avoid;
				            font-size:11.0pt;
				            mso-bidi-font-size:10.0pt;
				            font-family:Garamond;
				            mso-fareast-font-family:"Times New Roman";
				            mso-bidi-font-family:"Times New Roman";
				            text-transform:uppercase;}
			            p.HeaderBase, li.HeaderBase, div.HeaderBase
				            {mso-style-name:"Header Base";
				            margin-top:11.0pt;
				            margin-right:0in;
				            margin-bottom:11.0pt;
				            margin-left:-1.5in;
				            text-align:justify;
				            line-height:11.0pt;
				            mso-pagination:widow-orphan;
				            font-size:11.0pt;
				            mso-bidi-font-size:10.0pt;
				            font-family:Garamond;
				            mso-fareast-font-family:"Times New Roman";
				            mso-bidi-font-family:"Times New Roman";
				            text-transform:uppercase;}
			            p.DocumentLabel, li.DocumentLabel, div.DocumentLabel
				            {mso-style-name:"Document Label";
				            mso-style-next:"Section Title";
				            margin-top:0in;
				            margin-right:0in;
				            margin-bottom:11.0pt;
				            margin-left:0in;
				            text-align:justify;
				            mso-pagination:widow-orphan;
				            font-size:24.0pt;
				            mso-bidi-font-size:10.0pt;
				            font-family:Garamond;
				            mso-fareast-font-family:"Times New Roman";
				            mso-bidi-font-family:"Times New Roman";
				            letter-spacing:-1.0pt;}
			            p.SectionTitle, li.SectionTitle, div.SectionTitle
				            {mso-style-name:"Section Title";
				            mso-style-next:Objective;
				            margin-top:11.0pt;
				            margin-right:0in;
				            margin-bottom:0in;
				            margin-left:0in;
				            margin-bottom:.0001pt;
				            line-height:11.0pt;
				            mso-pagination:widow-orphan;
				            border:none;
				            mso-border-bottom-alt:solid gray .75pt;
				            padding:0in;
				            mso-padding-alt:0in 0in 1.0pt 0in;
				            font-size:10.0pt;
				            font-family:Garamond;
				            mso-fareast-font-family:"Times New Roman";
				            mso-bidi-font-family:"Times New Roman";
				            text-transform:uppercase;
				            letter-spacing:.75pt;}
			            p.Objective, li.Objective, div.Objective
				            {mso-style-name:Objective;
				            mso-style-next:"Body Text";
				            margin-top:3.0pt;
				            margin-right:0in;
				            margin-bottom:11.0pt;
				            margin-left:0in;
				            text-align:justify;
				            line-height:11.0pt;
				            mso-pagination:widow-orphan;
				            font-size:11.0pt;
				            mso-bidi-font-size:10.0pt;
				            font-family:Garamond;
				            mso-fareast-font-family:"Times New Roman";
				            mso-bidi-font-family:"Times New Roman";}
			            p.CompanyName, li.CompanyName, div.CompanyName
				            {mso-style-name:"Company Name";
				            mso-style-next:"Job Title";
				            margin-top:11.0pt;
				            margin-right:0in;
				            margin-bottom:0in;
				            margin-left:0in;
				            margin-bottom:.0001pt;
				            line-height:11.0pt;
				            mso-pagination:widow-orphan;
				            tab-stops:1.0in right 4.5in;
				            font-size:11.0pt;
				            mso-bidi-font-size:10.0pt;
				            font-family:Garamond;
				            mso-fareast-font-family:"Times New Roman";
				            mso-bidi-font-family:"Times New Roman";}
			            p.JobTitle, li.JobTitle, div.JobTitle
				            {mso-style-name:"Job Title";
				            mso-style-parent:"";
				            mso-style-next:Achievement;
				            margin-top:2.0pt;
				            margin-right:0in;
				            margin-bottom:2.0pt;
				            margin-left:0in;
				            mso-line-height-alt:11.0pt;
				            mso-pagination:widow-orphan;
				            font-size:11.5pt;
				            mso-bidi-font-size:10.0pt;
				            font-family:Garamond;
				            mso-fareast-font-family:"Times New Roman";
				            mso-bidi-font-family:"Times New Roman";
				            letter-spacing:.25pt;
				            font-style:italic;
				            mso-bidi-font-style:normal;}
			            p.Achievement, div.Achievement
				            {mso-style-name:Achievement;
				            mso-style-parent:"Body Text";
				            margin-top:0in;
				            margin-right:0in;
				            margin-bottom:3.0pt;
				            margin-left:12.0pt;
				            text-align:justify;
				            text-indent:-12.0pt;
				            line-height:12.0pt;
				            mso-pagination:widow-orphan;
				            mso-list:l0 level1 lfo2;
				            font-size:11.0pt;
				            mso-bidi-font-size:10.0pt;
				            font-family:Garamond;
				            mso-fareast-font-family:"Times New Roman";
				            mso-bidi-font-family:"Times New Roman";}
			            p.Name, li.Name, div.Name
				            {mso-style-name:Name;
				            mso-style-next:Normal;
				            margin-top:0in;
				            margin-right:0in;
				            margin-bottom:22.0pt;
				            margin-left:0in;
				            text-align:center;
				            mso-line-height-alt:12.0pt;
				            mso-pagination:widow-orphan;
				            font-size:22.0pt;
				            mso-bidi-font-size:10.0pt;
				            font-family:Garamond;;
				            letter-spacing:4.0pt;}
			            p.CityState, li.CityState, div.CityState
				            {mso-style-name:"City\/
				            mso-fareast-font-family:"Times New Roman";
				            mso-bidi-font-family:"Times New Roman";
				            text-transform:uppercaseState";
				            mso-style-parent:"Body Text";
				            mso-style-next:"Body Text";
				            margin-top:0in;
				            margin-right:0in;
				            margin-bottom:11.0pt;
				            margin-left:0in;
				            text-align:justify;
				            line-height:12.0pt;
				            mso-pagination:widow-orphan;
				            page-break-after:avoid;
				            font-size:11.0pt;
				            mso-bidi-font-size:10.0pt;
				            font-family:Garamond;
				            mso-fareast-font-family:"Times New Roman";
				            mso-bidi-font-family:"Times New Roman";}
			            p.Institution, li.Institution, div.Institution
				            {mso-style-name:Institution;
				            mso-style-next:Achievement;
				            margin-top:3.0pt;
				            margin-right:0in;
				            margin-bottom:0in;
				            margin-left:0in;
				            margin-bottom:.0001pt;
				            line-height:11.0pt;
				            mso-pagination:widow-orphan;
				            tab-stops:1.0in right 4.5in;
				            font-size:11.0pt;
				            mso-bidi-font-size:10.0pt;
				            font-family:Garamond;
				            mso-fareast-font-family:"Times New Roman";
				            mso-bidi-font-family:"Times New Roman";}
			            span.Lead-inEmphasis
				            {mso-style-name:"Lead-in Emphasis";
				            mso-style-parent:"";
				            mso-ansi-font-size:9.0pt;
				            font-family:"Arial Black";
				            mso-ascii-font-family:"Arial Black";
				            mso-hansi-font-family:"Arial Black";
				            letter-spacing:-.3pt;}
			            p.Address1, li.Address1, div.Address1
				            {mso-style-name:"Address 1";
				            margin:0in;
				            margin-bottom:.0001pt;
				            text-align:center;
				            line-height:8.0pt;
				            mso-pagination:widow-orphan;
				            font-size:7.5pt;
				            mso-bidi-font-size:10.0pt;
				            font-family:Garamond;
				            mso-fareast-font-family:"Times New Roman";
				            mso-bidi-font-family:"Times New Roman";
				            text-transform:uppercase;
				            letter-spacing:1.5pt;}
			            p.SectionSubtitle, li.SectionSubtitle, div.SectionSubtitle
				            {mso-style-name:"Section Subtitle";
				            mso-style-parent:"Section Title";
				            mso-style-next:Normal;
				            margin-top:11.0pt;
				            margin-right:0in;
				            margin-bottom:0in;
				            margin-left:0in;
				            margin-bottom:.0001pt;
				            mso-line-height-alt:11.0pt;
				            mso-pagination:widow-orphan;
				            border:none;
				            mso-border-bottom-alt:solid gray .75pt;
				            padding:0in;
				            mso-padding-alt:0in 0in 1.0pt 0in;
				            font-size:12.0pt;
				            mso-bidi-font-size:10.0pt;
				            font-family:Garamond;
				            mso-fareast-font-family:"Times New Roman";
				            mso-bidi-font-family:"Times New Roman";
				            letter-spacing:.5pt;
				            font-style:italic;
				            mso-bidi-font-style:normal;}
			            p.Address2, li.Address2, div.Address2
				            {mso-style-name:"Address 2";
				            margin:0in;
				            margin-bottom:.0001pt;
				            text-align:center;
				            line-height:8.0pt;
				            mso-pagination:widow-orphan;
				            font-size:7.5pt;
				            mso-bidi-font-size:10.0pt;
				            font-family:Garamond;
				            mso-fareast-font-family:"Times New Roman";
				            mso-bidi-font-family:"Times New Roman";
				            text-transform:uppercase;
				            letter-spacing:1.5pt;}
			            span.Job
				            {mso-style-name:Job;}
			            p.PersonalData, li.PersonalData, div.PersonalData
				            {mso-style-name:"Personal Data";
				            mso-style-parent:"Body Text";
				            margin-top:0in;
				            margin-right:.75in;
				            margin-bottom:6.0pt;
				            margin-left:-.75in;
				            text-align:justify;
				            line-height:12.0pt;
				            mso-line-height-rule:exactly;
				            mso-pagination:widow-orphan;
				            font-size:11.0pt;
				            mso-bidi-font-size:10.0pt;
				            font-family:Arial;
				            mso-fareast-font-family:"Times New Roman";
				            mso-bidi-font-family:"Times New Roman";
				            font-style:italic;
				            mso-bidi-font-style:normal;}
			            p.CompanyNameOne, li.CompanyNameOne, div.CompanyNameOne, .CompanyTable
				            {mso-style-name:"Company Name One";
				            mso-style-parent:"Company Name";
				            mso-style-next:"Job Title";
				            margin-top:3.0pt;
				            margin-right:0in;
				            margin-bottom:0in;
				            margin-left:0in;
				            margin-bottom:.0001pt;
				            line-height:11.0pt;
				            mso-pagination:widow-orphan;
				            tab-stops:1.0in right 4.5in;
				            font-size:11.0pt;
				            mso-bidi-font-size:10.0pt;
				            font-family:Garamond;
				            mso-fareast-font-family:"Times New Roman";
				            mso-bidi-font-family:"Times New Roman";}
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
				            font-family:Garamond;
				            mso-fareast-font-family:"Times New Roman";
				            mso-bidi-font-family:"Times New Roman";
				            text-transform:uppercase;
				            letter-spacing:.75pt;}
			            p.PersonalInfo, li.PersonalInfo, div.PersonalInfo
				            {mso-style-name:"Personal Info";
				            mso-style-parent:Achievement;
				            mso-style-next:Achievement;
				            margin-top:11.0pt;
				            margin-right:0in;
				            margin-bottom:3.0pt;
				            margin-left:12.25pt;
				            text-align:justify;
				            text-indent:-12.25pt;
				            line-height:12.0pt;
				            mso-pagination:widow-orphan;
				            mso-list:l0 level1 lfo2;
				            font-size:11.0pt;
				            mso-bidi-font-size:10.0pt;
				            font-family:Garamond;
				            mso-fareast-font-family:"Times New Roman";
				            mso-bidi-font-family:"Times New Roman";}
			            .SectionTitleDiv
			            {
				            mso-element:para-border-div;
				            border:none;
				            border-bottom:solid gray 1.0pt;
				            mso-border-bottom-alt:solid gray .75pt;
				            padding:0in 0in 1.0pt 0in;
			            }
			            li.Achievement
			            {
				            mso-style-name:Achievement;
				            mso-style-parent:"Body Text";
				            margin-top:0in;
				            margin-right:0in;
				            margin-bottom:3.0pt;
				            margin-left:0.0pt;
				            text-align:justify;
				            text-indent:-36.0pt;
				            line-height:12.0pt;
				            mso-pagination:widow-orphan;
				            font-size:11.0pt;
				            mso-bidi-font-size:10.0pt;
				            font-family:Garamond;
				            mso-fareast-font-family:"Times New Roman";
				            mso-bidi-font-family:"Times New Roman";
				            list-style-type:	square;
			            }
			         li
			         {
			             list-style-type:square;
			             font-size:11.0pt;
			             font-family:Garamond;
			             margin:0in 0in 3pt 0pt;
			             padding:0px 0px 0px 0px;
			         }
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
			            width:205;
		            }
		            .CompanyCityState
		            {
			            text-align:right;
		            }
		            .CompanyTable
		            {
			            width:330pt;
		            }
		            .CompanyDate, .CompanyName, .CompanyCityState
		            {
			            vertical-align:	top;
		            }
		          </style>
              <!--End of style sheets-->'''
    def BodyTag(self) -> str:
        return self.BodyStartTag() + '''
                <div class="Section1">
                    ''' + self.BodyHeading() + '''
                    <table 
                        class="MsoNormalTable" 
                        border="0" 
                        cellspacing="0" 
                        cellpadding="0" 
                        width="100%" 
                        style="width:100.0%;border-collapse:collapse;mso-padding-alt:0in 5.4pt 0in 5.4pt">
                    ''' + self.BodyObj() + self.BodyPortfolio() + self.BodySkills() + self.BodyJobHistory() + self.BodyEducation() + self.BodyFooter() + '''
                    </table>
                    <!--<br style="page-break-after: always;" />-->
                </div>
            ''' + self.BodyEndTag()
    def BodyHeading(self):
        return '''
            <!--Heading information-->
            <!--Jobseeker's Full Name-->
            <p class="Name">
            <!--ENTER JOB SEEKER FULL NAME HERE...-->
            ''' + self.jobseeker.FirstName + '&nbsp;' + self.jobseeker.LastName + '''</p>
            <!--End Jobseeker's Full Name-->
            <!--End of formating the heading information-->
            '''
    def BodyObj(self):
        return '''<!--Objective-->
				            <tr style='mso-yfti-irow:0;mso-yfti-firstrow:yes;page-break-inside:avoid'>
			  		            <td width="100%" colspan="2" valign="top" style="width:100.0%;padding:0in 5.4pt 0in 5.4pt">
			  			            <div 
			  				            style=
			  					            "
			  						            mso-element:para-border-div;
			  						            border:none;
			  						            border-bottom:solid gray 1.0pt;
			  						            mso-border-bottom-alt:solid gray .75pt;
			  						            padding:0in 0in 1.0pt 0in
			  					            ">
			  				            <p class="SectionTitle">objective</p>
					  	            </div>
					              </td>
				             </tr>
			 	            <tr style='mso-yfti-irow:1;mso-row-margin-right:.08%'>
					            <td width="24%" valign="top" style='width:24.44%;padding:0in 5.4pt 0in 5.4pt'>
						            <p class="NoTitle"></p>
					            </td>
					            <td class="RightSide">
						            <p class="Objective">''' + self.jobseeker.objective.ObjectiveDescription + '''</p>
					            </td>					
				            </tr>
			 	            <!--End of Objective-->'''
    def BodyPortfolio(self) -> str:
        ret:str = '''
                    <!--Portfolio-->
                    <tr style='mso-yfti-irow:2;page-break-inside:avoid'>
                        <td width="100%" colspan="2" valign="top" style='width:100.0%;padding:0in 5.4pt 0in 5.4pt'>
                            <div class="SectionTitleDiv">
                                <p class="SectionTitle">Portfolio</p>
                            </div>
                        </td>
                    </tr>
                    <tr style='mso-yfti-irow:3;mso-row-margin-right:.08%'>
                        <td width="24%" valign="top" style='width:24.44%;padding:0in 5.4pt 0in 5.4pt'>
                            <p class="NoTitle"></p>
                        </td>
                        <td width="75%" class="RightSide">
                            <!--ENTER SKILLS DESCRIPTION HERE...-->
                            <ul>'''
        for val in self.jobseeker.portfolios:
            ret = ret + '''
                                <li><a href="''' + val[Portfolio.SITE_ADDR] + '''">''' + val[Portfolio.SITE_ADDR] + '''</a></li>'''
        ret = ret + '''
                            </ul>
                        </td>
                    </tr>
                    <!--End of Portfolio-->
        '''
        return ret
    def BodySkills(self) -> str:
        ret:str = '''
                    <!--Skills-->
                    <tr style='mso-yfti-irow:2;page-break-inside:avoid'>
                        <td width="100%" colspan="2" valign="top" style='width:100.0%;padding:0in 5.4pt 0in 5.4pt'>
                            <div class="SectionTitleDiv">
                                <p class="SectionTitle">Skills</p>
                            </div>
                        </td>
                    </tr>
                    <tr style='mso-yfti-irow:3;mso-row-margin-right:.08%'>
                        <td width="24%" valign="top" style='width:24.44%;padding:0in 5.4pt 0in 5.4pt'>
                            <p class="NoTitle"></p>
                        </td>
                        <td width="75%" class="RightSide">
                            <!--ENTER SKILLS DESCRIPTION HERE...-->
                            <ul>'''
        for val in self.jobseeker.objective.skills:
            ret = ret + '''
                                <li>''' + val[Skill.SKILL_DESC] + '''</li>'''
        ret = ret + '''
                            </ul>
                        </td>
                    </tr>
                    <!--End of Skills-->
        '''
        return ret
    def BodyJobHistory(self) -> str:
        ret:str = '''
                    <!--Experience-->
                    <tr style='mso-yfti-irow:2;page-break-inside:avoid'>
                        <td width="100%" colspan="2" valign="top" style='width:100.0%;padding:0in 5.4pt 0in 5.4pt'>
                            <div class="SectionTitleDiv">
                                <p class="SectionTitle">Experience</p>
                            </div>
                        </td>
                    </tr>
                    <tr style='mso-yfti-irow:3;mso-row-margin-right:.08%'>
                        <td width="24%" valign="top" style='width:24.44%;padding:0in 5.4pt 0in 5.4pt'>
                            <p class="NoTitle"></p>
                        </td>
                        <td width="75%" class="RightSide">'''
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
                                    <ul>
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
                    <tr style='mso-yfti-irow:6;page-break-inside:avoid'>
                        <td width="100%" colspan="2" valign="top" style='width:100.0%;padding:0in 5.4pt 0in 5.4pt'>
                            <div class="SectionTitleDiv">
                                <p class="SectionTitle">Education</p>
                            </div>
                        </td>
                    </tr>
                    <tr style='mso-yfti-irow:7;mso-row-margin-right:.08%'>
                        <td width="24%" valign="top" style='width:24.44%;padding:0in 5.4pt 0in 5.4pt'>
                            <p class="NoTitle"></p>
                        </td>
                        <td width="100%" class="RightSide">'''
        for val in self.jobseeker.education:
            try:
                startDate:str = val[Education.START_DATE].strftime('%m/%d/%Y')
            except:
                startDate = val[Education.START_DATE]
            try:
                endDate:str = val[Education.END_DATE].strftime('%m/%d/%Y')
            except:
                endDate = Education.DEFAULT_ATTENDANCE_TXT
            ret = ret + '''
                                <table class="CompanyTable">
                                    <tr>
                                        <td class="CompanyDate">
                                            <!--Date Range-->
                                            ''' + startDate + '''&nbsp;-&nbsp;''' + endDate + '''
                                        </td>
                                        <td class="CompanyName">
                                            <!--School Name-->
                                            ''' + val[Education.SCHOOL_NAME] + '''
                                        </td>
                                        <td class="CompanyCityState">
                                            <!--City and State-->
                                            ''' + val[Education.CITY] + ''',&nbsp;''' + val[Education.STATE] + '''
                                        </td>
                                    </tr>
                                </table>
                                <!--Degrees and Honors-->
                                <ul>
                                    <li>
                                        ''' + val[Education.DEGREE] + '''
                                    </li>
                                </ul>	
                            '''							
        ret = ret + '''
                        </td>
                    </tr>
                    <!--End of Education-->
        '''
        return ret
    def BodyFooter(self) -> str:
        return '''<!--Heading information-->
                <tr>
                    <td colspan="2" valign="top">
                        <br />
                        <p 
                            class="Address1" 
                            style=
                                '
                                    mso-element:frame;
                                    mso-element-frame-hspace:9.35pt;
                                    mso-element-wrap:around;
                                    mso-element-anchor-vertical:page;
                                    mso-element-anchor-horizontal:margin;
                                    mso-element-top:bottom;
                                    mso-height-rule:exactly
                                '>
                                Email: <a href="mailto:''' +  self.jobseeker.EmailName + '''">''' + self.jobseeker.EmailName + '''</a>
                                <!--Website: http://resumedrafter.somee.com/Jobseeker/View/@jobseeker.JobseekerID-->
                        </p>
                        <p 
                            class="Address2" 
                            style=
                                '
                                    mso-element:frame;
                                    mso-element-frame-hspace:9.35pt;
                                    mso-element-wrap:around;
                                    mso-element-anchor-vertical:page;
                                    mso-element-anchor-horizontal:margin;
                                    mso-element-top:bottom;
                                    mso-height-rule:exactly
                                '>
                            ''' + self.jobseeker.Address + ''' • ''' + self.jobseeker.City + ''',&nbsp;''' + self.jobseeker.StateOrProvince + '''&nbsp;''' + self.jobseeker.PostalCode + '''&nbsp; •  
                            Phone: ''' + self.jobseeker.HomePhone + '''				
                        </p>
                    </td>
                </tr>	
                <!--End of formating the heading information-->'''