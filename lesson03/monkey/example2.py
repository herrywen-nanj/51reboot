

RESULT = [
	["monkey1", 12, "13987654321", "monkey@51reboot.com"],
    ["monkey2", 12, "13987654321", "monkey@51reboot.com"],
    ["monkey3", 12, "13987654321", "monkey@51reboot.com"],
]

# add monkey1 12 13987654321 monkey@51reboot.com

username = "monkey31"


NAMES = []

for i in RESULT:
    name = i[0]
    NAMES.append(name)


if username in NAMES:
    print("User {} already exists.".format(username))
else:
    RESULT.append("[userlist]")