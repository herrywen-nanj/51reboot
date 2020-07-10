

RESULT = [
	["monkey1", 12, "13987654321", "monkey@51reboot.com"],
    ["monkey2", 12, "13987654321", "monkey@51reboot.com"],
    ["monkey3", 12, "13987654321", "monkey@51reboot.com"],
]

# update monkey1 set age = 20

info = "update monkey1 set age = 20"
info_list = info.split()
action = info_list[0]

username = info_list[1]
where = info_list[2]

if action == "update":
    if where != "set":
        # break
        print("")


NAMES = []

for i in RESULT:
    name = i[0]
    NAMES.append(name)


if username in NAMES:
    idx = NAMES.index(username)
    if info_list[3] == "age":
        RESULT[idx][1] = info_list[-1]

    '''
    for i in RESULT:
        if i[0] == username:
            if info_list[3] == "age":
                i[1] = info_list[-1]
    '''
else:
    print("User {} not found.".format(username))