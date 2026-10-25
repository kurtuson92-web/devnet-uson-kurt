import requests
import random

border = "="*50

pokemon1 = requests.get("https://pokeapi.co/api/v2/pokemon/mew")
if pokemon1.status_code == 200:
    pokemon1 = pokemon1.json()
elif pokemon1.status_code == 404:
    print("Pokemon not found:", pokemon1.status_code)
elif pokemon1.status_code >= 400 and pokemon1.status_code < 500:
    print("Pokemon not found (Client Error):", pokemon1.status_code)
elif pokemon1.status_code >= 500 and pokemon1.status_code < 600:
    print("Server Error:", pokemon1.status_code)
else:
    print("Request failed:", pokemon1.status_code)


pokemon2 = requests.get("https://pokeapi.co/api/v2/pokemon/victini")
if pokemon2.status_code == 200:
    pokemon2 = pokemon2.json()
elif pokemon2.status_code == 404:
    print("Pokemon not found:", pokemon2.status_code)
elif pokemon2.status_code >= 400 and pokemon2.status_code < 500:
    print("Pokemon not found (Client Error):", pokemon2.status_code)
elif pokemon2.status_code >= 500 and pokemon2.status_code < 600:
    print("Server Error:", pokemon2.status_code)
else:
    print("Request failed:", pokemon2.status_code)


pokemon3 = requests.get("https://pokeapi.co/api/v2/pokemon/reshiram")
if pokemon3.status_code == 200:
    pokemon3 = pokemon3.json()
elif pokemon3.status_code == 404:
    print("Pokemon not found:", pokemon3.status_code)
elif pokemon3.status_code >= 400 and pokemon3.status_code < 500:
    print("Pokemon not found (Client Error):", pokemon3.status_code)
elif pokemon3.status_code >= 500 and pokemon3.status_code < 600:
    print("Server Error:", pokemon3.status_code)
else:
    print("Request failed:", pokemon3.status_code)


pokemon4 = requests.get("https://pokeapi.co/api/v2/pokemon/ninetales")
if pokemon4.status_code == 200:
    pokemon4 = pokemon4.json()
elif pokemon4.status_code == 404:
    print("Pokemon not found:", pokemon4.status_code)
elif pokemon4.status_code >= 400 and pokemon4.status_code < 500:
    print("Pokemon not found (Client Error):", pokemon4.status_code)
elif pokemon4.status_code >= 500 and pokemon4.status_code < 600:
    print("Server Error:", pokemon4.status_code)
else:
    print("Request failed:", pokemon4.status_code)


pokemon5 = requests.get("https://pokeapi.co/api/v2/pokemon/jirachi")
if pokemon5.status_code == 200:
    pokemon5 = pokemon5.json()
elif pokemon5.status_code == 404:
    print("Pokemon not found:", pokemon5.status_code)
elif pokemon5.status_code >= 400 and pokemon5.status_code < 500:
    print("Pokemon not found (Client Error):", pokemon5.status_code)
elif pokemon5.status_code >= 500 and pokemon5.status_code < 600:
    print("Server Error:", pokemon5.status_code)
else:
    print("Request failed:", pokemon5.status_code)


pokemons = [
    pokemon1,
    pokemon2,
    pokemon3,
    pokemon4,
    pokemon5
]

    

def whoisdat():
    while True:
        ran = random.choice(pokemons)
        name = ran["name"]

        print(border)
        print("WHO'S THAT POKEMON")
        print(border)
        print("Height:", ran["height"])
        print("Weight:", ran["weight"])
        print(border)

        guess = input("Guess That POKEMON: ")

        if guess.lower() == name:
            print("Wonderful! You got that! you're a Pro")
        else:
            print("That's not right.")
            print(border)
            print("Hint 1")
            print("Type:", ran["types"][0]["type"]["name"])
            print(border)

            guess2 = input("Guess That POKEMON: ")

            if guess2.lower() == name:
                print("Nice! You got it!")
            else:
                print("Here's another hint.")
                print(border)
                print("Hint 2")
                print("Ability 1:", ran["abilities"][0]["ability"]["name"])
                print(border)

                guess3 = input("Guess That POKEMON: ")

                if guess3.lower() == name:
                    print("Interesting! You got it!")
                else:
                    print("Here's the last hint.")
                    print(border)
                    print("Hint 3")
                    print("Move:", ran["moves"][0]["move"]["name"])
                    print("Move:", ran["moves"][1]["move"]["name"])
                    print(border)

                    guess4 = input("Guess That POKEMON: ")

                    if guess4.lower() == name:
                        print("At last! You got it!")
                    else:
                        print("That's the last chance. Better luck next time!")
                        print("The Pokemon was:", name)

        answer = input("Do you want to play again? (y/n): ")

        if answer.lower() == "n" or answer.lower() == "no":
            print("Thanks for playing WHO'S THAT POKEMON!")
            break
        elif answer.lower() == "y" or answer.lower() == "yes":
            print("Starting a new game!")
        else:
            print("Invalid choice. Exiting game.")
            break

whoisdat()