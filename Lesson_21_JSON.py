import json
filename = "/Users/aegar/Desktop/Programming/ADV_lessons/File processing/user_settings.txt"
myfile = open(filename, mode='w', encoding='Latin-1')

igrok1 = {
    'Name'  : "Ivan Polkin",
    'Score' : "150",
    'Awards': ["Moscow", "S-Pb", "Novosibirsk"]
}
igrok2 = {
    'Name': "Petr Pchelkin",
    'Score': "170",
    'Awards': ["Kiev", "Gomel\'", "Khabarovsk"]
}

myplayers = []
myplayers.append(igrok1)
myplayers.append(igrok2)


    # _____________ Save by JSON ______________

json.dump(myplayers, myfile)
myfile.close()

    # _____________ Load by JSON ______________

myfile = open(filename, mode='r', encoding='Latin-1')
json_load = json.load(myfile)

for user in json_load:
    print("Player name is: " + str(user['Name']))
 #   print(user)
    print("Score is: " + str(user['Score']))
 #   print(user)
    print("Player Award N1 " + str(user['Awards'][0]))
    print("Player Award N2 " + str(user['Awards'][1]))
    print("Player Award N3 " + str(user['Awards'][2]))



