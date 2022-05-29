from time import *
import time
import threading
import sys
import matplotlib.pyplot as plt

print("")
print("                           * * * * * * * * * * * *")
print("                           *                     *")
print("                           * Welcome to QUIZLAND *")
print("                           *                     *")
print("                           * * * * * * * * * * * *\n")
sleep(0.5)
print("Please enter your name to register.\n")
sleep(1)

user_name = input("Name: ")

data = {"User name:": user_name}
data1 = {"User name:": user_name}
data2 = {"User name:": user_name}

topdata = []

players_data = [
    {'User name:': 'James', 'Selected game:': 'Mani', 'Score:': 30, 'Time(sec):': 32},
    {'User name:': 'James', 'Selected game:': 'Histori', 'Score:': 20, 'Time(sec):': 21},
    {'User name:': 'James', 'Selected game:': 'CapACity', 'Score:': 10, 'Time(sec):': 13},
    {'User name:': 'Mary', 'Selected game:': 'Mani', 'Score:': 70, 'Time(sec):': 24},
    {'User name:': 'Mary', 'Selected game:': 'Histori', 'Score:': 90, 'Time(sec):': 26},
    {'User name:': 'Mary', 'Selected game:': 'CapACity', 'Score:': 80, 'Time(sec):': 32},
    {'User name:': 'Robert', 'Selected game:': 'Mani', 'Score:': 10, 'Time(sec):': 47},
    {'User name:': 'Robert', 'Selected game:': 'Histori', 'Score:': 10, 'Time(sec):': 33},
    {'User name:': 'Robert', 'Selected game:': 'CapACity', 'Score:': 30, 'Time(sec):': 27},
    {'User name:': 'Linda', 'Selected game:': 'Mani', 'Score:': 90, 'Time(sec):': 25},
    {'User name:': 'Linda', 'Selected game:': 'CapACity', 'Score:': 90, 'Time(sec):': 34},
    {'User name:': 'William', 'Selected game:': 'Mani', 'Score:': 100, 'Time(sec):': 23},
    {'User name:': 'William', 'Selected game:': 'Histori', 'Score:': 100, 'Time(sec):': 10},
    {'User name:': 'John', 'Selected game:': 'CapACity', 'Score:': 20, 'Time(sec):': 32},
    {'User name:': 'Elizabeth', 'Selected game:': 'Histori', 'Score:': 70, 'Time(sec):': 28},
    {'User name:': 'Charles', 'Selected game:': 'Histori', 'Score:': 40, 'Time(sec):': 24}, ]


def cap():
    capital_cities(answer_key)


def his():
    his_tori(answer_key1)


def mani():
    cur(answer_key2)


def beg():
    print("")
    print(
        "Welcome again " + user_name + "! There are three different game: CapACity , HisTori and Mani. Which one do you want to play?\n")

    game_select = input("CapACity (c) - HisTori (h) - Mani (m) :")
    print("")
    print("The game begins...")
    sleep(1.5)
    if game_select == "c":

        cap()

    elif game_select == "h":

        his()
    elif game_select == "m":

        mani()


def sec():
    print("")

    if len(topdata) == 1:

        if (topdata[0])['Selected game:'] == "CapACity":
            print(
                "Welcome again " + user_name + "! There are two different game: HisTori and Mani. Which one do you want to play?\n")
            gs = input("Mani (m) or HisTori (h) : ")
            if gs == "m":
                print("The game begins...")
                sleep(1.5)

                mani()
            elif gs == "h":
                print("The game begins...")
                sleep(1.5)

                his()



        elif (topdata[0])['Selected game:'] == "Histori":
            print(
                "Welcome again " + user_name + "! There are two different game: CapACity and Mani. Which one do you want to play?\n")
            gs = input("Mani (m) or CapACity (c) : ")
            if gs == "m":
                print("The game begins...")
                sleep(1.5)

                mani()
            elif gs == "c":
                print("The game begins...")
                sleep(1.5)

                cap()



        elif (topdata[0])['Selected game:'] == "Mani":
            print(
                "Welcome again " + user_name + "! There are two different game: CapACity and Histori. Which one do you want to play?\n")
            gs = input("HisTori (h) or CapACity (c) : ")
            if gs == "h":
                print("The game begins...")
                sleep(1.5)

                his()
            elif gs == "c":
                print("The game begins...")
                sleep(1.5)

                cap()




    elif len(topdata) == 2:

        if (topdata[0])['Selected game:'] == "CapACity" and (topdata[1])['Selected game:'] == "Histori" or (topdata[1])[
            'Selected game:'] == "CapACity" and (topdata[0])['Selected game:'] == "Histori":

            print("This game opens automatically because only this game is left that you haven't played.")
            sleep(1.5)

            mani()

        elif (topdata[0])['Selected game:'] == "CapACity" and (topdata[1])['Selected game:'] == "Mani" or (topdata[1])[
            'Selected game:'] == "CapACity" and (topdata[0])['Selected game:'] == "Mani":

            print("This game opens automatically because only this game is left that you haven't played.")
            sleep(1.5)

            his()

        elif (topdata[0])['Selected game:'] == "Mani" and (topdata[1])['Selected game:'] == "Histori" or (topdata[1])[
            'Selected game:'] == "Mani" and (topdata[0])['Selected game:'] == "Histori":

            print("This game opens automatically because only this game is left that you haven't played.")
            sleep(1.5)

            cap()


class Questions:

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


question_list = ["1. Which country's capital is Lisbon?\na. Portgual\nb. Estonia\nc. New Zeland\n",

                 "2. Which country's capital is Abu Dhabi?\na. Saudi Arabia\nb. United Arab Emirates\nc. Qatar\n",

                 "3. Which country's capital is Tehran?\na. Iran\nb. Iraq\nc. India\n",

                 "4. Which country's capital is Oslo?\na. Sweden\nb. Norwey\nc. Finland\n",

                 "5. Which country's capital is Budapest?\na. Bosnia and Herzegovin\nb. Romania\nc. Hungary\n",

                 "6. Which country's capital is Dublin?\na. Iceland\nb. Holland\nc. Ireland\n",

                 "7. Which country's capital is Tokyo?\na. China\nb. Japan\nc. South Korea\n",

                 "8. Which country's capital is Kiev?\na. Ukraine\nb. Belarus\nc. Taiwan\n",

                 "9. Which country's capital is Nur Sultan?\na. Bangladesh\nb. Kazakhistan\nc. Pakistan\n",

                 "10. Which country's capital is Warsaw?\na. Belgium\nb. Bulgaria\nc. Poland\n",
                 ]

answer_key = [

    Questions(question_list[0], "a"),
    Questions(question_list[1], "b"),
    Questions(question_list[2], "a"),
    Questions(question_list[3], "b"),
    Questions(question_list[4], "c"),
    Questions(question_list[5], "c"),
    Questions(question_list[6], "b"),
    Questions(question_list[7], "a"),
    Questions(question_list[8], "b"),
    Questions(question_list[9], "c")
]


def capital_cities(answer_key):
    dki = time.strftime("%M")
    sni = time.strftime("%S")

    score = 0
    for question in answer_key:
        answer = input(question.question + "Which is the correct answer?:\n ")
        if answer == question.answer:
            score += 10
    sleep(1)
    print("")
    print("          ***********\n")
    print("            *******  \n")
    print("              ***    \n")
    print("               *    \n")
    print("Your score for CapACity Game is ...\n ")
    sleep(1)
    print("              " + str(score))
    dks = time.strftime("%M")
    sns = time.strftime("%S")
    data["Selected game:"] = "CapACity"
    data["Score:"] = score

    if dki > dks:
        dk = 3600 - (int(dki) * 60) - int(sni) + (int(dks) * 60) + int(sns)
    else:
        dk1 = 3600 - (int(dki) * 60) - int(sni)
        dk2 = 3600 - (int(dks) * 60) - int(sns)
        dk = dk1 - dk2

    if dk >= 60:
        sonucdk = int(dk) // 60
        sonucsn = int(dk) % 60

    else:
        sonucsn = int(dk)

    data["Time(sec):"] = sonucsn
    topdata.append(data)


class Questions1:

    def __init__(self, question1, answer1):
        self.question1 = question1
        self.answer1 = answer1


question_list1 = [

    "1. What year was the French Revolution?\na. 1789\nb. 1781\nc. 1879\n",
    "2. In what year was Istanbul conquered?\na. 1543\nb. 1345\nc. 1453\n",
    "3. When did the Industrial Revolution take place?\na. 1760\nb. 1770\nc. 1780\n",
    "4. What year was the Battle of Manzikert?\na. 1299\nb. 1071\nc. 1048\n",
    "5. When did World War 1 start?\na. 1916\nb. 1915\nc. 1914\n",
    "6. When did World War 2 start?\na. 1933\nb. 1936\nc. 1939\n",
    "7. When did Christopher Columbus discover America?\na. 1492\nb. 1497\nc. 1495\n",
    "8. Which was the year the Black Death start?\na. 1350\nb. 1340\nc. 1360\n",
    "9. In what year was the atomic bomb first used?\na. 1944\nb. 1945\nc. 1946\n",
    "10. When were the Twin Towers attacked?\na. 2000\nb. 2002\nc. 2001\n",
]

answer_key1 = [

    Questions1(question_list1[0], "a"),
    Questions1(question_list1[1], "c"),
    Questions1(question_list1[2], "a"),
    Questions1(question_list1[3], "b"),
    Questions1(question_list1[4], "c"),
    Questions1(question_list1[5], "c"),
    Questions1(question_list1[6], "a"),
    Questions1(question_list1[7], "a"),
    Questions1(question_list1[8], "b"),
    Questions1(question_list1[9], "c")
]


def his_tori(answer_key1):
    dki = time.strftime("%M")
    sni = time.strftime("%S")

    score1 = 0
    for question1 in answer_key1:
        answer1 = input(question1.question1 + "Which is the correct answer?:\n ")
        if answer1 == question1.answer1:
            score1 += 10
    sleep(1)
    print("")
    print("          ***********\n")
    print("            *******  \n")
    print("              ***    \n")
    print("               *    \n")
    print("Your score for HisTori Game is ...\n ")
    sleep(1)
    print("              " + str(score1))
    dks = time.strftime("%M")
    sns = time.strftime("%S")
    data1["Selected game:"] = "Histori"
    data1["Score:"] = score1

    if dki > dks:
        dk = 3600 - (int(dki) * 60) - int(sni) + (int(dks) * 60) + int(sns)
    else:
        dk1 = 3600 - (int(dki) * 60) - int(sni)
        dk2 = 3600 - (int(dks) * 60) - int(sns)
        dk = dk1 - dk2

    if dk >= 60:
        sonucdk = int(dk) // 60
        sonucsn = int(dk) % 60

    else:
        sonucsn = int(dk)
    data1["Time(sec):"] = sonucsn
    topdata.append(data1)


class Questions2:

    def __init__(self, question2, answer2):
        self.question2 = question2
        self.answer2 = answer2


question_list2 = ["1. The dollar is the currency of which country?\na. Bahrain\nb. Barbados\nc. Benin\n",
                  "2. The peso is the currency of which country?\na. Argentina\nb. Brazil\nc. Cayman Island\n",
                  "3. The krone is the currency of which country?\na. Ethiopia\nb. Costa Rica\nc. Dominican Republic\n",
                  "4. The dinar is the currency of which country?\na. Saudi Arabia\nb. Iraq\nc. United Arab Emirates\n",
                  "5. The euro is the currency of which country?\na. Canada\nb. Italy\nc. Singapore\n",
                  "6. The rupee is the currency of which country?\na. Sri Lanka\nb. Peru\nc. Niger\n",
                  "7. The riyal is the currency of which country?\na. Lebanon\nb. Morocco\nc. Qatar\n",
                  "8. The shekel is the currency of which country?\na. Israel\nb. Seychelles\nc. Solomon Islands\n",
                  "9. The won is the currency of which country?\na. China\nb. South Korea\nc. Japan\n",
                  "10. The pound is the currency of which country?\na. Iceland\nb. Haiti\nc. Egypt\n",
                  ]
answer_key2 = [

    Questions2(question_list2[0], "b"),
    Questions2(question_list2[1], "a"),
    Questions2(question_list2[2], "c"),
    Questions2(question_list2[3], "b"),
    Questions2(question_list2[4], "b"),
    Questions2(question_list2[5], "a"),
    Questions2(question_list2[6], "c"),
    Questions2(question_list2[7], "a"),
    Questions2(question_list2[8], "b"),
    Questions2(question_list2[9], "c")
]


def cur(answer_key2):
    dki = time.strftime("%M")
    sni = time.strftime("%S")

    score2 = 0
    for question2 in answer_key2:
        answer2 = input(question2.question2 + "Which is the correct answer?:\n ")
        if answer2 == question2.answer2:
            score2 += 10
    sleep(1)
    print("")
    print("          ***********\n")
    print("            *******  \n")
    print("              ***    \n")
    print("               *    \n")
    print("Your score for Mani Game is ...\n ")
    sleep(1)
    print("              " + str(score2))
    dks = time.strftime("%M")
    sns = time.strftime("%S")
    data2["Selected game:"] = "Mani"
    data2["Score:"] = score2

    if dki > dks:
        dk = 3600 - (int(dki) * 60) - int(sni) + (int(dks) * 60) + int(sns)
    else:
        dk1 = 3600 - (int(dki) * 60) - int(sni)
        dk2 = 3600 - (int(dks) * 60) - int(sns)
        dk = dk1 - dk2

    if dk >= 60:
        sonucdk = int(dk) // 60
        sonucsn = int(dk) % 60

    else:
        sonucsn = int(dk)
    data2["Time(sec):"] = sonucsn
    topdata.append(data2)


beg()

while True:

    if len(topdata) == 3:

        print()
        print()
        print("*************************************************************")
        print("                         ANALYZES")
        print()
        print("User Name" + "       ->  ", (topdata[0])['User name:'])
        print("Selected game" + "   ->  ", (topdata[0])['Selected game:'], "  -  ", (topdata[1])['Selected game:'],
              "  -  ", (topdata[2])['Selected game:'])
        print("Score" + "           ->  ", (topdata[0])['Score:'], "   -    ", (topdata[1])['Score:'], "    -    ",
              (topdata[2])['Score:'])
        print("Time" + "            ->  ", (topdata[0])['Time(sec):'], "  -    ", (topdata[1])['Time(sec):'],
              "    -    ", (topdata[2])['Time(sec):'])
        print()
        print("*************************************************************")
        print()

        break
    else:

        print(" ")
        choise = input("Press M to return to the main menu and A to view your analysis.")

        if choise == "M" or choise == "m":
            sec()
        elif choise == "A" or choise == "a":
            if len(topdata) == 1:
                print()
                print()
                print("*************************************************************")
                print("                         ANALYZES")
                print()
                print("User Name" + "       ->  ", (topdata[0])['User name:'])
                print("Selected game" + "   ->  ", (topdata[0])['Selected game:'])
                print("Score" + "           ->  ", (topdata[0])['Score:'])
                print("Time" + "            ->  ", (topdata[0])['Time(sec):'])
                print()
                print("*************************************************************")
                print()
            elif len(topdata) == 2:
                print()
                print()
                print("*************************************************************")
                print("                         ANALYZES")
                print()
                print("User Name" + "       ->  ", (topdata[0])['User name:'])
                print("Selected game" + "   ->  ", (topdata[0])['Selected game:'], "  -  ",
                      (topdata[1])['Selected game:'])
                print("Score" + "           ->  ", (topdata[0])['Score:'], "   -  ", (topdata[1])['Score:'])
                print("Time" + "            ->  ", (topdata[0])['Time(sec):'], "  -  ", (topdata[1])['Time(sec):'])
                print()
                print("*************************************************************")
                print()

            break
a = topdata + players_data
while True:

    ls = input("Press D if you want a more detailed analysis or press X to exit: ")

    if ls == "D" or ls == "d":

        sleep(1)

        ga = input(
            "Press H to see analyzes in Histori Game press M to see analyzes in Mani Game, press C to see analyzes in CapACity Game.")

        sleep(1)
        if ga == "H" or ga == "h":

            hu = []
            hs = []
            ht = []

            for i in a:
                if i["Selected game:"] == "Histori":
                    hu.append(i["User name:"])

                    hs.append(i["Score:"])

                    ht.append(i["Time(sec):"])

            hd = {}
            hd.update(zip(hu, hs))

            hr = sorted(hd.items(), key=lambda r: r[1], reverse=True)
            num = 1
            for i in hr:
                print(num, ".", "{}  -->    {}".format(i[0], i[1]))
                num += 1

            plt.title("HISTORI", color="#D68C8C")
            plt.xlabel("USERS", color="#965959")
            plt.ylabel("SCORES", color="#965959")

            plt.bar(hu, hs, color="#FFD1D1")
            plt.show()

            plt.title("HISTORI", color="#AF7676")
            plt.xlabel("USERS", color="#AF7676")
            plt.ylabel("TIME", color="#AF7676")

            plt.bar(hu, ht, color="#F4AFAF")
            plt.show()












        elif ga == "M" or ga == "m":
            mu = []
            ms = []
            mt = []
            for i in a:
                if i["Selected game:"] == "Mani":
                    mu.append(i["User name:"])

                    ms.append(i["Score:"])

                    mt.append(i["Time(sec):"])

            md = {}
            md.update(zip(mu, ms))

            mr = sorted(md.items(), key=lambda r2: r2[1], reverse=True)
            num2 = 1
            for i in mr:
                print(num2, ".", "{}  -->    {}".format(i[0], i[1]))
                num2 += 1

            plt.title("MANI", color="#EDE411")
            plt.xlabel("USERS", color="#EDE411")
            plt.ylabel("SCORES", color="#EDE411")

            plt.plot(mu, ms, "y*")
            plt.show()

            plt.title("MANI", color="#2F542F")
            plt.xlabel("USERS", color="#2F542F")
            plt.ylabel("TIME", color="#2F542F")

            plt.plot(mu, mt, "go")
            plt.show()








        elif ga == "C" or ga == "c":
            cu = []
            cs = []
            ct = []
            for i in a:
                if i["Selected game:"] == "CapACity":
                    cu.append(i["User name:"])

                    cs.append(i["Score:"])

                    ct.append(i["Time(sec):"])

            cd = {}
            cd.update(zip(cu, cs))

            cr = sorted(cd.items(), key=lambda r1: r1[1], reverse=True)
            num1 = 1
            for i in cr:
                print(num1, ".", "{}  -->    {}".format(i[0], i[1]))
                num1 += 1

            plt.title("CAPACITY", color="#CDD9E9")
            plt.xlabel("USERS", color="#506684")
            plt.ylabel("SCORES", color="#506684")

            plt.plot(cu, cs, color="#B9CDE8")
            plt.show()

            plt.title("CAPACITY", color="blue")
            plt.xlabel("USERS", color="#425772")
            plt.ylabel("TIME", color="#425772")

            plt.plot(cu, ct, "b--")
            plt.show()






    elif ls == "X" or ls == "x":
        print("Exiting the program...")
        sleep(1.5)
        print("Program is terminated.")
        break

