/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 *//*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package acsl.pkg2014.pkg15.round.pkg1;

import java.util.Scanner;
/**
 *
 * @author Ben
 */
public class ACSL2014_15Round1 
{
    private static final int[] cities = {450, 140, 125, 365, 250, 160, 380, 235, 320};
    private static final String[] helper = {"A", "B", "C", "D", "E", "F", "G", "H", "J", "K"};
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) 
    {
        Scanner s = new Scanner(System.in);
        System.out.println("Please enter your input in the following format: "
                + "\n -City1 name (String)"
                + "\n -City2 name (String)"
                + "\n -Car1 start time in hours (int)"
                + "\n -Previous entered start time is AM or PM (String)"
                + "\n -Car2 start time in hours (int)"
                + "\n -Previous entered start time is AM or PM (String)"
                + "\n -Car1 speed (int)"
                + "\n -Car2 speed (int)"
                
                + "\nPress enter after each input to submit it. Exceptions will be thrown for incorrect formats:\n");
        System.out.println(calculateTime(s.next(), s.next(), s.nextInt(), s.next(), s.nextInt(), s.next(), s.nextInt(), s.nextInt()));
        
    }
    public static String calculateTime(String point1, String point2, int time1, String amPm1, int time2, String amPm2, double mph1, double mph2)
    {
        final int MINUTES_60 = 60;
        final int HOURS_24 = 24;
        int length1 = -1;
        int length2 = -1;
        double distance = 0;
        int headStartDifference = 0;
        int headStart = 0;
        double hours = 0;
        double minutes = 0;
        double minutes2 = 0;
        double minutes3 = 0;
        
        //Finds the distance between cities along with some exceptions and errors.
        for (int x = 0; x < helper.length; x++)
        {
            if (point1.equalsIgnoreCase(helper[x]))
            {
                length1 = x;
            }
            if (point2.equalsIgnoreCase(helper[x]))
            {
                length2 = x;
            }
        }
        if (length1 == -1 || length2 == -1)
            return "Error, you entered a letter that is not one of the available cities.";
        else if (length1 == length2)
        {
            length1 = 0;
            length2 = 0;
            return ("Time taken: 0:00");
        }
        else if (length1 > length2)
        {
            for (int x = length2; x < length1; x++)
            {
                distance += cities[x];
            }
        }
        else
        {
            for (int x = length1; x < length2; x++)
            {
                distance += cities[x];
            }
        }
        //Finds the time difference between the starting time of the two cars 
            //as well as updates the distance needed to travel after the car to leave first drives.
        if ((!amPm1.equalsIgnoreCase("AM") && !amPm1.equalsIgnoreCase("PM")) ||
                (!amPm2.equalsIgnoreCase("AM") && !amPm2.equalsIgnoreCase("PM")))
        {
            return "Error, you have entered an input other than \"AM\" or \"PM\" for one or more of the inputs that requires it.";
        }
        if (amPm1.equalsIgnoreCase("PM"))
        {
            if (time1 != 12)
                time1 += 12; 
        }
        if (amPm2.equalsIgnoreCase("PM"))
        {
            if (time2 != 12)
                time2 += 12;
        }
        if (time1 > time2)
        {
            headStartDifference = time1 - time2;
            if (HOURS_24 - headStartDifference < headStartDifference)
            {
                headStart = HOURS_24 - headStartDifference;
                distance -= mph1 * headStart;
            }
            else
            {
                headStart = headStartDifference;
                distance -= mph2 * headStart;
                headStart = 0;
            }
            
            
        }
        else if (time1 < time2)
        {
            headStartDifference = time2 - time1;
            if (HOURS_24 - headStartDifference < headStartDifference)
                headStart = HOURS_24 - headStartDifference;
            else
                headStart = headStartDifference;
            distance -= mph1 * headStart;
        }
        //calculates the total time of the trip as well as rounds the minutes.
        hours = headStart + Math.floor(distance / (mph1 + mph2));
        minutes = Math.round(((distance / (mph1 + mph2)) * MINUTES_60) % 60);
        String sMinutes = "" + minutes;
//        if (sMinutes.length() > 1)
//        {
//            for (int x = sMinutes.length(); x > 3; x--)
//            {
//                minutes /= 10;
//            }
//            if (minutes % 10 > 4)
//            {
//                minutes += 10;
//                minutes /= 10;
//            }
//            else
//                minutes /= 10;
//        }
        //prints the result.
        String sHours = "" + hours;
        sHours = sHours.substring(0, sHours.length() - 2);
        String s2Minutes = "" + minutes;
        s2Minutes = s2Minutes.substring(0, s2Minutes.length() - 2);
        if (minutes == 0)
            return ("Time taken: " + sHours + ":00");
        else if (minutes / 10.0 < 1)
            return ("Time taken: " + sHours + ":0" + s2Minutes);
        else
            return("Time taken: " + sHours + ":" + s2Minutes);
    }
    
}
