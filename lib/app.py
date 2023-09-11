dog = input("what is the dog's condition? : ")
dict_map = {
    "hungry": "feed the dog",
    "thirsty": "refill the water bottle",
    "playful": "play with the dog",
}
owner = dict_map.get(dog, "dog is boring") #.get method lets us set a default value
print(owner)