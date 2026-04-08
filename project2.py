questionsright = 0
questionsdone = 0
lives = 5

print ("welcome to quiz")
input ()
print ("you get 5 lives and there are  10 questions")
input ()
answer1 = input ("what is the capital of france? ")
if answer1 == "paris":
    questionsright += 1
    print ("correct!")
else:
    lives -=1
    print ("wrong :(")
questionsdone += 1
print (f"{questionsright}/{questionsdone} right so far!")
input ()
answer2 = input ("5.5 x 3? ")
if answer2 == "16.5":
    questionsright += 1
    print ("correct!")
else   :
    lives -=1
    print ("wrong :(")
questionsdone += 1
input ()
print (f"{questionsright}/{questionsdone} right so far!")
answer3 = input ("is the teacher's name josh?")
if answer3 == "yes":
    questionsright += 1
    print ("correct!")
else   :
    lives -=1
    print ("wrong :(")
questionsdone += 1
input ()
print (f"{questionsright}/{questionsdone} right so far!")
answer4 = input ("which president was obama?(example: 1st) ")
if answer4 == "44th":
    questionsright += 1
    print ("correct!")
else   :
    lives -=1
    print ("wrong :(")
questionsdone += 1
input ()
print (f"{questionsright}/{questionsdone} right so far!")
answer5 = input ("what does STEM stand for?(shorten)")
if answer5 == "science tech engineering math" or answer5 == "Science tech engineering math":
    questionsright += 1
    print ("correct!")
else   :
    lives -=1
    print ("wrong :(")
    if lives == 0:
        input ("you lost :(" )
        quit ()
questionsdone += 1
input ()
print (f"{questionsright}/{questionsdone} right so far!")
answer6 = input ("who is the current monarch of Britain?(spell out) ")
if answer6 == "king charles" or answer6 == "King Charles" or answer6 == "king charles the third" or answer6 == "King Charles The Third":
    questionsright += 1
    print ("correct!")
else   :
    lives -=1
    print ("wrong :(")
    if lives == 0:
        input ("you lost :(" )
        quit ()
questionsdone += 1
input ()
print (f"{questionsright}/{questionsdone} right so far!")
answer7 = input ("biggest dog breed? ")
if answer7 == "great dane" or answer7 == "Great Dane":
    questionsright += 1
    print ("correct!")
else   :
    lives -=1
    print ("wrong :(")
    if lives == 0:
        input ("you lost :(" )
        quit ()
questionsdone += 1
input ()
print (f"{questionsright}/{questionsdone} right so far!")
answer8 = input ("What is the famous line Hamlet said? ")
if answer8 == "to be or not to be, that is the question" or answer8 == "To be or not to be, that is the question" or answer8 == "to be or not to be that is the question" or answer8 == "To be or not to be that is the question":
    questionsright += 1
    print ("correct!")
else   :
    lives -=1
    print ("wrong :(")
    if lives == 0:
        input ("you lost :(" )
        quit ()
questionsdone += 1
input ()
print (f"{questionsright}/{questionsdone} right so far!")
answer9 = input ("does the average person have a pet? ")
if answer9 == "yes" or answer9 == "Yes":
    questionsright += 1
    print ("correct!")
else   :
    lives -=1
    print ("wrong :(")
    if lives == 0:
        input ("you lost :(" )
        quit ()
questionsdone += 1
input ()
print (f"{questionsright}/{questionsdone} right so far!")
input ()
print ("last question!!!")
input ()
answer7 = input ("name 15 digits of pi (dont search it up) ")
if answer7 == "3.14159265358979" :
    questionsright += 1
    print ("correct!")
else   :
    lives -=1
    print ("wrong :(")
    if lives == 0:
        input ("you lost :(" )
        quit ()
questionsdone += 1
input ()
print ("you win!!!")
input ()
print (f"you ended with a score of {questionsright}/{questionsdone}, with {lives} lives remaining!")
input ()
if lives == 5 and questionsright == 10 :
    print ("you got a perfect score!")
    print ("                                                                                                    ")
    print ("                                                                                                    ")    
    print ("                                       ::----:.                                                     ")
    print ("                                    .--:::::...:--                                                  ")
    print ("                                   :-::........ ..--                                                ")
    print ("                                  .-:...........  ..=                                               ")
    print ("                                  :::............  .:-                                              ")
    print ("                                 .=:............... .+                                              ")
    print ("                                 .-................ .-                                              ")
    print ("                                 -:..................-                                              ")
    print ("                                .=:::................+                                              ")
    print ("                                =::::..............::-                                              ")
    print ("                   .===-::::-==+=--::::............:+                                               ")
    print ("               .=-:...........::::-==-:::::::::::::=                                                ")
    print ("            .=-:.....:::::::::::::::::-=-::::::::-:                                                 ")
    print ("          :-:::::::::::::::::::::::::..::-=--:---.                                                  ")
    print ("        .=:::::::::::.......:::::::........:==:             ...........                             ")
    print ("      .=::::::::.............................-=       ..-=---:=+*##*-::----:.                       ")
    print ("     .-::::::.................................--. .---:---::-%%%*+*#+....::-----.                   ")
    print ("    .-:::::....................................:-=:--::....:%+................:----.                ")
    print ("   .-:::::............----:.....................:=-:.......:....................:+*+=:              ")
    print ("   -:::::..................::--..................-:.............................#%%%%=-:            ")
    print ("  .-:::::......................::--...............-................................:#%-:-.          ")
    print ("  -:::::...........................:=-............=:.......:--=*+--..................+=::--         ")
    print ("  -:::::..............................-=:..:......=.......:=@=:.::##:.................-::::-.       ")
    print ("  =::::.................................:=-...:..:-.......#=      ..@:......:-----:......:::--      ")
    print ("  =::::...................................:=:::::-:......++   =+     @.....:-@@@@@@=:....:::::-     ")
    print ("  -:::::....................................=-.:=:......=+  %  :-+   .-...:@.       @=:...::::-:    ")
    print ("  ::::::..........-=:........................-+:..:.....=+ #=  @@=.   -...=.  #+     .#...:::::-.   ")
    print ("  .-::::...............==....................:=:.....::==: +=@@@@+.   -...* . .#*+     +..:::::-:   ")
    print ("   -::::..................:=:.................:-.....::--:-:*=@ .=   *:...=.- -@@#:    -::::::::-.  ")
    print ("   .-::::....................:=:..............-:.......:-::.:=@@.   .-.....-**@@.=-    :-:::::::-.  ")
    print ("    :-:::::....................:=:...........:+.:----:::::....-   ..=......:-*==+#    .-:::::::::-  ")
    print ("     .-:::::.....................:-:....:::::=........=.::.....-..+-.........-       ..=:::::::::-  ")
    print ("       =:::::.....................:-::.::::=-..........-........:.............-:. ..-::::-:::::::-  ")
    print ("        .-:::::::..................:----==::............::......................--::----:::::::::-  ")
    print ("          .-::::::::::......::.....:--:::::::...........:##-...................:::::::....:::::::-  ")
    print ("            .--::::::::::::::::::::---:::::::............+@- :.:...................::-=-:::::::::-  ")
    print ("               .:--::::::::::::::-=:..:::::::::..........:%@:   ..:-:::::::.......::::.:::::::::-.  ")
    print ("                   ..:-=======-:. .-...:::::::............+@@%        ......+**=:::....:::::::::-.  ")
    print ("                                   :....::::::::..........:%@@@%.          .@%=.......:::::::::-.   ")
    print ("                                   .:.....::::::...........-%@@@@@@+     .#@%=........::::::::-:    ")
    print ("                                    .-......::::::..........=*+#@@@@@@@@@@@@+........:::::::::-.    ")
    print ("                                     ::......::::::..........+**###@@@@@@@%%:.....:::::::::-:-.     ")
    print ("                                      .-......:::::::.........-####*#%@@@%%-:....:::::::::::=       ")
    print ("                                        =:......:::::::::...:..:+#####%%%#-:::::::::::::::--        ")
    print ("                                         .-.......::::::::::.:-:.::=***=:::::::::::::::::-.         ")
    print ("                                          .--.......::::::::::::-:::::::::::::::::::::--:           ")
    print ("                                             --:......::::::::::::::::::::::::::::::---             ")
    print ("                                               :-:......::::::::::::::::::::::::-----               ")
    print ("                                                  :--.....::::::::::::::::::-----:.                 ")
    print ("                                                     .---:::::--::::::--------.                     ")
    print ("                                                          ..:--::::-::::.                           ")
    print ("                                                                                                    ")                                                                                                 
elif questionsright < 10 and questionsright > 8:
    print ("you were close to perfect!")
elif questionsright < 8:
    print ("you tried your best!")