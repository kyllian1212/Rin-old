------------------------------------------------------------------------
## v0.1.0 - 31/10/2020
* initial release with report function
## v0.1.1 - 31/10/2020
* bugfix with role issues
## v0.1.2 - 31/10/2020
* added songs into the presence thing
* bugfix with crash issue 

------------------------------------------------------------------------
## v0.2.0 - 01/11/2020 
* added more songs into the library
* added a proper crash handler
## v0.2.1 - 01/11/2020 
* converted the !!quit command into a proper bot.command() instead of a on_message() command
* .gitignore update to exclude the python cache

------------------------------------------------------------------------
## v0.3.0 - 01/11/2020
* added !!say command
* added !!info command
* added !!october18 command
* transferred the version into an .env variable
* the bot will now show when it's in dev mode (as in when it's running locally, rather than running on heroku)
## v0.3.1 - 02/11/2020
* fixed the !!info command (everyone used to have created the bot lmao)
## v0.3.2 - 11/11/2020 
* added a version verification (if versions aren't matching, the bot will quit)
* added !!changelog
* full changelog is now in a markdown format
* fixed the issue with the bot crashing if people react in another server
* fixed the issue with edited messages not being able to be reported
## v0.3.3 - 06/12/2020
* added !!lastchange
* added madeon's adventure (deluxe) into the bot's presence
* changed the bot's presence format ('song' by 'artist')
* fixed an issue where the bot would crash if someone reacted to a webhook/deleted user 
* fixed the changelog links oops
* normalized date format to dd/mm/yyyy
## v0.3.4 - 11/12/2020
* the bot will now automatically restart at a certain undisclosed time
* little functional change to !!lastchange (just so that it's easier for me to edit versions lmfao)
## v0.3.5 - 15/12/2020
* added a very barebone !!roll command that throws a d6 dice
* the bot now shows the version in it's nickname
* !!lastchange has been removed and it's functionality was moved to !!changelog (i felt like both commands were redundant)
## v0.3.6 - 11/02/2021
* updated libraries, including discord.py to 1.6.0
* a reported message will now be deleted instead of staying up if a mod reacts 🚫 after a regular user did
* added a countdown to be posted in #nurture every day at 12:00am GMT. closer to the release i'll add a function that will allow the bot to send a message for each timezone that'll get nurture.
* added !!days_to_nurture that will tell you how many days are left before nurture releases (in the GMT timezone)


