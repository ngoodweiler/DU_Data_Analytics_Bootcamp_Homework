# @TODO: Your code here
hobbybook={
        "name": "Nolan Goodweiler",
        "age": 29,
        "hobbies": ["snowboarding",
            "reading",
            "coding"],
        "wakeup": {
            "early":"3:30",
            "snoozed":"4:00",
            "weekend":"6:00"
        }
}

print(f'Hello, my name is {hobbybook["name"]} and I am {hobbybook["age"]} years old')
print(f'I have {len(hobbybook["hobbies"])} hobbies.')
print(f'On Saturdays I wake up at {hobbybook["wakeup"]["weekend"]}')
