# Dictionaries

# Jan -> January
# Mar -> March

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "Augustus",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",


}

print(monthConversions["Mar"])
print(monthConversions.get("Dec"))
print(monthConversions.get("Luv"))
print(monthConversions.get("Luv", "Not a valid key"))


# monthConversions = {
#   0: "January",
#   1: "February",
#   10: "March",
#   "Apr": "April",
#   "May": "May",
#   "Jun": "June",
#   "Jul": "July",
#   "Aug": "Augustus",
#   "Sep": "September",
#   "Oct": "October",
#   "Nov": "November",
#   "Dec": "December",
#
#
# }


# monthConversions = {
#     "Jan": "January",
#     "Jan": "February", # Do not make duplicate keys
#     "Mar": "March",
#
# }
