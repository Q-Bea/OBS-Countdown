# OBS-Countdown
Take a non-dated timestamp and countdown to it. Save the time to a txt file so it can be read by OBS.

This was a small project developed for the 2020 Calgary Fringe, which was performed online as a result of the Covid-19 Shutdown. 
It is provided AS IS with no guarantee on functionality

# Getting Started

## Configuring the target time
Open the Countdown.cfg file. 
On the first line, put the integer of an hour (in 24h format)
On the second line, put the integer of a minute
On the third line, put the integer of a second

## Running the application
Run the included Countdown.bat file, which will run the python script located in the same directory. 
When the target time is reached, the python script will automatically exit it's runtime

## Reading the output
The included Countdown.txt file will be updated twice a second with the time remaining before the target time is reached. 
Tell OBS or any other streaming service the can read live from files to listen to this file and you're good to go

# Known Bugs
- Attempting to use a target time before the current time will not work and will immediately close the application
