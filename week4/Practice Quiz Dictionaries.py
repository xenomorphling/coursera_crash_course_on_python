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


"""
The groups_per_user function receives a dictionary, which contains group names with the list of users. Users can belong to multiple groups. Fill in the blanks to return a dictionary with the users as keys and a list of their groups as values. 
"""

def groups_per_user(group_dictionary):
    user_groups = {}
    # Go through group_dictionary
    for user in group_dictionary.values():
        # Now go through the users in the group
        print(user)
        for group, user in group_dictionary.items():
            # Now add the group to the the list of
            # groups for this user, creating the entry
            # in the dictionary if necessary
            print(user, group)
    return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
        "public":  ["admin", "userB"],
        "administrator": ["admin"] }))



dictionary = {'george': 16, 'amber': 19}
search_age = input("Provide age")
for name, age in dictionary.items():  # for name, age in dictionary.iteritems():  (for Python 2.x)
    if age == search_age:
        print(name)