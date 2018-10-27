def balls_collide(argument1, argument2):
    if (argument1[2] < 0) or (argument2[2] < 0):
        raise ValueError
    if (argument1[2] + argument2[2]) ** 2 - ((argument1[0] - argument2[0]) ** 2 + (argument1[1] - argument2[1]) ** 2) > 0.00000001:
        return False	
    else:
        return True
