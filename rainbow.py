import csv 
import hashlib

dict_hash_code = dict()
for i in range (0 , 10000):
    dict_hash_code[hashlib.sha256(b'%i'%i).hexdigest()] = str(i)
    
with open('data.csv') as f :
    reader = dict(csv.reader(f))

result = dict()
for key , value in reader.items():
    result[key] = dict_hash_code[value]

print(result)