Game_Command = ""
is_started = False
is_stopped = False
while True:
    Game_Command = str.lower(input(">"))
    if Game_Command == "start":
        is_stopped = False
        if is_started:
            print("car already started")
        else:
            is_started = True
            print("Car Started...Ready to go !")
    elif Game_Command == "help":
        print("""
 start - to start the car
 stop - to stop the car
 quit - to exit
        """)
    elif Game_Command == "stop":
        is_started = False
        if is_stopped:
            print("car already stopped")
        else:
            is_stopped = True
            print("car stopped.")
    elif Game_Command == "quit":
        Counter = 0
        break
    else:
        print("I don't understand that... ")


