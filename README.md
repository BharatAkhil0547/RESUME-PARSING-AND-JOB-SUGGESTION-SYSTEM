# RESUME PARSING AND JOB SUGGESTION SYSTEM
While applying for a job, it is always a good practice to apply for a job based on the skills required for that 
position. Without the essential skills, it is difficult to perform well in that job. It is very difficult to find a 
appropriate job for them as there will be many job openings in a online job portal and it is every difficult to 
identify the one that matches their skills. 
But it is very difficult this task. So our website acts an intermediate between employer and employee to provide 
job suggestions to the job seeker based on the skills present in the candidates resume. 

# INTRODUCTION
Our project overcomes the above difficulty by,
* Extracting the skills mentioned in the candidates resume through resume parsing.
* After that, our system provides job suggestions to the job seeker by matching job seekers skills 
with the skills required for a job.
 
Therefore, any candidate can easily apply for appropriate jobs for them. 

# INPUTS AND OUTPUTS

### Inputs:
* Main source of data for our project is resumes of the job seekers in Portable Document Format (PDF) format.
* Another source of data for our project is the online job portals. Job opening posts in these online job portals are 
main inputs for our system.
### Outputs:
The final outcome of “Resume Parsing and Job Suggestion System” is suggesting some job openings to a candidate 
by matching the skills mentioned in his/her resume with the skills required for a particular job role.

# TOOLS AND TECHNOLOGIES
### MODULES REQUIRED:
* Flask
* Pyresparser
* Apache Tika
* Spacy
* NTLK
* Regular Expressions
* Selenium
* Beautiful Soup
* os module
* Pandas module

# DESIGN AND IMPLEMENTATION

![image](https://github.com/BharatAkhil0547/RESUME-PARSING-AND-JOB-SUGGESTION-SYSTEM/assets/106509821/53137402-e8c6-4265-9e39-175c8738a899)

### WORKFLOW
* Job seeker uploads their resume in our website.
* The resume is parsed and required information such as name, email, skills, etc are
extracted from it.
* Information about available job openings in online job portals – Naukri and Monster is
stored in a CSV file using web scraping.
* Job suggestions are provided to the user by matching the skills present in the resume with
the skills required for the job opening

# RESULTS AND DISCUSSIONS

Examine the results  👉 👉 [here](https://github.com/BharatAkhil0547/RESUME-PARSING-AND-JOB-SUGGESTION-SYSTEM/tree/main/outputs).

# CONCLUSIONS

Our project “Resume Parsing and Job Suggestion System” makes the job hiring
process easier and more reliable by hiring candidates with the required skill set. Our
system provides a benefit for both the employer and employee. A candidate can save a
lot of time by eliminating the tedious work of job searching. It benefits the employer
also as only the candidate with right skill set can apply for a job role.







