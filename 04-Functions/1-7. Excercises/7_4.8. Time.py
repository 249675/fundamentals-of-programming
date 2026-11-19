#efine a function time_string(hours, minutes, time_format) that, given the number of hours (0..23) and the number of minutes (0..59), returns a string specifying the time in the given format ('24' for 24-hour time and '12' for 12-hour time).

#Then write a program that tests whether the function works correctly.

#time_string(15, 38, '24') returns '15:38'
#time_string(8, 3, '24') returns '08:03'
#time_string(0, 5 '24') returns '00:05'
#time_string(11, 15, '12') returns '11:15am'
#time_string(0, 7, '12') returns '12:07am'
#time_string(7, 30, '12') returns '7:30am'
#time_string(12, 46, '12') returns '12:46pm'
#time_string(13, 10, '12') returns '1:10pm'
#time_string(19, 02, '12') returns '7:02pm'
#Hint: Use f-strings formatting. Search the Internet for 'Format numbers using f-strings'.

def time_string(hours,minutes,time_format):
    if time_format == "24":
        return f'{hours:02d}:{minutes:02d}' # Zapisujemy godzinę i minuty na dwie cyfry, np. 08:05.
    elif time_format == "12":
        if hours <12: # Dla godzin od 0 do 11 wybieramy oznaczenie „am”.
            suffix = "am"
        elif hours >= 12:  # Dla godzin od 12 do 23 wybieramy oznaczenie „pm”.
            suffix = "pm"
        if hours > 12: # Dla godzin od 13 do 23 odejmujemy 12, np. 15 zmieniamy na 3.
            hours -= 12
        elif hours == 0: # Północ zapisujemy jako 12 w formacie 12-godzinnym.
            hours = 12
        return f'{hours}:{minutes:02d}{suffix}'

print (time_string(15, 38, '24'))
print (time_string(8, 3, '24')) 
print (time_string(0, 5, '24')) 
print (time_string(11, 15, '12')) 
print (time_string(0, 7, '12')) 
print (time_string(7, 30, '12')) 
print(time_string(12, 46, '12')) 
print (time_string(13, 10, '12')) 
print(time_string(19, 2, '12'))
