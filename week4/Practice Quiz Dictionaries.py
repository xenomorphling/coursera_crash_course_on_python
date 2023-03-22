"""
The email_list function receives a dictionary, which contains domain names as keys, and a list of users as values. Fill in the blanks to generate a list that contains complete email addresses (e.g. diana.prince@gmail.com).
"""

# def email_list(domains):
#     emails = []
#     for key in domains.keys():
#         for person in domains[key]:
#             emails.append("{}@{}".format(person, key))
#     return(emails)
# print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))

# def email_list(domains):
# 	emails = []
# 	for domain, users in domains.items():
# 	  for user in users:
# 	    emails.append("{}@{}".format(user, domain))
# 	return(emails)

# print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))


"""
The groups_per_user function receives a dictionary, which contains group names with the list of users. Users can belong to multiple groups. Fill in the blanks to return a dictionary with the users as keys and a list of their groups as values. 
"""

# def groups_per_user(group_dictionary):
#     user_groups = {}
#     # Go through group_dictionary
#     for group in group_dictionary.keys():
#         # print(users)
#         for user in group_dictionary[group]:
#             # print(user, group)
#             if user in user_groups.keys():
#                 print(user, group)
#                 user_groups.append(user, group)
#         # for group in group_dictionary.keys():
#         #     print(group)
#     return(user_groups)

# print(groups_per_user({ "local": ["admin", "userA"],
#                         "public":  ["admin", "userB"],
#                         "administrator": ["admin"] }))

def groups_per_user(group_dictionary):
    user_groups = {}
    # Go through group_dictionary
    for group, users in group_dictionary.items():
        # Now go through the users in the group
        for user in users:
            # Now add the group to the the list of groups for this user, creating the entry in the dictionary if necessary
            if user not in user_groups:
                user_groups[user] = []
            user_groups[user].append(group)
    return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],"public":  ["admin", "userB"],"administrator": ["admin"] }))



# def groups_per_user(group_dictionary):
# 	user_groups = {}
# 	# Go through group_dictionary
# 	for group, users in group_dictionary.items():
# 		# Now go through the users in the group
# 		for user in users:
# 			# Now add the group to the the list of
# 			# groups for this user, creating the entry
# 			# in the dictionary if necessary
# 			if user not in user_groups:
# 				user_groups[user] = []
# 			user_groups[user].append(group)

# 	return(user_groups)






# wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
# for cloth in wardrobe.keys():
#     for color in wardrobe[cloth]:
#         print("{} {}".format(color, cloth))
# dictionary = {'george': 16, 'amber': 19}
# search_age = input("Provide age")
# for name, age in dictionary.items():  # for name, age in dictionary.iteritems():  (for Python 2.x)
#     if age == search_age:
#         print(name)