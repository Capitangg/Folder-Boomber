from rand_string.rand_string import RandString
import os

# for i in range (10) :
 #   os.mkdir(RandString ("uppercase",6))

while true : 
    try:

    os.mkdir(RandString ("uppercase",6))
    except FileExistsError : 
        pass



    #CAPIGG