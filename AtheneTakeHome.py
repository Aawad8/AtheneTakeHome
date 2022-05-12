import json

string = input("Enter name of the JSON file: ")
min = int(input("Enter min range: "))
max = int(input("Enter max range: "))



with open(string, "r") as f:
    file = json.loads(f.read())

values = {}

for i in file:
    num = i.get("team_size")
    
    if num in range(min,max+1,1):
        words = i.get("tech_stack")

        for w in words:
         if w in values :
            values[w] = values[w] +1;
         else :
            values[w] = 1
    

print(values)
    
    