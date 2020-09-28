# <em>The Brown and White</em> Lehigh University 2020 Election Poll

To assess Lehigh University's sentiments on candidates and issues relating to the 2020 Presidential Election, a survey was made available to community members via the social media accounts of <em>The Brown and White</em>, The Lehigh University newspaper. The survey was also distributed to faculty and administration members by direct email.

<em>The Brown and White</em> first analyzed responses by looking at the community as a whole, and then again by looking at how responses differed by college, and at how responses differed by Lehigh affiliation. For purposes of the poll, “Lehigh affiliation” refers to whether the respondent was an undergraduate student, a graduate student, a faculty member, a staff member, or an administrator.

For the breakdown of issue stance by college, the College of Health was excluded due to low response rates from that group. For the breakdown of issues stance by Lehigh affiliation, the Administrator group was excluded for the same reason.

The poll questions were phrased based on popular wordings in existing political polls, and based on the advice of experts from Lehigh University’s Department of Journalism and Communication and the Lehigh University Pride Center. 

The bwelectionpoll.py Python file, in this repository, was used to transform the poll data. The data was read into a Pandas Dataframe directly from Google Sheets, and transformed into multiple different views. Some views include separate sheets for the different questions that were asked of respondents based on their affiliation with Lehigh. For example, only undergraduate students were asked if they were affiliated with a Greek organization on campus. Separate spreadsheets were also made for the questions that pertained to the candidates, and for the questions that pertained to specific issues. All views were written to different sheets in the same Excel file, as seen in the commented-out code at the end of the file.

The client_secret.json file needed to authorize access to the Google spreadsheet was purposefully excluded from the repository to prevent access to the poll data.    
