'''
Building the car game ::
  CAR GAME:
        > help
          start - to start the car
          stop - to stop the car
          quit - to exit
        > asd
          I don't understand this
        > start
          Car started... Ready to go!!
          >start
           Car had already started!!
        > stop
          Car stopped..
          >stop
           Car had already stopped!!
        > quit
'''

command= ""
started =False
while True :
    command = input("> ").lower()
    if command == "start":
        if started :
            print("car has already started.")
        else:
            started == True
            print('car started')
    elif command == "stop":
        if  started==False :
            print("car is stoped")
        else:
            started = True
            print("car stopped")
    elif command == "help":
        print('''
start - to start the car
stop - to stop the car
quit - to exit
        ''')
    elif command == "quit":
        break
    else:
        print("i don't understand this.")



