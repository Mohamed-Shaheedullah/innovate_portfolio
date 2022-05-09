#
# key value pairs
dict_of_films = {
    "Dune": 2020, "Sicario": 2018, "Blade runner sequel" : 2017
}

# do not use a numbered index, use key 

dict_of_films["Dune"] = 2019

print(dict_of_films)

dict_of_dog = {
"name" : "Prince", "colour": "Black", "age" : 7, "ears": "floppy", "teeth": "small" }

print(dict_of_dog)

dict_of_dog["name"] = "Judy"
print(dict_of_dog["name"])

dict_of_dog["colour"] = "Brown"
print(dict_of_dog["colour"])

dict_of_dog["age"] = 4
print(dict_of_dog["age"])

dict_of_dog["ears"] = "Stiff"
print(dict_of_dog["ears"])


countries_dict = {
    "United Kingdom" : "London",
    "France" : "Paris",
    "Germany" : "Berlin",
    "Spain" : "Madrid",
    "Italy" : "Rome"
}

countries_dict.setdefault("Bangladesh", "Dhaka")
countries_dict.setdefault("USA", "Washington D. C.")

print(countries_dict) # this is a simplke method

