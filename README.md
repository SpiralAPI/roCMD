# roCMD Documentation and Usage Guide
### What is roCMD?
roCMD is a CLI, or command-based terminal, which allows users to retrieve information of creations throughout the ROBLOX platform. It uses python (.py), which is one of the leading languages in the world. 

### What is Python?
Python is a general-purpose coding language—which means that, unlike HTML, CSS, and JavaScript, it can be used for other types of programming and software development besides web development. That includes back end development, software development, data science and writing system scripts among other things.
###### Source: https://skillcrush.com/blog/what-is-python-used-for/

### Hows it made?
I am using a module known as pyrblx (https://pypi.org/project/pyrblx/) to use ROBLOX Api's. Although the module does not cover all bases of ROBLOX api, it still works fine as is. In future updates, I will be rewriting pyrblx to suit a more diverse set of options in roCMD>

### Planned updates
* More Commands for Information (assets, catalog, search, games, avatar) | NOT YET COMPLETE
* Control Roblox, etc control roles in groups, games, and cover as many API endpoints as possible. | NOT YET COMPLETE
* Make a Discord Bot version of roCMD.

### Usage
I have made this as easy as possible. 

After downloading the rocmd-master.zip, please unzip it to your preferred location. 

Now, to run the program, open the folder and navigate to the folder named 'roCMD'. 

Finally, run 'roCMD_batchRun.bat' and follow the steps from there. If you wish to alter or edit the files, please navigate to the folder named 'src' and edit index.py.

If any issues come up, feel free to report them. 

### Commands
To get a list of commands, you can run 'help' within roCMD, or use the list below.

```
                    COMMANDS >
                                GROUPS >
                                        listAllies <groupid> | Lists all allies of the group.
                                        getName <groupid> | Lists name of the selected group.
                                        groupDescription <groupid> | Returns the groups description.
                                        getOwnerName <groupid> | Returns the username of the group owner.
                                        getOwnerId <groupid> | Returns the id of the group owner.
                                        getMemberCount <groupid> | Returns the number of members of a group.
                                        isPrivate <groupid> | Returns "True" or "False" if the group is open or closed to entry.
                                        getShout <groupid> | Returns the current shout of the group.
                                        groupShoutPoster <groupid> | Returns the username of the user who made the last shout.
                                        thumbnailURL <groupid> | Returns the URL to the thumbnail of the group.
                                        groupURL <groupid> | Returns the URL to the groups homepage.
                                PLAYER >
                                        getUsername <userId> | Returns users username / displayname.
                                        getDescription <userId> | Returns users description.
                                        creationDate <userid> | Returns the creation date of the user.
                                        listBadges <userid> | Lists a users badges that are currently owned.
                                        getURL <userid> | Returns the users direct URL to their profile.
                                        listFriends <userid> | Lists a users friends list.
                                        latestFriend <userid> | Returns the users latest added friend.
                                        oldestFriend <userid> | Returns the users oldest added friend.
                                        friendCount <userid> | Returns the users friend count.
                                        listGroups <userid> | Lists all groups the user is in.
                                        latestGroup <userid> | Returns the latest group joined by the user.
                                        oldestGroup <userid> | Returns the oldest group joined by the user.
                                        groupCount <userid> | Returns the users amount of groups they have joined.
                                        avatarURL <userid> | Returns the URL for the users Avatar picture.
                                        thumbnailURL <userid> | Returns the URL for the users Thumbnail picture.
```




#### Thank you for using roCMD.
