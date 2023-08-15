# imports
from matrix import Matrix
import random

# guesserPro
game_data = [
    # {
    #     "player": "user/ai",
    #     "attempts": 0,
    #     "number": comp_gen,
    # }
]

# main game function


def guesserPro():
    global game_data
    ai_guesses = []
    # guess limits
    l_limit, u_limit = 1, 100

    # Game mode
    try:
        mode = int(input(
            """
1. For You vs AI
2. For AI vs AI
>>> """
        ))
    except:
        errorFormatter("Invalid game mode !")
        guesserPro()

    # Game Logic
    game_attempts = 1

    comp_gen = random.randint(l_limit, u_limit)
    if mode == 1:
        while True:
            try:
                user_gen = int(input("Your Guess : "))
            except:
                errorFormatter("Invalid guess !")
                guesserPro()

            if user_gen > comp_gen:
                displayFormatter(user_gen, "is greater than the number")
            elif user_gen < comp_gen:
                displayFormatter(user_gen, "is lesser to the number")
            else:
                game_data.append({
                    "player": "You",
                    "attempts": game_attempts,
                    "number": comp_gen
                })
                break

            game_attempts += 1

    elif mode == 2:
        prev_greater = -1
        prev_lesser = -1
        while True:

            if prev_greater is None:
                l_limit = prev_lesser
            elif prev_lesser is None:
                u_limit = prev_greater
            else:
                pass

            user_gen = random.randint(l_limit, u_limit)

            if user_gen in ai_guesses:
                continue
            else:
                if user_gen > comp_gen:
                    ai_guesses.append(user_gen)

                    prev_greater = user_gen
                    prev_lesser = None

                    displayFormatter(user_gen, "is greater than the number")
                elif user_gen < comp_gen:
                    ai_guesses.append(user_gen)

                    prev_lesser = user_gen
                    prev_greater = None

                    displayFormatter(user_gen, "is lesser to the number")
                else:
                    game_data.append({
                        "player": "AI",
                        "attempts": game_attempts,
                        "number": comp_gen
                    })
                    break
                game_attempts += 1

    else:
        errorFormatter("Invalid game mode !")
        guesserPro()

    # Game Progression
    def gameProgression():
        game_progression_status = input("Do you want to continue? (y/n): ")
        if game_progression_status == "y":
            guesserPro()
        elif game_progression_status == "n":
            gameAnalytics()
            return
        else:
            errorFormatter("Type either 'y' or 'n' to continue !")
            gameProgression()

    gameProgression()

# Game Analytics


def gameAnalytics():
    print("\nGame Analytics\n")
    m1 = Matrix("Player", "Attempts", "Number")
    m1.unlock()
    for i in game_data:
        m1.add_row(
            i["player"],
            i["attempts"],
            i["number"],
        )
    m1.serialize()

    m1.lock()

    m1.printf()

    export_status = input("Do you want to export the analytics? (y/n): ")
    if export_status == "y":
        export_type = int(input(
            """
1. Export As CSV
2. Export AS HTML
>>> """
        ))

        if export_type == 1:
            m1.export_csv("./analytics.csv")
        elif export_type == 2:
            m1.export_html("./analytics.html")
        else:
            pass

    elif export_status == "n":
        pass
    else:
        pass

    print("DONE .")

# display formatter


def displayFormatter(guess, message):
    m1 = Matrix("Guess", "Message")
    m1.unlock()
    m1.add_row(guess, message)
    m1.lock()

    m1.printf()

# error formatter


def errorFormatter(message):
    m1 = Matrix("Status", "Message")
    m1.unlock()
    m1.add_row("Error", message)
    m1.lock()

    m1.printf()


# Calling the game function
guesserPro()
