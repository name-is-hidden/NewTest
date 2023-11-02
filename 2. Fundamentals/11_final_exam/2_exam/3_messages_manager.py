messages_cap = int(input())

command = input()

data_dict = dict()

while command != "Statistics":
    command_parameter = command.split("=")

    action = command_parameter[0]

    users_dict = dict()
    users_dict["sent"] = 0
    users_dict["received"] = 0

    if action == "Add":
        username = command_parameter[1]
        sent_messages_count = int(command_parameter[2])
        received_messages_count = int(command_parameter[3])

        if username not in data_dict:
            data_dict[username] = users_dict
            users_dict["sent"], users_dict["received"] = sent_messages_count, received_messages_count

        else:
            pass

    elif action == "Message":
        sender = command_parameter[1]
        receiver = command_parameter[2]

        data_dict[sender]["sent"] += 1
        data_dict[receiver]["received"] += 1

        if sum(data_dict[sender].values()) >= messages_cap:
            print(f"{sender} reached the capacity!")
            data_dict.pop(sender)

        elif sum(data_dict[receiver].values()) >= messages_cap:
            print(f"{receiver} reached the capacity!")
            data_dict.pop(receiver)

    elif action == "Empty":
        profile = command_parameter[1]

        if profile in data_dict:
            data_dict.pop(profile)

        else:
            data_dict.clear()

    command = input()

print(f"Users count: {len(data_dict)}")

for key, value in data_dict.items():
    print(f"{key} - {sum(data_dict[key].values())}")

##################################################################

# messages_cap = int(input())
#
# command = input()
#
# data_dict = dict()
#
# while command != "Statistics":
#     command_parameter = command.split("=")
#
#     action = command_parameter[0]
#
#     if action == "Add":
#         username = command_parameter[1]
#         sent_messages_count = int(command_parameter[2])
#         received_messages_count = int(command_parameter[3])
#
#         if username not in data_dict:
#             data_dict[username] = sent_messages_count + received_messages_count
#
#         else:
#             pass
#
#     elif action == "Message":
#         sender = command_parameter[1]
#         receiver = command_parameter[2]
#
#         data_dict[sender] += 1
#         data_dict[receiver] += 1
#
#         if data_dict[sender] >= messages_cap:
#             print(f"{sender} reached the capacity!")
#             data_dict.pop(sender)
#
#         elif data_dict[receiver] >= messages_cap:
#             print(f"{receiver} reached the capacity!")
#             data_dict.pop(receiver)
#
#     elif action == "Empty":
#         profile = command_parameter[1]
#
#         if profile in data_dict:
#             data_dict.pop(profile)
#
#         else:
#             data_dict.clear()
#
#     command = input()
#
# print(f"Users count: {len(data_dict)}")
#
# for key, value in data_dict.items():
#     print(f"{key} - {value}")
