'''
Created on Dec 1, 2014

@author: Ben
'''
from time import sleep


class clock2():
    hour = 12
    minute = 0
    amPm = True #True = am, False = pm

    aHour = 12
    aMinute = 1
    aAmPm = True #True = am, False = pm
    onOff = True #True = on, False = off
    active = True

    ''' Turns the alarm on/off as well as activates the alarm sounds.'''
    def  __toggleAlarm(self, pOnOff):

        #use to stop music after alarm __activates as well as when they press
            #the on/off button in GUI interface.

        #use enrique's method to play a playlist here.

        onOff = pOnOff
        if (onOff):
            print ("WAKE UP!")
        else:
            print ("Off")

    '''Use to activate the alarm.'''
    def  __activateAlarm(self):

        self.__toggleAlarm(True)

    '''Use to de-activate the alarm.'''
    def __deactivateAlarm(self):
        
        self.__toggleAlarm(False)

    '''Use this to turn off the alarm off all together.'''
    def alarmOff(self):

        self.__deactivateAlarm()

    '''Used by the runClock(), occurs every minute to change the time.'''
    def  __modTime(self):

        self.minute += 1
        if (self.minute == 60):

            if (self.hour == 11 and not self.amPm):

                self.hour = 12
                self.amPm = not self.amPm

            elif (self.hour == 11 and self.amPm):

                self.hour = 12
                self.amPm = not self.amPm

            elif (self.hour == 12):

                self.hour = 1

            else:
                self.hour += 1
            self.minute = 0

        if (self.hour == self.aHour and self.minute == self.aMinute and self.aAmPm == self.amPm):
            self.__activateAlarm()
        print ("" + self.__str__())

    '''Starts the clock.'''
    def  runClock(self):

        print("" + self.__str__())
        while(self.active):
            sleep(60)
            self.__modTime()

    '''Sets the time for the clock. Enter in the format: hr, min, am(true)/pm(false).'''
    def  setTime(self, pHour,  pMinute,  pAmPm):

        self.hour = pHour
        self.minute = pMinute
        self.amPm = pAmPm


    '''Sets the time for the alarm to __activate. Enter in the format: hr, min, am(true)/pm(false).'''
    def  setAlarm(self, pHour,  pMinute,  pAmPm):

        self.aHour = pHour
        self.aMinute = pMinute
        self.aAmPm = pAmPm

    '''Gets the clock' current hour'''
    def __getHr(self):

        return self.hour

    '''Gets the clock' current minute.'''
    def  __getMin(self):

        if (self.minute < 10):
            return ("0" + str(self.minute))
        return ("" + str(self.minute))

    '''Gets whether the clock is currently am or pm.'''
    def  __getAmPm(self):

        if (self.amPm):
            return ("am")
        return ("pm")


    def  __str__(self):

        return ("" + str(self.__getHr()) + " : " + str(self.__getMin()) + " " + str(self.__getAmPm()))

    '''Gets the alarm hour.'''
    def __getaHr(self):

        return self.aHour

    '''Gets the alarm minute.'''
    def  __getaMin(self):

        if (self.aMinute < 10):
            return ("0" + str(self.aMinute))
        return ("" + str(self.aMinute))

    '''Gets whether the alarm is am or pm.'''
    def  __getaAmPm(self):

        if (self.aAmPm):
            return ("am")
        return ("pm")

    def  __getAlarm(self):

        return ("" + str(self.__getaHr()) + " : " + str(self.__getaMin()) + " " + str(self.__getaAmPm()))

    def snooze(self):

        self.__deactivateAlarm()
        self.setAlarm(self.__getaHr(), self.__getaMin() + 5, self.__getaAmPm())

#for testing
#Clock2 = clock2()
#Clock2.runClock()
