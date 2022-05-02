import json


json_text = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},' \
            '{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'
key = "messages"
key2 = "message"
#парсим все что внутри messages
obj = json.loads(json_text)
#выводим конкретный тег message
obj2 = obj[key][1]
print(obj2[key2])