from matrix import Matrix
import random

game_data = [
    # {
    #     "player": ""
    #     "attempts": 0
    # }
]

l_limit, u_limit = 0, 100


def display_data():
    print("\n Game Analytics \n")
    m1 = Matrix("Player", "Attempts")
    m1.unlock()

    for data in game_data:
        m1.add_row(data["player"], data["attempts"])

    m1.serialize()
    m1.lock()

    m1.printf()


def guesserPro():

    global game_data

    prompt = """
1. For You vs AI
2. For AI vs AI
>>> """

    mode = int(input(prompt))
    cur_rounds = 0

    cgen = random.randint(l_limit, u_limit)
    while True:
        if mode == 1:
            m1 = Matrix("User Number", "Message")
        else:
            m1 = Matrix("AI's Number", "Message")

        if mode == 1:
            ugen = int(input("Your Guess : "))
        elif mode == 2:
            ugen = random.randint(l_limit, u_limit)

        if ugen > cgen:
            m1.unlock()
            m1.add_row(ugen, "is greater than computer's number")
            m1.lock()
            m1.printf()
        elif ugen < cgen:
            m1.unlock()
            m1.add_row(ugen, "is lesser than computer's number")
            m1.lock()
            m1.printf()
        else:
            break

        cur_rounds += 1

    if mode == 1:
        player = "You"
    else:
        player = "AI"

    game_data.append({
        "player": player,
        "attempts": cur_rounds
    })

    if input("Do you want to continue y/n : ") == "y":
        guesserPro()
    else:
        display_data()
        return


Matrix.pretty_print([
    ["Guesser Pro"]
])

guesserPro()
