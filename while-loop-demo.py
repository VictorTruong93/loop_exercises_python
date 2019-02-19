
# Prompt user over and over again until they say "bye"
bye_count=0

# if day_number == 0:
while bye_count < 3:
# while True:
# if False:
    # body goes here
        # run while condition is true (below) as part of the while
        should_run = True

        while should_run:
            user_input = input("What? ")
            print("%s" % (user_input,))

            # must eventually change the condition to false(Below)
            if user_input == "bye":
                should_run = False
            
            # re-assigning bye_count using its previous value (valid as long as variable is defined initially)
                bye_count = bye_count + 1
                print(bye_count)