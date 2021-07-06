q = {"How many days do we have in a week?":["a.7","b.8","c.6","a"],"How many days are there in a year":["a.366","b.365","c.364","b"],
 "How many colors are there in a rainbow?":["a.9","b.7","c.6","b"],
 "Which animal is known as the ‘Ship of the Desert?":["a.camel","b.Thorny Devil","c.Chile","a"],"How many letters are there in the English alphabet?":["a.27","b.25","c.26","c"],"How many consonants are there in the English alphabet?":["a.21","b.22","c.23","a"]," How many sides are there in a triangle?":["a.4","b.5","c.3","c"],"In which direction does the sun rise?":["a.north","b.east","c.south","b"],"Which month of the year has the least number of days?":["a.february","b.march","c.june","a"],"We smell with our?":["a.nose","b.ear","c.eyes","a"]
 }
q = list(q.items())
q = dict(q)
count = 0
for i in q.keys():
    print(i)
    for j in range(0,len(q[i])-1,1):
        print(q[i][j])
    ans = input("ur choice is : ")
    if ans == q[i][len(q[i])-1]:
        count +=1
print("Total Score:",count)
