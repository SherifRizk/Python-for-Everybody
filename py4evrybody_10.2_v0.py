10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = "mbox-short.txt" #input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
count=dict()
handle = open(name)
for line in handle:
    if not line.startswith('From '):continue
    words = line.split()
    for word in words:
        if ':'in word:
            count[word[:2]]=count.get(word[:2],0)+1
           # print(word[:2])
        
lst = list()
for key,value in count.items():
    lst.append((key,value))

lst=sorted(lst)
for k,v in lst:
    print (key,value)
    
    

#x= sorted([(k,v) for k,v in count.items()]) #list comrehension
#for i in x:
#    print(i[0],i[1])