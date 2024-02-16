import pandas as pd
import string
from pyresparser import ResumeParser
from tika import parser
import re
import spacy 
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
import string

nlp=spacy.load("en_core_web_sm")
# Extracting Skills
def extract_skill(resume_data):
    df=pd.read_csv("C:\\Users\\chaitu\\Desktop\\JobExplorer\\skills.csv")
    filter_data=resume_data.strip()
    filter_data=re.sub(r'\n',r' ',filter_data)
    nlp_text=nlp(resume_data)
    noun_phrases=nlp_text.noun_chunks
    tokens=[i.text for i in nlp_text if not i.is_stop]
    skill_set=[]
    tokens=[i for i in tokens if len(i)!=0]
    for i in tokens:
        i=str(i)
        if i[0].upper() in df.columns.values and i[0] not in string.punctuation and i.lower() in df[i[0].upper()].values:
            skill_set.append(i.lower())
    for i in noun_phrases:
        i=str(i)
        if i[0].upper() in df.columns.values and i[0] not in string.punctuation and i.lower() in df[i[0].upper()].values:
            skill_set.append(i.lower())
    skills=[i.capitalize() for i in set(skill_set)]
    return skills


# Extract Education

stop_words=set(stopwords.words("english"))
EDUCATION = [
            'BE','B.E.', 'B.E', 'BS', 'B.S', 
            'ME', 'M.E', 'M.E.', 'MS', 'M.S', 
            'BTECH', 'B.TECH', 'M.TECH', 'MTECH']
def extract_education(resume_data):
    nlp=spacy.load("en_core_web_sm")
    nlp_text=nlp(resume_data)
    nlp_text=[sent.string.strip() for sent in nlp_text.sents]
    edu={}
    for ind,text in enumerate(nlp_text):
        for tex in text.split():
            tex=re.sub(r'[.|?|$|.|!|,]',r'',tex)
            if tex in EDUCATION and tex not in stop_words:
                edu[tex]=text+nlp_text[ind+1]

    education=[]
    for i in edu.keys():
        education.append(i)
        # year=re.search(re.compile(r'(((20|19)(\d{2})))'),edu[i])
        # if year:
        #     education.append((i,''.join(year[0])))
        # else:
        #     education.append(i)
    if education:
        return education[0]
    else:
        return None
    
# Experience
text=["Work History",
"Experience",
"Employment History",
"Work Experience",
"Employment",
"Employment Experience",
"Military Experience",
"Professional Experience",
"Professional Background",
"Employment Background",
"Internships",
"Paid Internships",
"Work Internships",
"Professional Internships",
"Professional Background",
"Relevant Experience",
"Work Accomplishments",
"Career Highlights",
"Key Achievements",
"Career Achievements",
"Work Achievements",
"Career Progression"]
nlp=spacy.load("en_core_web_sm")
def extract_experience(resume_data):
    nlp_text=nlp(resume_data)
    noun_phrases=[str(i).lower() for i in nlp_text.noun_chunks]
    tokens = [str(token) for token in nlp_text if not token.is_stop]
    tokens=[i.lower() for i in tokens]
    for i in text:
        if i.lower() in tokens:
            return True
        else:
            for j in noun_phrases:
                if i.lower() in j:
                    return True
    return False
    



def Resume_Parser(resume_data):
    details={}
    parsed=parser.from_file(resume_data)
    data=parsed['content']
    data=re.sub("Bachelor of Technology",'B.TECH',data)
    data=re.sub("Bachelor of Engineering",'B.E.',data)
    data=re.sub("Bachelor of Science in Engineering",'B.S',data)
    data=re.sub("Master of Technology",'M.TECH',data)
    data=re.sub("Master of Science",'M.S',data)
    data=re.sub("Master of Engineering",'M.E.',data)
    content=ResumeParser(resume_data).get_extracted_data()
    details["Name"]=content['name']
    details["Email"]=content['email']
    details["Mobile_Number"]=content['mobile_number']
    details["Education"]=extract_education(data)
    details["Skills"]=extract_skill(data)
    details["Experience"]=extract_experience(data)
    return details

#Skill Match
def check(row,skills):
    row=row.split('/')
    count=0
    for i in skills:
        if i.lower() in row:
            count=count+1
    return count
# percentage
def percentage(row1,row2):
    row1=row1.split('/')
    match=row2/len(row1)
    return round(match,2)

