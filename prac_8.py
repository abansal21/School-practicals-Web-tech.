#list
a = []
for i in range(5):
    b = input("enter element {} of the list".format(i + 1))
    a.append(b)
print(a)
z = list(range(5))
print(z)

#dictonaries
d = {'arun': 'bansal', 'reading':'books'}
print(d.items())
print(d.values())
print(d.keys())
print("d['arun'] = {}".format(d['arun']))

for v,k in d.items():
    print(v, k)
    
#textfiles
f = open('ab.txt', 'w')
f.write("Hello python world!")
f.close()
f = open('ab.txt','r')
string = f.read()
print(string)

f.close()
