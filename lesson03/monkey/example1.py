

RESULT = [
	["monkey1", 12, "13987654321", "monkey@51reboot.com"],
    ["monkey2", 12, "13987654321", "monkey@51reboot.com"],
    ["monkey3", 12, "13987654321", "monkey@51reboot.com"],
]

# find monkey3
# add monkey1 12 13987654321 monkey@51reboot.com

username = "monkey31"
find_flag = False

for i in RESULT:
    name = i[0]
    if name == username:
        print("{} {} {} {}".format(i[0], i[1], i[2], i[3]), end="\t")
        find_flag= True


if not find_flag:
    print("User {} not found.".format(username))