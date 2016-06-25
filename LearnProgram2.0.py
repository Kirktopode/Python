ab = "y"
while ab == "y":
        x = input("Give me a number. ")
        y = input("Give me another number. ")
        xysum = x + y
        xyproduct = x * y
        print "Your sum is " + str(xysum) + " and your product is " + str(xyproduct) + ". You're welcome."
        u = 0
        while u == 0:
                ab = raw_input("Do you want another sum and product? y/n ")
                if ab == "n":
                        u = 1
                        print "Goodbye."
                        break
                if ab == "y":
                        print "Alright, here we go:"
                        u = 1        
                else:
                        print "I don't understand that. Let's try again."
                        
