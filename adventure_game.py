# I added a third starting choice (BEACH) with four levels of 
# nested choices, exceeding the minimum three level requirement.
# I showwed the game to my colleague at the office and he liked it.

print("""Your boat has just capsized and you are washed ashore. 
You see a CAVE, FOREST and the BEACH.""")
ashore = input("Where do you go, CAVE, FOREST or BEACH? ").lower()
if ashore == "cave":
    print ("""Inside the cave, you find a PATH riddled
with snakes and a rickety BRIDGE on the verge of collapse. 
Do you take the PATH or the BRIDGE?""")
    cave = input("PATH or BRIDGE? ").lower()
    if cave == "path":
        print("""you pick up a stick and take the path. 
You fend off the snakes with the stick and 
get to the other side of the cave where you 
come out in a clearing. You see some native people. 
Do you CALLOUT or WAIT to see if they are friendly.""")
        path = input("CALLOUT or WAIT? ").lower()
        if path == "callout":
            print("""you call out to the native people and 
they take you home, you are saved.""")
        elif path == "wait":
            print("""you wait too long and do not notice a 
venomous snake creeping up on you. 
It bites you and you are killed.""")
        else:
            print("Invalid response, CALLOUT or WAIT")
    elif cave == "bridge":
        print("""you take the bridge, it creaks and breaks, 
you fall into the icy cold water below. 
Do you follow the CURRENT out to sea or hold on to a 
BRANCH in the water and scream for help.""")
        bridge = input("CURRENT or BRANCH? ").lower()
        if bridge == "current":
            print("""you follow the current out to sea and 
find yourself in shark-infested waters and get eaten alive.""")
        elif bridge == "branch":
            print("""you hold on to the branch and scream 
for help. Luckily, some scientists carrying out research 
in the cave hear you and you are saved. Congratulations!""")
        else:
            print("Invalid response, CURRENT or BRANCH")
    else:
        print("Invalid response, PATH or BRIDGE.")
elif ashore == "forest":
    print("""You go into the forest and find two paths. 
A MUDDY PATH and a DRY PATH.
Do you take the dry or muddy path?
""")
    forest = input("MUDDY PATH or DRY PATH? ").lower()
    if forest == "muddy path":
        print("""you take the muddy path and get to a 
clearing, where you find another boat. 
Do you SHOUT or IGNORE them.""")
        muddypath = input("SHOUT or IGNORE? ").lower()
        if muddypath == "shout":
            print("""you shout for help and the people on 
the boat hear you. It turns out they are pirates and they 
capture you.""")
        elif muddypath == "ignore":
            print("""you ignore them and keep going. 
You find some natives and they save you.""")
        else:
            print("Invalid response, SHOUT or IGNORE")
    elif forest == "dry path":
        print("""you choose the dry path and find a cabin. 
Do you ENTER or PASS.""")
        drypath = input("ENTER CABIN or PASS? ").lower()
        if drypath == "enter cabin":
            print("""You enter the cabin and find a radio. 
You are able to call for help and you are rescued. 
Congratulations!""")
        elif drypath == "pass":
            print("""you fearfully pass the cabin, 
not sure of what/who is inside. 
You keep going and come face to face with a huge bear, 
and it overpowers you.""")
        else:
            print("Invalid response, ENTER CABIN or PASS")
    else:
        print("Invalid response, MUDDY PATH or DRY PATH.")
elif ashore == "beach":
    print("""You choose to remain on the beach. 
This offers two choices, STAY on the beach until you spot 
a passing boat or ship, or FORAGE for food. """)
    beach = input("STAY or FORAGE? ").lower()
    if beach == "stay":
        print("""you stay on the beach and wait. 
After several hours, you notice smoke rising in the 
distance and hear strange noises from farther down the shore. 
Do you INVESTIGATE the smoke or BUILD a signal fire 
and remain where you are.""")
        stay = input("INVESTIGATE or BUILD FIRE? ").lower()
        if stay == "investigate":
            print("""you walk toward the smoke and 
discover an abandoned campsite. 
Inside, you find a map and some supplies. 
Suddenly, you hear footsteps nearby. 
Do you HIDE or CALL OUT.""")
            investigate = input("HIDE or CALLOUT? ").lower()
            if investigate == "hide":
                print("""you hide behind some rocks 
and see that the footsteps belong to a rescue team 
searching the island. Once they leave, you follow 
their tracks and are rescued. Congratulations!""")
            elif investigate == "callout":
                print("""you call out loudly, but the 
people are not rescuers. They are smugglers hiding 
stolen goods on the island, and they capture you.""")
            else:
                print("Invalid response, HIDE or CALLOUT.")
        elif stay == "build fire":
            print("""you build a large signal fire on the 
beach. As night falls, a passing cargo ship notices 
the smoke. Do you WAVE frantically or LEAVE 
the beach to search for water while waiting.""")
            buildfire = input("WAVE or LEAVE? ").lower()
            if buildfire == "wave":
                print("""you wave frantically and the 
crew spots you. They send a rescue boat and you are saved. 
Congratulations!""")
            elif buildfire == "leave":
                print("""you leave the beach searching for 
water, but you lose your way in the dark jungle and are 
never seen again. Sorry.""")
            else:
                print("Invalid response, WAVE or LEAVE")
        else:
            print("Invalid response, INVESTIGATE or BUILD FIRE.")
    elif beach == "forage":
        print("""you leave the beach to search for food. 
After walking for a while, you find a PALM GROVE 
filled with coconuts and a small LAGOON with fish swimming 
in it. Do you go to the PALM GROVE or the LAGOON.""")
        forage = input("PALM GROVE or LAGOON? ").lower()
        if forage == "palm grove":
            print("""you climb a palm tree to collect 
coconuts. While at the top, you spot a helicopter flying 
overhead. Do you CLIMB DOWN and signal it or 
STAY hidden in the tree.""")
            palmgrove = input("CLIMB DOWN or STAY? ").lower()
            if palmgrove == "climb down":
                print("""you quickly climb down and use 
shiny coconuts to reflect sunlight toward the helicopter. 
The pilot notices you and you are rescued. Congratulations!""")
            elif palmgrove == "stay":
                print("""you stay hidden in the tree too long. 
The branch snaps and you fall, injuring yourself badly 
with no way to escape the island.. Sorry.""")
            else:
                print("Invalid response, CLIMB DOWN or STAY")
        elif forage == "lagoon":
            print("""you head to the lagoon and try to 
catch fish. While there, you notice a small raft tied 
near the reeds. Do you USE the raft or 
SEARCH the area first.""")
            lagoon = input("USE or SEARCH? ").lower
            if lagoon == "use":
                print("""you use the raft to leave the 
island, but a sudden storm overturns it and you disappear 
into the sea. Sorry""")
            elif lagoon == "search":
                print("""you search carefully around the 
lagoon and discover the raft belongs to some friendly fishermen nearby. 
They take you aboard and bring you safely home. 
Congratulations!""")
            else: 
                print("Invalid response, USE or SEARCH")
        else: 
            print("Invalid response, PALM GROVE or LAGOON")
    else:
        print("Invalid response, STAY or FORAGE.")
else:
    print("Invalid response, CAVE, FOREST, or BEACH.")