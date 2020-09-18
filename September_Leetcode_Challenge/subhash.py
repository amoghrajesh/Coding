# check_rain() will tell if there is rain or not
# the check_rain() will return a float value which if > RAIN_THRESHOLD, then it is 
# raining otherwise not

RAIN_THRESHOLD = 0
def check_rain():
    '''write the logic to get value from rain sensor '''
    pass

def get_soil_moisture_level():
    '''write the sensor logic to get this value'''
    pass

def turn_on_relay():
    '''write logic to turn on relay'''
    pass

def turn_off_relay():
    '''write logic to turn off relay'''
    pass

if __name__=="main":
    rain = check_rain()
    if rain < RAIN_THRESHOLD:
        #not raining
        soil = get_soil_moisture_level()
        if soil < 0.3:
            turn_on_relay()
            while soil < 0.9:
                soil = get_soil_moisture_level()
            print("soil level reached 90%")
            turn_off_relay()
        else:
            #break the system
            print("breaking out")
            break
    else:
        #raining
        print("breaking out")
        break
