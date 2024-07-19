age = 20
print(f"You are {age}")

name = "Bruno"
greeting = f"How are you, {name}?" # the string is calculate with the value of 'name' at this moment
print(greeting)

name = "Bob"
print(greeting)

name = "Bruno"
final_greeting = "How are you, {}?"
bruno_greeting = final_greeting.format(name)

print(bruno_greeting)

name = "Bob"
bob_greeting = final_greeting.format(name)
print(bob_greeting)

named_parameter = "How are you, {name}?"
jose_greeting = named_parameter.format(name="Jose")
print(jose_greeting)
