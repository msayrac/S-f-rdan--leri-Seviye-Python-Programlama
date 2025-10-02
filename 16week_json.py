# json ortak veri tasıma olarak adlandırabiliriz
import json

# person_string = '{"name":"Ali","languages":["python","C#"]}'
# # print(type(person_string))

# # JSON string to Dict

# result = json.loads(person_string)
# # result = result["name"]
# result = result["languages"]

# with open("person.json") as f:

#     data = json.load(f)
#     print(data["name"])
#     print(data["languages"])

# person_dict = {
#     "name":"Ali2",
#     "languages":["Python2","C#2"]
# }

# result = json.dumps(person_dict)

# with open("person.json","w") as file:

#     json.dump(person_dict,file)


person_string = '{"name":"Ali","languages":["python","C#"]}'
person_dict = {
    "name":"Ali2",
    "languages":["Python2","C#2"]
}

person_dict = json.loads(person_string)
result = json.dumps(person_dict,indent=4,sort_keys=True)

print(person_dict)
print(result)
print(type(result))


