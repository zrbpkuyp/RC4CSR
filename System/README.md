# The main structure of this project
functionalities are divided into System, Recommendation, Discussion and Writing
## System
<<<<<<< HEAD
basic models & main pages  
### basic models
PlatformUser  
Book  
Group  
Topic    
### main pages
welcome（TODO)
register
login
user page  
=======
>>>>>>> refs/remotes/upstream/master
## Recommendation
offer recommendations to users based on their behaviors and other info  
recieving results from model ML
### model: PlatformUser
### model: Book  
### model: Topic
## Discussion
discussion zone & groups  
### discussion zone
showing groups of different topics or books  
### model: discGroup
members of the group can post comments about its topic or book  
### model: discRecord
key design for discussion zone  
allowing group members to post comments, reply to other comments and give likes  
### web page: Discussion.index  
displaying groups  
### web page: Discussion.detail  
showing discussions after entering a group  
## Writing
post pencrafts and comment pencrafts  
### model: Pencraft
main body of a pencraft created by a platformUser  
containing title(topic), description and chapters  
### model: Chapter
containing subtitle and content of a chapter  
### web page: Writing.index
displaying pencrafts  
### web page: Writing.pencraft
showing title, author, chapters and other information about a pencraft  
### web page: Writing.chapter
showing content of a chapter  