import MySQLdb
import speech_recognition as sr
import nltk
from nltk import load_parser
from nltk.sem import chat80

def speech():
    r = sr.Recognizer()
    m = sr.Microphone()
    z=2
    try:
        with m as source: r.adjust_for_ambient_noise(source)
        while z!=1:
            print("Give your query in English ")
            with m as source: audio = r.listen(source)
            print("Recognizing the input\nPlease wait....")
            try:
                value = r.recognize_google(audio)
                if str is bytes: 
                    print(u"Query in English - {}".format(value).encode("utf-8"))
                else: 
                    print("You said {}".format(value))
            except sr.UnknownValueError:
                print("Oops! Didn't catch that")
            except sr.RequestError as e:
                print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
            lol=format(value)
            hi=lol
            hi=hi.encode("utf-8")
            #for i in lol: hi.append(i)
            z=1
    except KeyboardInterrupt:
        pass

    return hi


def sqlTOdb(query):
    db = MySQLdb.connect(host="localhost", user="user", passwd="password", db="student")
    cursor = db.cursor()
    cursor.execute(query)
    db.commit()
    numrows = int(cursor.rowcount)
    print "\nDatabase Output :",
    if numrows==0:
        print "\nNo database entry"
    for x in range(0,numrows):
        row = cursor.fetchone()
        print "\n"
        for i in row:
            print i, "~~~",



def sqlGen(query):
    select=[]
    from_words=[]
    where=[]
    names=['Ramesh','Suresh','Mahesh']
    dept=['ISE', 'computers', 'Civil','civil','mechanical']
    sem=['first','second','third','fourth','fifth','sixth','1st','2nd','3rd','4th','5th','6th']
    coll=['rvce','pesit','nitk','RVCE','PESIT','NITK']
    city=['bangalore','tumkur','mysore','Bangalore','Tumkur','Mysore']
    marks=['100','90','80','70','60','95','85','75','65']
      #tabs=['student']
      #atts=['name','names','department','departments','hometown','city','college',',colleges','marks','sem','semester','grade','percentage']
    q=query.split()
    for i in q:
      if i=='name' or i=='names': select.append('name')
      elif i=='department' or i=='departments':   select.append('dept')
      elif i=='city' or i=='hometown' or i=='cities': select.append('hometown')
      elif i=='colleges' or i=='college': select.append('coll_name')
      elif i=='marks' or i=='percentage' or i=='grade':   select.append('marks')
      elif i=='semester' or i=='sem': select.append('sem')
      elif i=='details':  select.append('*')
    if "*" in select:   s="*"
    else:   s=', '.join(select)

    for i in q:
      if i=='student' or i=='students':   from_words.append('student')
    f=', '.join(from_words)

    for i in q:
      if i in names:  where.append('name="'+i+'"')
      elif i in dept:   where.append('dept="'+i+'"')
      elif i in coll:   where.append('coll_name="'+i+'"')
      elif i in city:   where.append('hometown="'+i+'"')
      elif i in marks:    where.append('marks='+i)
      elif i in sem:
          if i=='first' or i=='1st':  where.append('sem=1')
          elif i=='second' or i=='2nd':   where.append('sem=2')
          elif i=='third' or i=='3rd':    where.append('sem=3')
          elif i=='fourth' or i=='4th':   where.append('sem=4')
          elif i=='fifth' or i=='5th':    where.append('sem=5')
          elif i=='sixth' or i=='6th':    where.append('sem=6')
    if len(where)==0:   where.append('1')
    w=' AND '.join(where)

    sql="SELECT "+s+" FROM "+f+" WHERE "+w
    return sql

print "\n\n******************* Natural Language Interface for Database ********************\n\n"
print "1. Speech Input\n2. Text Input"
choice=raw_input('Enter Your Choice : ')
print choice
if choice == '1':
    speech()
elif choice == '2':
    query = raw_input("Give your query in English : ")
sql=sqlGen(query)
print "Query in SQL - "+sql
sqlTOdb(sql)


