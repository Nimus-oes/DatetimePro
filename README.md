# DatetimePro
This is a Python datetime library project.

## Features
1. **D-Day**: calculates remaining days until the target date
2. **Days Elapsed between Two Dates**: calculates the elpased days between two date points
3. **Matching Date**: finds a date based on the elapsed days from a base date
4. **Day of the Week**: finds a weekday of the provided date
5. **Age**: calculates an age using the birth date   
&nbsp;
## Workflow   

### D-Day
> Enter target date > Subtract current date from target date > Get d-day value
1. Receive a target date input from the user
2. Create an aware datetime object using the target date
3. Create another aware datetime object using the current date
4. Convert both target and current date objects into naive ones for simpler day calculation
5. Subtract the naive current date object from the naive target date object
6. Get days value from the returned timedelta object
7. Return the d-day value  
&nbsp;
### Days Elapsed between Two Dates
> Enter two dates > Subtract one date from another > Get elapsed days with absolute value
1. Receive two dates input from the user
2. Create two aware datetime objects using the provided dates
3. Convert both dates into naive objects for simpler day calculation
4. Subtract one date from another
5. Get days value from the returned timedelta object
6. Return the absolute value of the elapsed days  
&nbsp;
### Matching Date
> Enter elapsed days, a base date, and calculation direction (forward/backward) > Subtract or add the days from/to the base date depending on the direction > Get a matching date value
1. Receive elapsed days, a base date, and calculation direction (forward/backward) input from the user
2. Convert the elapsed days input to integer value
3. Create a timedelta object using the elapsed days value
4. Create an aware datetime object using the base date
5. If forward, add the timedelta object to the base date. If backward, subtract it. 
6. Convert the returned datetime object to naive for simpler date format
7. Return the matching date value  
&nbsp;
### Day of the Week
> Enter a target date > Get a weekday value of the date
1. Receive a target date input from the user
2. Create an aware datetime object using the target date
3. Create a list of weekday values from Monday to Sunday
4. Get a weekday value from the target date object with weekday() function
5. Index a list with the returned weekday value
6. Return a weekday value in a human readable format  
&nbsp;
### Age
> Enter a birth date > Subtract birth date from the current date > Get an age value
1. Receive a birth date input from the user
2. Create an aware datetime object using the birth date
3. Create another aware datetime object using a current date
4. Subtract the birth date year from the current year to get a tentative age value.
5. If the month and day value of the birth date is greater than the today’s (meaning the birthday hasn’t happened this year yet), subtract 1 from the age value.
6. Return the age value