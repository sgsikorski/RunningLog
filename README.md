# RunningLog
Terminal based running log

Finally decided to upload this.
Project that is from May of 2020 when I finished Fall semester classes and was 
still stuck in lockdown with nothing to do.

Running Log

Scott Sikorski
University of Rochester Undergraduate '23
May 2020
Terminal based running log application

Features include:
Calendar using graphics.py that displays non-interactive run data.
Adding runs that are then stored in a .txt file.
Runs are sorted from oldest to newest.
Finding your longest run by distance.
Editing a run based on its date.

I created this project in about 15 hours of work as a side project because
I was bored during lockdown. I learnt Python during my Spring 2020 semester
at the University of Rochester. As well, this was created between second
semester ending and beginning summer work. I'm also a runner at the 
University of Rochester so I thought that this would be a good idea.
First time dedicating an extended amount of time to create a big project
that hasn't been assigned as school work. Turnt out pretty well and had some 
stumps especially with the sorting method but have been able to get the
methods created in good manner, at least to an undergraduate. 

Thank you for checking this code out and let me know if there are any bugs
or data that isn't calculated or displayed correctly.

How to use
-----------
Using a number based selection in the terminal, select what you would like to see
The calendar will be completely blank if the RunningDatabase.txt file is empty 
If there are runs logged, navigate to which month you would like to see.
The calendar will pop up and show your distance, time, and pace for that day.

To add a run, type '2'.
It will prompt you to enter a date which must be seperated using '/'
then distance (any float works)
Then time which must be seperated using ':', and multiple times for hours.

Type '3' to see the longest run, which also displays the data from that day

Type '4' to edit a run
Enter a date using the '/' seperation, and then enter the new data.
The program will then delete that old date data and add the new data

Type '5' to quit the window

Typing anything else will result in 'Under development' text appearing
The data in the database will then automatically sort after the user quits the program.
This allows for the calendar and other functions to work more smoothly and more quickly. 

Was debating on expanding this more, but I decided that I won't because it is too old and I'm taking classes 
