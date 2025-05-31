#Print to the screen phrases like the following example:

"The capital of Germany is Berlin"

#Use the zip function, loops, and the following lists of countries and capitals to solve it quickly and efficiently.

capitals = ["Berlin", "Tokyo", "Paris", "Helsinki", "Ottawa", "Canberra"]
countries = ["Germany", "Japan", "France", "Finland", "Canada", "Australia"]

combined_words =   list(zip(capitals,countries))

for capitals,countries in combined_words:
    print(f'The capital of {countries} is {capitals}')