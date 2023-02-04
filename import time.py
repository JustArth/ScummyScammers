import time
import pyfiglet


def printt(string, strDelay):
  for i in str(string + "\n"):
    print(i, end="", flush=True)
    time.sleep(strDelay)


result = pyfiglet.figlet_format("Scummy Scammers", font="big")
print(result)
printt("I recommend you import this to visual studio for better performance. ", 0.02)
printt('Welcome to Scummy Scammers!\n', 0.04)
skipIntro = input("Skip the intro? 1 for yes, 2 for no ")
if skipIntro == "2":
  printt(
    "You are broke, with a paperclip to your name, so you result to be a scammer and your goal is to make $800k by scamming.\n",
    0.02)
  printt(
    'You setup a fake microsoft help service and you “work” in it, make sure you scam the right people or you get reverse scammed and your money goes DOWN.\n',
    0.02)
  printt(
    'You are given a choice if you want to scam them or not, there will be a total of 12 people to scam before the business closes and relocates. Be careful though, some people will have very suspicious voice, or their description may be a little middle aged. Some will be old people or young kids with their moms credit card.\n',
    0.02)

commandlist = ['Description', 'Hack', 'Stats']
fakeName = input('Start with a fake scammer name. ')
if fakeName == 'Rajeesh':
  printt('YOUR A NATURAL, Rajeesh is the superior one.', 0.02)
if fakeName == 'Elias':
  printt('Nice try...', 0.02)
  quit("Bye Bye Elias")
if fakeName == 'elias':
  printt('Nice try...', 0.02)
  quit("Bye Bye Elias")
if fakeName == 'Blackwell':
  printt('Nice try...', 0.02)
  quit("Bye Bye Elias")
if fakeName == 'blackwell':
  printt('Nice try...', 0.02)
  quit("Bye Bye Elias")
if fakeName == 'Elia$':
  printt('Nice try...', 0.02)
  quit("Bye Bye Elias")
if fakeName == 'elia$':
  printt('Nice try...', 0.02)
  quit("Bye Bye Elias")
if fakeName == 'Arth':
  printt('Welcome leader, this will be easy for you.', 0.02)

else:
  printt(f"Alrighty then, {fakeName} let the scamming begin!", 0.02)
CharName = fakeName
money = 0
scammed = 0
gotScammed = 0
AvoidedScam = 0
MissedScam = 0
Timmy = 'Timmy'
TimmyMoney = 200000
TimmyBio = "Timmy is a 6 year old kid who got a comupter virus, he is currently on the phone with you. Its a good thing he fell for your fake virus, now all you need to do is get the numbers. Oh wait, he has a speach impediment. Type 1 for hack and 2 for flee. "
Jimmy = 'Jimmy'
JimmyMoney = 80000
JimmyBio = 'Jimmy is a 8 year old kid who saw your ad for free robux, all he has to do is put in the bank details. His parents are near, so you have to be careful on how you want him to answer to not rise suspicion. Type 1 for hack and 2 for flee. '
Harold = 'Harold'
HaroldMoney = 20000
HaroldBio = 'You texted a 7 year old kid about a package that doesnt exist. So you made a ip logger and made him click a sketchy link. You will now threaten him, for his money, and sell his info anyways. Type 1 for hack and 2 for flee. '
Peter = 'Peter'
PeterMoney = 50000
PeterBio = "He has a Iq of a poptart, but he loves singing about them. Make sure you get that money and act like nothing happenend. Type 1 for hack and 2 for flee. "
Cleveland = "Cleveland"
ClevelandMoney = -100
ClevelandBio = "This man is so broke you owe him money, dont scam him........... trust me.......... yeaaaaaaa....... Type 1 for hack and 2 for flee. "
Quagmire = "Quagmire"
QuagmireMoney = 300000
QuagmireBio = "He isnt very tech savvy, so this should be a peice of cake.  Type 1 for hack and 2 for flee. "
Johnathen = 'Johnathen'
JohnathenMoney = -20000
JohnathenBio = 'This guy has what sounds like a voice changer and with further inspection, you see that they are using a virtual machine. They dont sound very tech savvy, and they sound very old. Type 1 for hack and 2 for flee. '
Andrew = 'Andrew'
AndrewMoney = 40000
AndrewBio = "Your call is glitching out and you don't have a great connection, you hear a glitch in his voice, but you dont think much of it. Type 1 for hack and 2 for flee. "
John = 'John'
JohnMoney = 7000
JohnBio = 'John is a guy who does pretty well with computers, but is really gullible. He has 7k to get, so treat him nicely Type 1 for hack and 2 for flee. '
Jacob = 'Jacob'
JacobMoney = 100000
JacobBio = "This guy's father is loaded, he is rich to Get that money and go on, should be easy. Type 1 for hack and 2 for flee. "
Daab = 'Mr.Daab'
DaabMoney = money
DaabBio = 'This man teaches engeneering, thats all you need to know. '
#rob this guy and all your money is gone....#
Keith = 'Keith'
KeithMoney = 3000
KeithBio = 'What a weird name, anyway, have a good time though, he is very oblivious, so this should be very easy. Type 1 for hack and 2 for flee. '
timmyhack = input(f"A local {Timmy} appeared! {TimmyBio}")
if timmyhack == "1":
  printt(f"You hack timmy and gain {TimmyMoney}", 0.02)

  money += TimmyMoney
  scammed += 1
if timmyhack == "2":
  printt("You decide not to hack and move on", 0.02)

  MissedScam += 1
printt(f"stats for {fakeName}", 0.02)
printt(f"you have ${money}!", 0.02)
printt(f"You have scammed {scammed} time(s)", 0.02)
printt(f'you got scammed {gotScammed} time(s)', 0.02)
printt(f'you dodged getting scammed {AvoidedScam} times!', 0.02)
printt(f'You have missed an Opportunity to scam {MissedScam} times!', 0.02)
jimmyhack = input(f"A local {Jimmy} appeared! {JimmyBio}")
if jimmyhack == "1":
  printt(f"You hack Jimmy and gain {JimmyMoney}", 0.02)

  money += JimmyMoney
  scammed += 1
if jimmyhack == "2":
  printt("You decide not to hack and move on", 0.02)

  MissedScam += 1
printt(f"stats for {fakeName}", 0.02)
printt(f"you have ${money}!", 0.02)
printt(f"You have scammed {scammed} time(s)", 0.02)
printt(f'you got scammed {gotScammed} time(s)', 0.02)
printt(f'you dodged getting scammed {AvoidedScam} times!', 0.02)
printt(f'You have missed an Opportunity to scam {MissedScam} times!', 0.02)
haroldhack = input(f"A local {Harold} appeared! {HaroldBio}")
if haroldhack == "1":
  printt(f"You hack {Harold} and gain {HaroldMoney}", 0.02)

  money += HaroldMoney
  scammed += 1
if haroldhack == "2":
  print("You decide not to hack and and move on", 0.02)

  MissedScam += 1
printt(f"stats for {fakeName}", 0.02)
printt(f"you have ${money}!", 0.02)
printt(f"You have scammed {scammed} time(s)", 0.02)
printt(f'you got scammed {gotScammed} time(s)', 0.02)
printt(f'you dodged getting scammed {AvoidedScam} times!', 0.02)
printt(f'You have missed an Opportunity to scam {MissedScam} times!', 0.02)
peterhack = input(f"A local {Peter} appeared! {PeterBio}")
if peterhack == ('1'):
  printt(f'You hacked peter and you got {PeterMoney}', 0.02)

  money += PeterMoney
  scammed += 1
if peterhack == ("2"):
  printt('you decided not to hack and move on', 0.02)

  MissedScam += 1
printt(f"stats for {fakeName}", 0.02)
printt(f"you have ${money}!", 0.02)
printt(f"You have scammed {scammed} time(s)", 0.02)
printt(f'you got scammed {gotScammed} time(s)', 0.02)
printt(f'you dodged getting scammed {AvoidedScam} times!', 0.02)
printt(f'You have missed an Opportunity to scam {MissedScam} times!', 0.02)
clevelandhack = input(f"A local {Cleveland} appeared! {ClevelandBio}")
if clevelandhack == "1":
  printt("You hack Cleveland and LOSE MONEY YOU IDIOT WHY WOULD YOU DO THAT ",
         0.02)

  money += ClevelandMoney
  gotScammed += 1
if clevelandhack == "2":
  printt("You decide not to hack and move on", 0.02)

  AvoidedScam += 1
printt(f"stats for {fakeName}", 0.02)
printt(f"you have ${money}!", 0.02)
printt(f"You have scammed {scammed} time(s)", 0.02)
printt(f'you got scammed {gotScammed} time(s)', 0.02)
printt(f'you dodged getting scammed {AvoidedScam} times!', 0.02)
printt(f'You have missed an Opportunity to scam {MissedScam} times!', 0.02)
Quagmirehack = input(f"A local {Quagmire} appeared! {QuagmireBio}")
if Quagmirehack == "1":
  printt(f"You hack Quagmire and gain {QuagmireMoney}", 0.02)

  money += QuagmireMoney
  scammed += 1
if Quagmirehack == "2":
  printt("You decide not to hack and move on", 0.02)

  MissedScam += 1
printt(f"stats for {fakeName}", 0.02)
printt(f"you have ${money}!", 0.02)
printt(f"You have scammed {scammed} time(s)", 0.02)
printt(f'you got scammed {gotScammed} time(s)', 0.02)
printt(f'you dodged getting scammed {AvoidedScam} times!', 0.02)
printt(f'You have missed an Opportunity to scam {MissedScam} times!', 0.02)
Johnathenhack = input(f"A local {Johnathen} appeared! {JohnathenBio}")
if Johnathenhack == "1":
  printt(f"You hack Johnathen and gain {JohnathenMoney}", 0.02)

  money += JohnathenMoney
  scammed += 1
if Johnathenhack == "2":
  printt("You decide not to hack and move on", 0.02)

  AvoidedScam += 1
printt(f"stats for {fakeName}", 0.02)
printt(f"you have ${money}!", 0.02)
printt(f"You have scammed {scammed} time(s)", 0.02)
printt(f'you got scammed {gotScammed} time(s)', 0.02)
printt(f'you dodged getting scammed {AvoidedScam} times!', 0.02)
printt(f'You have missed an Opportunity to scam {MissedScam} times!', 0.02)
Andrewhack = input(f"A local {Andrew} appeared! {AndrewBio}")
if Andrewhack == "1":
  printt(f"You hack Andrew and gain {AndrewMoney}", 0.02)

  money += AndrewMoney
  scammed += 1
if Andrewhack == "2":
  printt("You decide not to hack and move on", 0.02)

  MissedScam += 1
printt(f"stats for {fakeName}", 0.02)
printt(f"you have ${money}!", 0.02)
printt(f"You have scammed {scammed} time(s)", 0.02)
printt(f'you got scammed {gotScammed} time(s)', 0.02)
printt(f'you dodged getting scammed {AvoidedScam} times!', 0.02)
printt(f'You have missed an Opportunity to scam {MissedScam} times!', 0.02)
Johnhack = input(f"A local {John} appeared! {JohnBio}")
if Johnhack == "1":
  printt(f"You hack John and gain {JohnMoney}", 0.02)

  money += JohnMoney
  scammed += 1
if Johnhack == "2":
  printt("You decide not to hack and move on", 0.02)

  MissedScam += 1
printt(f"stats for {fakeName}", 0.02)
printt(f"you have ${money}!", 0.02)
printt(f"You have scammed {scammed} time(s)", 0.02)
printt(f'you got scammed {gotScammed} time(s)', 0.02)
printt(f'you dodged getting scammed {AvoidedScam} times!', 0.02)
printt(f'You have missed an Opportunity to scam {MissedScam} times!', 0.02)
Jacobhack = input(f"A local {Jacob} appeared! {JacobBio}")
if Jacobhack == "1":
  printt(f"You hack Jacob and gain {JacobMoney}", 0.02)

  money += JacobMoney
  scammed += 1
if Jacobhack == "2":
  printt("You decide not to hack and move on", 0.02)

  MissedScam += 1
printt(f"stats for {fakeName}", 0.02)
printt(f"you have ${money}!", 0.02)
printt(f"You have scammed {scammed} time(s)", 0.02)
printt(f'you got scammed {gotScammed} time(s)', 0.02)
printt(f'you dodged getting scammed {AvoidedScam} times!', 0.02)
printt(f'You have missed an Opportunity to scam {MissedScam} times!', 0.02)
Keithhack = input(f"A local {Keith} appeared! {KeithBio}")
if Keithhack == "1":
  printt(f"You hack Keith and gain {KeithMoney}", 0.02)

  money += KeithMoney
  scammed += 1
if Keithhack == "2":
  printt("You decide not to hack and move on", 0.02)

  MissedScam += 1
printt(f"stats for {fakeName}", 0.02)
printt(f"you have ${money}!", 0.02)
printt(f"You have scammed {scammed} time(s)", 0.02)
printt(f'you got scammed {gotScammed} time(s)', 0.02)
printt(f'you dodged getting scammed {AvoidedScam} times!', 0.02)
printt(f'You have missed an Opportunity to scam {MissedScam} times!', 0.02)

Daabhack = input(f"A local {Daab} appeared! {DaabBio}", )
if Daabhack == "1":
  print(f"so you have chosen death, {fakeName}", end='')

  printt('...', 0.5)
  printt(
    "if you want to escape from Mr. Daab, then you must fight for survival",
    0.02)

  printt("You have 2 options", 0.02)
  DaabFightChoice = input("[Fight] 1, or [Flee] 2. What is your choice? ")
  if DaabFightChoice == "1":
    printt("You attack Mr.Daab with HACK ATTACK", 0.02)
    time.sleep(2.5)
    printt("Daab Countered with REVERSE HACK", 0.02)
    time.sleep(2.5)
    printt("you got hacked off your computer...", 0.02)
    printt("what did you expect?", 0.02)
    printt("Take this ending and dont come here again", 0.02)
    printt("Ending: 5/6", 0.02)
    quit("Nice Try")
  if DaabFightChoice == "2":
    printt(
      "You decide... nah just kidding, you die anyway, don't cross Mr.Daab Like that",
      0.02)
    printt("Ending: 6/6", 0.02)
    quit("Bye")
if Daabhack == "2":
  printt("You decide not to hack and move on", 0.02)
  AvoidedScam += 1
printt(f"stats for {fakeName}", 0.02)
printt(f"you have ${money}!", 0.02)
printt(f"You have scammed {scammed} time(s)", 0.02)
printt(f'you got scammed {gotScammed} time(s)', 0.02)
printt(f'you dodged getting scammed {AvoidedScam} times!', 0.02)
printt(f'You have missed an Opportunity to scam {MissedScam} times!', 0.02)

if money == 800000:
  printt("Master Hacker... Ending: (1/6)", 0.02)
if money == 0:
  printt("Pacifist ending, You hacked no one!... Ending: (2/6)", 0.02)
if 1 <= money <= 799999:
  printt("Average Hacker... Ending: (3/6)", 0.02)

if -999999999999 <= money <= -1:
  printt(
    "How did you even..? Nvm take the ending and get outta here!... Ending: (4/6) ",
    0.02)

quit("End of run")
