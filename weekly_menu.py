# importing a libraries responsible for cleaning the console, and 
import os, msvcrt
wrong_input = ("\033[1;31;40m\nI do not understand what you mean. Please try again.\n")
get_char = msvcrt
# begin functions
def else_cond():
        print(wrong_input)
        print("\033[1;37;40mPress spacebar to continue...")
        get_char.getch()
        lets_start()
def lets_start():
        os.system("cls")
        print("\nSimple menu using functions and variables.\n"
        "Enter day of the week and time of meal to see menu. You can choose between meals like:\n\n"
        "\033[1;32;40mbreakfast\033[1;37;40m | \033[1;33;40msec breakfast\033[1;37;40m | \033[1;34;40mlunch\033[1;37;40m | \033[1;36;40mdinner\033[1;37;40m\n"
        "\neg. 'Monday sec breakfast' or 'Wednesday dinner'"
        )
        choice = input("\nWhat's your choice?: ")
        if choice.lower() == "monday breakfast":
                monday_break()
        elif choice.lower() == "monday sec breakfast":
                monday_sec_break()
        elif choice.lower() == "monday lunch":
                monday_lunch()
        elif choice.lower() == "monday dinner":
                monday_dinner()
        elif choice.lower() == "tuesday breakfast":
                tuesday_break()
        elif choice.lower() == "tuesday sec breakfast":
                tuesday_sec_break()
        elif choice.lower() == "tuesday lunch":
                tuesday_lunch()
        elif choice.lower() == "tuesday dinner":
                tuesday_dinner()
        elif choice.lower() == "wednesday breakfast":
                wednesday_break()
        elif choice.lower() == "wednesday sec breakfast":
                wednesday_sec_break()
        elif choice.lower() == "wednesday lunch":
                wednesday_lunch()
        elif choice.lower() == "wednesday dinner":
                wednesday_dinner()
        elif choice.lower() == "thursday breakfast":
                thursday_break()
        elif choice.lower() == "thursday sec breakfast":
                thursday_sec_break()
        elif choice.lower() == "thursday lunch":
                thursday_lunch()
        elif choice.lower() == "thursday dinner":
                thursday_dinner()
        elif choice.lower() == "friday breakfast":
                friday_break()
        elif choice.lower() == "friday sec breakfast":
                friday_sec_break()
        elif choice.lower() == "friday lunch":
                friday_lunch()
        elif choice.lower() == "friday dinner":
                friday_dinner()
        elif choice.lower() == "saturday breakfast":
                saturday_break()
        elif choice.lower() == "saturday sec breakfast":
                saturday_sec_break()
        elif choice.lower() == "saturday lunch":
                saturday_lunch()
        elif choice.lower() == "saturday dinner":
                saturday_dinner()
        elif choice.lower() == "sunday breakfast":
                sunday_break()
        elif choice.lower() == "sunday sec breakfast":
                sunday_sec_break()
        elif choice.lower() == "sunday lunch":
                sunday_lunch()
        elif choice.lower() == "sunday dinner":
                sunday_dinner()
        elif choice.lower() == "exit":
                goodbye()
        else:
                else_cond()
def monday_break():
        os.system("cls")
        print(
        "\nMonday breakfast\n"
        "----------------\n"
        "'Porridge with fruits'\n"
        "- porridge 60g\n"
        "- natural yogurt 300g\n"
        "- blueberries and raspberries 200g\n"
        "- walnuts 25g\n"
        "- natural honey 25g\n\n")
        print("\033[1;37;40mPress spacebar to continue...")
        get_char.getch()
        lets_start()
def monday_sec_break():
        os.system("cls")
        print(
        "\nMonday second breakfast\n"
        "-----------------------\n"
        "'Greek salad with chicken'\n"
        "- chicken 200g\n"
        "- tomato 80g\n"
        "- pepper 140g\n"
        "- cucumber 50g\n"
        "- onion 50g\n"
        "- spinach 50g\n"
        "- sunflower oil 10ml\n"
        "- bread 80g\n")
        print("\033[1;37;40mPress spacebar to continue...")
        get_char.getch()
        lets_start()
def monday_lunch():
        os.system("cls")
        print(
        "\nMonday lunch\n"
        "------------\n"
        "'Spaghetti'\n"
        "- turkey 250g\n"
        "- pasta 30g\n"
        "- mushrooms 65g\n"
        "- onion 25g\n"
        "- sunflower oil 5ml\n"
        "- tomato sauce 500ml\n"
        "- cheddar 50g\n")
        print("\033[1;37;40mPress spacebar to continue...")
        get_char.getch()
        lets_start()
def monday_dinner():
        os.system("cls")
        print(
        "\nMonday dinner\n"
        "-------------\n"
        "'Toasts with mozarella cheese'\n"
        "- toasted bread 80g\n"
        "- mozarella 125g\n"
        "- tomato 100g\n"
        "- olive oil 5ml\n")
        print("\033[1;37;40mPress spacebar to continue...")
        get_char.getch()
        lets_start()
def tuesday_break():
        os.system("cls")
        print(
        "\nTuesday breakfast\n"
        "-----------------\n"
        "'White cheese with vegetables'\n"
        "- white cheese 150g\n"
        "- natural yoghurt 100g\n"
        "- peper 100g\n"
        "- radish 50g\n"
        "- chive 20g\n"
        "- bread 120g\n")
        print("\033[1;37;40mPress spacebar to continue...")
        get_char.getch()
        lets_start()
def tuesday_sec_break():
        os.system("cls")
        print(
        "\nTuesday second breakfast"
        "------------------------\n"
        "'Mexican salad'\n"
        "- chicken 200g\n"
        "- pearl barley 50g\n"
        "- red bean 35g\n"
        "- corn 45g\n"
        "- leek 25g\n"
        "- mayonnaise 30g\n"
        "- rapeseed oil 5ml\n")
        print("\033[1;37;40mPress spacebar to continue...")
        get_char.getch()
        lets_start()
def tuesday_lunch():
        os.system("cls")
        print(
        "\nTuesday lunch\n"
        "-------------\n"
        "'Spaghetti'\n"
        "- turkey 250g\n"
        "- pasta 30g\n"
        "- mushrooms 75g\n"
        "- onion 25g\n"
        "- sunflower oil 5ml\n"
        "- tomato sauce 500ml\n"
        "- cheddar 50g\n")
        print("\033[1;37;40mPress spacebar to continue...")
        get_char.getch()
        lets_start()
def tuesday_dinner():
        os.system("cls")
        print(
        "\nTuesday dinner\n"
        "--------------\n"
        "'Salmon with bread and cumcumber'\n"
        "- smoked salmon 60g\n"
        "- bread 120g\n"
        "- cumcumber 50g\n"
        "- butter 20g\n")
        print("\033[1;37;40mPress spacebar to continue...")
        get_char.getch()
        lets_start()
def wednesday_break():
        os.system("cls")
        print(
        "\nWednesday breakfast\n"
        "-------------------\n"
        "'Porridge with fruits'\n"
        "- porridge 60g\n"
        "- natural yogurt 300g\n"
        "- blueberries and raspberries 200g\n"
        "- walnuts 25g\n"
        "- natural honey 25g\n\n")
        print("\033[1;37;40mPress spacebar to continue...")
        get_char.getch()
        lets_start()
def wednesday_sec_break():
        os.system("cls")
        print(
        "\nWednesday second breakfast\n"
        "--------------------------\n"
        "'Mexican salad'\n"
        "- chicken 200g\n"
        "- pearl barley 50g\n"
        "- red bean 35g\n"
        "- corn 45g\n"
        "- leek 25g\n"
        "- mayonnaise 30g\n"
        "- rapeseed oil 5ml\n")
        print("\033[1;37;40mPress spacebar to continue...")
        get_char.getch()
        lets_start()
def wednesday_lunch():
        os.system("cls")
        print(
        "\nWednesday lunch\n"
        "---------------\n"
        "'Mashed potato with burger and vegetables'"
        "- pork/beef 125g\n"
        "- potatoes 160g\n"
        "- grated beetroots 150g\n"
        "- sunflower oil 15ml\n")
        print("\033[1;37;40mPress spacebar to continue...")
        get_char.getch()
        lets_start()
def wednesday_dinner():
        os.system("cls")
        print(
        "\nWednesday dinner\n"
        "----------------\n"
        "'Chicken sandwich'\n"
        "- chicken 200g\n"
        "- cumcumber 50g\n"
        "- tomato 150g\n"
        "- bread 80g\n"
        "- rapeseed oil 5ml\n")
        print("\033[1;37;40mPress spacebar to continue...")
        get_char.getch()
        lets_start()
def thursday_break():
        os.system("cls")
        print(
        "\nThursday breakfast\n"
        "------------------\n"
        "'Natural yoghurt with banana'\n"
        "- natural yoghurt 500ml\n"
        "- bananas 240g\n")
        print("\033[1;37;40mPress spacebar to continue...")
        get_char.getch()
        lets_start()
def thursday_sec_break():
        os.system("cls")
        print(
        "\nThursday second breakfast\n"
        "------------------------\n"
        "'Greek salad with chicken'\n"
        "- chicken 200g\n"
        "- tomato 80g\n"
        "- pepper 140g\n"
        "- cucumber 50g\n"
        "- onion 50g\n"
        "- spinach 50g\n"
        "- sunflower oil 10ml\n"
        "- bread 80g\n")
        print("\033[1;37;40mPress spacebar to continue...")
        get_char.getch()
        lets_start()
def thursday_lunch():
        os.system("cls")
        print(
        "\nThursday lunch\n"
        "--------------"
        "'Mexican stew'\n"
        "- chicken 125g\n"
        "- pearl barley 50g\n"
        "- courgette 200g\n"
        "- passata 100ml\n"
        "- onion 100g\n"
        "- cheddar cheese 100g\n"
        "- rapeseed oil 10ml\n"
        "- red bean 60g\n")
        print("\033[1;37;40mPress spacebar to continue...")
        get_char.getch()
        lets_start()
def thursday_dinner():
        os.system("cls")
        print(
        "\nThursday dinner\n"
        "---------------\n"
        "'Avocado toasts'\n"
        "- avocado 70g\n"
        "- 2 eggs\n"
        "- bread 80g\n")
        print("\033[1;37;40mPress spacebar to continue...")
        get_char.getch()
        lets_start()
def friday_break():
        os.system("cls")
        print(
        "\nFriday breakfast\n"
        "----------------\n"
        "'Porridge with fruits'\n"
        "- porridge 60g\n"
        "- natural yogurt 300g\n"
        "- blueberries and raspberries 200g\n"
        "- walnuts 25g\n"
        "- natural honey 25g\n\n")
        print("\033[1;37;40mPress spacebar to continue...")
        get_char.getch()
        lets_start()
def friday_sec_break():
        os.system("cls")
        print(
        "\nFriday second breakfast\n"
        "------------------------\n"
        "'Eggs stuffed with tuna'\n"
        "- tuna 140g\n"
        "- 3 eggs\n"
        "- natural yoghurt 50ml\n"
        "- chive 15g\n"
        "- bread 60g\n")
        print("\033[1;37;40mPress spacebar to continue...")
        get_char.getch()
        lets_start()
def friday_lunch():
        os.system("cls")
        print(
        "\nFriday lunch\n"
        "------------\n"
        "'Mexican stew'\n"
        "- pearl barley 50g\n"
        "- courgette 300g\n"
        "- passata 100ml\n"
        "- onion 100g\n"
        "- cheddar cheese 100g\n"
        "- rapeseed oil 10ml\n"
        "- red bean 60g\n")
        print("\033[1;37;40mPress spacebar to continue...")
        get_char.getch()
        lets_start()
def friday_dinner():
        os.system("cls")
        print(
        "\nFriday dinner\n"
        "-------------\n"
        "'Banana and chocolate cocktail'\n"
        "- bananas 120g\n"
        "- mango 100g\n"
        "- peanut milk 100ml\n"
        "- natural yoghurt 100ml\n"
        "- walnuts 10g\n"
        "- cocoa 5g\n")
        print("\033[1;37;40mPress spacebar to continue...")
        get_char.getch()
        lets_start()
def saturday_break():
        os.system("cls")
        print(
        "\nSaturday breakfast\n"
        "------------------\n"
        "'Semolina with peach'\n"
        "- natural yoghurt 150ml\n"
        "- semolina  50g\n"
        "- peach 150g\n"
        "- dried cranberries 10g\n"
        "- linseed 10g\n"
        "- pumpkin seeds 10g\n"
        "- pistachio nuts 10g\n"
        "- natural honey 20g\n")
        print("\033[1;37;40mPress spacebar to continue...")
        get_char.getch()
        lets_start()
def saturday_sec_break():
        os.system("cls")
        print(
        "/nSaturday second breakfast\n"
        "-------------------------\n"
        "'Cod salad'\n"
        "- cod 115g\n"
        "- rice 50g\n"
        "- canned corn 145g\n"
        "- peper 150g\n"
        "- natural yoghurt 50ml\n")
        print("\033[1;37;40mPress spacebar to continue...")
        get_char.getch()
        lets_start()
def saturday_lunch():
        os.system("cls")
        print(
        "\nSaturday lunch\n"
        "--------------\n"
        "'Pasta with pesto'\n"
        "- mozarella 125g\n"
        "- pasta 60g\n"
        "- pesto 40g\n"
        "- tomatoes 150g\n")
        print("\033[1;37;40mPress spacebar to continue...")
        get_char.getch()
        lets_start()
def saturday_dinner():
        os.system("cls")
        print(
        "\nSaturday dinner\n"
        "---------------\n"
        "'Fried eggs with kimchi'\n"
        "- 3 eggs\n"
        "- kimchi 50g\n"
        "- bread 100g\n"
        "- spinach 100g\n"
        "- apple cake 50g\n")
        print("\033[1;37;40mPress spacebar to continue...")
        get_char.getch()
        lets_start()
def sunday_break():
        os.system("cls")
        print(
        "\nSunday breakfast\n"
        "----------------\n"
        "'White cheese with vegetables'\n"
        "- white cheese 200g\n"
        "- natural yoghurt 100g\n"
        "- peper 150g\n"
        "- radish 50g\n"
        "- chive 15g\n"
        "- bread 120g\n")
        print("\033[1;37;40mPress spacebar to continue...")
        get_char.getch()
        lets_start()
def sunday_sec_break():
        os.system("cls")
        print(
        "\nSunday second breakfast\n"
        "-----------------------\n"
        "'Cod salad'\n"
        "- cod 115g\n"
        "- rice 50g\n"
        "- canned corn 145g\n"
        "- peper 150g\n"
        "- natural yoghurt 50ml\n")
        print("\033[1;37;40mPress spacebar to continue...")
        get_char.getch()
        lets_start()
def sunday_lunch():
        os.system("cls")
        print(
        "\nSunday lunch\n"
        "------------\n"
        "'Stewed chicken legs with vegetables'\n"
        "- chicken legs 150g\n"
        "- buckwheat 50g\n"
        "- broccoli 150g\n"
        "- rapeseed oil 10ml\n")
        print("\033[1;37;40mPress spacebar to continue...")
        get_char.getch()
        lets_start()
def sunday_dinner():
        os.system("cls")
        print(
        "\nSunday dinner\n"
        "-------------\n"
        "'Scrambled eggs'\n"
        "- 3 eggs\n"
        "- bread 60g\n"
        "- butter 10g\n")
        print("\033[1;37;40mPress spacebar to continue...")
        get_char.getch()
        lets_start()
def goodbye():
        print("Thank you for using the program.")
lets_start()