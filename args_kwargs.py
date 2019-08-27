
# args - takes any number of positional argument values and adds them to a list
def list_fave_colors(name, *args):
  for color in args:
    print(f"My name is {name}, and one of my fave colors is {color}")

# Pass in any number of arguments after the name ("Fred" or "Tia", and the function works, thanks to *args)
list_fave_colors("Fred", "red", "green", "blue", "orange")
list_fave_colors("Tia", "puce", "goldenrod")


#kwargs -- takes any number of keyword arguments and adds them to a dictinary
def make_family(name, **tacos):
  family_str = f"We are the {name} family. "
  for title, person in tacos.items():
    family_str += f"The {title} is {person}. "

  return family_str

# Now we can make families of any size, and have flexibility to have those family members have whatever role we want
family = make_family("Shepherd", mom="Anne", dad="Joe", dog="Murph")
other_family = make_family("Parker", aunt="May", nephew="Peter")

print(family)
print(other_family)
