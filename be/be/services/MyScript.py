from output_from_sevice import OutputFromService

outputFromService = OutputFromService

outputFromService.initialize_session(outputFromService)

#option 1 - get new word
#option 2 - enter input
#option 3 - word found
#option 4 - exit

option = 1

while option!= "4" and option!="3":
    print("Enter option: ", end="")
    option = input()
    if option == "1":
        outputFromService.get_suggested_word(outputFromService)
    elif option == "2":
        outputFromService.set_result_from_game(outputFromService)
    elif option == "3":
        print("Word found")
    elif option == "4":
        print("Terminate program")