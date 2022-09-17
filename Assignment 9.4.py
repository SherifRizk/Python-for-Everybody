name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
count = dict()
for line in handle:
    if not line.startswith('From '):continue
    words = line.split()
    #print(words[1])
    for word in words:
        if '@' in word:
            count[word]=count.get(word,0) + 1

#print(count)
max_key=None
max_value=None

for key , value in count.items():
    if max_value is None or value >max_value:
        max_key = key
        max_value = value
print(max_key,max_value)