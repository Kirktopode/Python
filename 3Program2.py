grade = raw_input("Gimme a grade between 0.0 and 1.0: ")
try:
    g = float(grade)
    if g > 1.0:
        print "Yeah, you could never have gotten more than 100%. Nice try, cheater."
    elif g >= 0.9:
        print "An A. Whoopdeedoo, go slap it on the fridge at home so mommy and daddy can be proud."
    elif g >= 0.8:
        print "You got a B! It's like the new-age C."
    elif g >= 0.7:
        print "You got a C? Well, I guess we need more factory workers."
    elif g >= 0.6:
        print "D stands for unintelligent. Go ahead and challenge me. Nobody will take your side."
    elif g < 0.6 and g >= .0:
        print "F? It's okay, I already called the police. We all know you're only going to end up as a hooker or a thief."
    else:
        print "You got a negative score? I would make fun of you, but I'm just so impressed!"
except:
    print "That's not what I asked for."
