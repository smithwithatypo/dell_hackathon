import Person

# init constants
SIZE = 4
MEDIAN = 5


# read pre.csv -->  Goal is to set magnitudes for person
with open("pre.csv", "r") as file:
    pre_data = file.readline()
pre_data = pre_data.split(",")

# init person with BadgeID
person = Person.Person(pre_data[0])

# set ratings of person object
for i in range(SIZE):
    person.setRatings(i, pre_data[i+1])   # setRatings(category, rating)

person.setRatingsTotal()
person.setMagnitudes(MEDIAN, SIZE)
person.setWeights(SIZE)


# read multi.csv   -->   Goal: set Preference list for person
with open("multi.csv", "r") as file:
    multi_data = file.read().splitlines()

for i, v in enumerate(multi_data):
    # array of arrays in format: [str, str, str, str, str]
    multi_data[i] = v.split(",")

for i in range(len(multi_data)):   # i is [manager, str, str, str, str]
    for j in range(1, len(multi_data)+1):  # j is the strings
        multi_data[i][j] = int(multi_data[i][j])

person.setScores(multi_data, SIZE)
person.setPreferences(multi_data, SIZE)


# write output.csv -->  Goal:  export top 5 machine-created preferences from person to our Stable Marriage Algorithm
with open("output.csv", "w") as file:
    pass

print("Final Preference List:", person.getPreferences())
