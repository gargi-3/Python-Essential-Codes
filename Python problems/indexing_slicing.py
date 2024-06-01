# indexing demo
topic = "Python"
print(topic[0])
print(topic[1])
print(topic[2])
print(topic[3])
print(topic[4])
print(topic[5])
print(topic[-1])
print(topic[-2])
print(topic[-3])
print(topic[-4])
print(topic[-5])
print(topic[-6])
# print(topic[7]) -> Index Error (out of range)

# slicing demo

city = "panvel"
partialCityData = city[3:6]
print(partialCityData)

message = "welcome to python session"
subMesssage = message[4:20:2]
print(subMesssage)

message1 = "hello all, welcome"
subMesssage = message1[:10:]
print(subMesssage)

message2 = "hi this is gargi"
subMesssage = message2[::]
print(subMesssage)