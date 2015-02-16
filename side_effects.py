def side_effect_test(value):
    # Do something to modify the value
    #value[1] = "orange"
    #value ='bob'
    value = 7
    print "Inside the function, the value becomes {}".format(value)

if __name__ == "__main__":
    # Create the value
    #value = ["red", "green", "blue"]
    #value = 'Trevor'
    value = 10

    print "Outside the function, the value starts as {}".format(value)

    side_effect_test(value)

    print "Outside the function, the value is now {}".format(value)
    
    # mutable objects demonstrate the side effect.   A list is changed in place.