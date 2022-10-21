# Old Rin changelog

This was a very early version of Rin, created as an emergency after the old Sad Machine bot died, to keep the report features working. It wasn't announced publically at all in either the Porter Robinson Discord or the Madeon Discord until v1.0.0. 

Fun fact: most of the functionality on those old Rin versions was contained in only one file! (which was a mess)

(date format is dd/mm/yyyy)

------------------------------------------------------------------------
## v0.3.20-final - 10/09/2021
* added a countdown for second sky
* this is the final version of the bot (before rewritting) due to discord.py being deprecated
## v0.3.19 - 11/07/2021
* removal of the code for the PRD event announcement "game"
* some changes to the dev mode, to separate it from Rin in the PRD and test stuff elsewhere
* actual new stuff for the bot coming Soon:tm:
## v◈.◈.6 - 10/07/2021
* PRD event announcement "game" part 6
## v◈.◈.5 - 09/07/2021
* PRD event announcement "game" part 5
## v◈.◈.4 - 08/07/2021
* PRD event announcement "game" part 4
## v◈.◈.3 - 07/07/2021
* PRD event announcement "game" part 3
## v◈.◈.2 - 06/07/2021
* PRD event announcement "game" part 2
## v◈.◈.1 - 05/07/2021
* PRD event announcement "game" part 1
## v◈.◈.◈ - 04/07/2021
* PRD event announcement "game" teasing
## v0.3.18 - 02/06/2021
* added the 'sky marshall' role to the list of roles that allows you to delete messages when you report them
## v0.3.17 - 29/05/2021
* removed nurture countdown stuff
* reverted rin's rich presence to random songs instead of nurture in order
## v0.3.16 - 21/04/2021
* updated countdown stuff
* the bot will now play nurture in order in the rich presence
## v0.3.15 - 14/04/2021
* updated the report functionnality so that temp moderators can report messages as well
## v0.3.14 - 07/04/2021
* fixed !!nurture's issue (again x2) with counting seconds/days
## v0.3.13 - 07/04/2021
* added !!saytts (for mods)
* added special countdown stuff for nurture's release
* switched the timezone of the countdown from utc to nzst
## v0.3.12 - 22/03/2021
* renamed the !!days_to_nurture command to !!nurture
* fixed !!nurture's issue (again) with counting seconds
## v0.3.11 - 22/03/2021
* fixed !!days_to_nurture's issue with counting days
## v0.3.10 - 21/03/2021
* updated the bot's functionment (related to dev mode and versionning)
* updated !!days_to_nurture and it's functionment  
* updated !!fiftyfifty's functionment (will draw a number from 0 to 999 instead of 1 or 2, 0 to 499 being yes and 500 to 999 being no) 
* added placeholder stuff
## v0.3.9 - 12/03/2021
* added musician by porter robinson to the song library
* added !!fiftyfifty for geoguessr in #live-games
## v0.3.8 - 28/02/2021
* migrated from heroku to google cloud, which removed the 24hrs reboot limitation. i removed it from the bot as well as a result
## v0.3.7 - 13/02/2021
* fixed a glitch with the 'days to nurture' automation in #nurture
* fixed the song length for 'look at the sky' (5m10s instead of 2m32s)
* added placeholder code for when nurture releases
## v0.3.6 - 11/02/2021
* updated libraries, including discord.py to 1.6.0
* a reported message will now be deleted instead of staying up if a mod reacts 🚫 after a regular user did
* added a countdown to be posted in #nurture every day at 12:00am GMT. closer to the release i'll add a function that will allow the bot to send a message for each timezone that'll get nurture.
* added !!days_to_nurture that will tell you how many days are left before nurture releases (in the GMT timezone)
## v0.3.5 - 15/12/2020
* added a very barebone !!roll command that throws a d6 dice
* the bot now shows the version in it's nickname
* !!lastchange has been removed and it's functionality was moved to !!changelog (i felt like both commands were redundant)
## v0.3.4 - 11/12/2020
* the bot will now automatically restart at a certain undisclosed time
* little functional change to !!lastchange (just so that it's easier for me to edit versions lmfao)
## v0.3.3 - 06/12/2020
* added !!lastchange
* added madeon's adventure (deluxe) into the bot's presence
* changed the bot's presence format ('song' by 'artist')
* fixed an issue where the bot would crash if someone reacted to a webhook/deleted user 
* fixed the changelog links oops
* normalized date format to dd/mm/yyyy
## v0.3.2 - 11/11/2020 
* added a version verification (if versions aren't matching, the bot will quit)
* added !!changelog
* full changelog is now in a markdown format
* fixed the issue with the bot crashing if people react in another server
* fixed the issue with edited messages not being able to be reported
## v0.3.1 - 02/11/2020
* fixed the !!info command (everyone used to have created the bot lmao)
## v0.3.0 - 01/11/2020
* added !!say command
* added !!info command
* added !!october18 command
* transferred the version into an .env variable
* the bot will now show when it's in dev mode (as in when it's running locally, rather than running on heroku)

------------------------------------------------------------------------
## v0.2.1 - 01/11/2020 
* converted the !!quit command into a proper bot.command() instead of a on_message() command
* .gitignore update to exclude the python cache
## v0.2.0 - 01/11/2020 
* added more songs into the library
* added a proper crash handler


------------------------------------------------------------------------
## v0.1.2 - 31/10/2020
* added songs into the presence thing
* bugfix with crash issue 
## v0.1.1 - 31/10/2020
* bugfix with role issues
## v0.1.0 - 31/10/2020
* initial release with report function
