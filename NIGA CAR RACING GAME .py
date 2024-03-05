print("      CAR RACING GAME  ")
started=False
in_valid_count=0
total_invalid_count=0
while True:
    command = (input("> ").lower())
    if command=="start":
        if started:
            print("CAR HAS ALREADY BEEN STARTED!")
        else:
            started=True
            print("CAR STARTED......")
    elif command == "stop":
        if not started:
            print("CAR HAS ALREADY BEEN STOPPED")
        else:
            started=False
            print("CAR HAS BEEN STOPPED")
    elif command == "help":
        print("""
        START- START THE CAR 
        STOP -STOP THE CAR
        HELP - DISPLAY THE MENU
        QUIT- QUIT THE GAME """)
    elif command =="quit":
        print("IT WAS A LOVELY DAY")
        break
    else:
        in_valid_count+=1
        if in_valid_count==2:
            print(" DONT YOU MESS WITH ME YOU MOTHERFUCKER")
        elif in_valid_count == 3:
            print("teri maa ki chut")
        elif in_valid_count == 4:
            print("tori maika choda gachar gachar")
        elif in_valid_count>4<100:
            print(" YOU SON OF A BITCH")
        else:
            print(" I DONT UNDERSTAND WHAT THE FUCK ARE YOU SAYING")
