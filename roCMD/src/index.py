# @author:SpiralRBX
# Subscribe to me on youtube at https://youtube.com/c/SpiralRBX
# Have a bug? Make a request on the github.

import pyrblx
from time import sleep  # wait() for python lol
from os import system, name  # stuff


def clear():  # stolen from stackoverflow lol
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


#opening questions and stuff
clear()
print("Welcome to roCMD! I am made to help you get information and explore Roblox with a command-based terminal.")
sleep(5)
clear()
# the main part of the thingy

#ignore the thing below, its for an upcoming update

#			ASSETS >
#				assetName <assetid> | Returns the name of the asset.
#				assetDescription <assetid> | Returns the description of the asset.
#				assetCreatorUsername <assetid> | Returns the assets creator username.
#				assetCreatorId <assetid> | Returns the assets creator userid.
#				assetPrice <assetid> | Returns the assets price.
#				isForSale <assetid> | Returns "True" or "False" if the asset is on sale.
#				assetType <assetid> | Returns the type of asset it is.


stopped = False
while not stopped:
	cmd = input("cmd>>>   ")
	if cmd == "help":
		print("""
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
			""")  # list of commands

	# ASSETS (coming soon)

	def assetsplaceholder():
		"""
		if cmd == "assetName":
			try:
				try:
					assetid = int(input("Please enter the assetid: "))
				except ValueError:
					print("Please enter a valid number.")
					continue
				new = pyrblx.Bundles(int(assetid))
				print(str(pyrblx.Bundles.bundle_name(new)))
			except pyrblx.BundleNotFound:
				print("Asset is invalid. Please check the ID and try again.")

		if cmd == "assetCreatorUsername":
			try:
				try:
					assetid = int(input("Please enter the assetid: "))
				except ValueError:
					print("Please enter a valid number.")
					continue
				new = pyrblx.Bundles(int(assetid))
				print(str(pyrblx.Bundles.bundle_creator_name(new)))
			except pyrblx.BundleNotFound:
				print("Asset is invalid. Please check the ID and try again.")
		
		if cmd == "assetCreatorId":
			try:
				try:
					assetid = int(input("Please enter the assetid: "))
				except ValueError:
					print("Please enter a valid number.")
					continue
				new = pyrblx.Bundles(int(assetid))
				print(str(pyrblx.Bundles.bundle_creator_id(new)))
			except pyrblx.BundleNotFound:
				print("Asset is invalid. Please check the ID and try again.")

		if cmd == "assetPrice":
			try:
				try:
					assetid = int(input("Please enter the assetid: "))
				except ValueError:
					print("Please enter a valid number.")
					continue
				new = pyrblx.Bundles(int(assetid))
				print(str(pyrblx.Bundles.price(new)))
			except pyrblx.BundleNotFound:
				print("Asset is invalid. Please check the ID and try again.")

		if cmd == "isForSale":
			try:
				try:
					assetid = int(input("Please enter the assetid: "))
				except ValueError:
					print("Please enter a valid number.")
					continue
				new = pyrblx.Bundles(int(assetid))
				print(str(pyrblx.Bundles.isforsale(new)))
			except pyrblx.BundleNotFound:
				print("Asset is invalid. Please check the ID and try again.")

		if cmd == "assetType":
			try:
				try:
					assetid = int(input("Please enter the assetid: "))
				except ValueError:
					print("Please enter a valid number.")
					continue
				new = pyrblx.Bundles(int(assetid))
				print(str(pyrblx.Bundles.type(new)))
			except pyrblx.BundleNotFound:
				print("Asset is invalid. Please check the ID and try again.")
	"""

	# GROUPS
	if cmd == "listAllies":
		try:
			try:
				groupid = int(input("Please enter the groupid: "))
			except ValueError:
				print("Please enter a valid number.")
				continue
			new = pyrblx.Groups(int(groupid))
			print(str(pyrblx.Groups.group_allies(new)))
		except pyrblx.GroupNotFound:
			print("Group is invalid. Please check the ID and try again.")

	if cmd == "getName":
		try:
			try:
				groupid = int(input("Please enter the groupid: "))
			except ValueError:
				print("Please enter a valid number.")
				continue
			new = pyrblx.Groups(int(groupid))
			print(str(pyrblx.Groups.group_name(new)))
		except pyrblx.GroupNotFound:
			print("Group is invalid. Please check the ID and try again.")

	if cmd == "getOwnerName":
		try:
			try:
				groupid = int(input("Please enter the groupid: "))
			except ValueError:
				print("Please enter a valid number.")
				continue
			new = pyrblx.Groups(int(groupid))
			print(str(pyrblx.Groups.group_owner_name(new)))
		except pyrblx.GroupNotFound:
			print("Group is invalid. Please check the ID and try again.")

	if cmd == "getOwnerId":
		try:
			try:
				groupid = int(input("Please enter the groupid: "))
			except ValueError:
				print("Please enter a valid number.")
				continue
			new = pyrblx.Groups(int(groupid))
			print(str(pyrblx.Groups.group_owner_id(new)))
		except pyrblx.GroupNotFound:
			print("Group is invalid. Please check the ID and try again.")

	if cmd == "getMemberCount":
		try:
			try:
				groupid = int(input("Please enter the groupid: "))
			except ValueError:
				print("Please enter a valid number.")
				continue
			new = pyrblx.Groups(int(groupid))
			print(str(pyrblx.Groups.group_member_count(new)))
		except pyrblx.GroupNotFound:
			print("Group is invalid. Please check the ID and try again.")

	if cmd == "isPrivate":
		try:
			try:
				groupid = int(input("Please enter the groupid: "))
			except ValueError:
				print("Please enter a valid number.")
				continue
			new = pyrblx.Groups(int(groupid))
			print(str(pyrblx.Groups.is_private(new)))
		except pyrblx.GroupNotFound:
			print("Group is invalid. Please check the ID and try again.")

	if cmd == "getShout":
		try:
			try:
				groupid = int(input("Please enter the groupid: "))
			except ValueError:
				print("Please enter a valid number.")
				continue
			new = pyrblx.Groups(int(groupid))
			print(str(pyrblx.Groups.group_shout(new)))
		except pyrblx.GroupNotFound:
			print("Group is invalid. Please check the ID and try again.")

	if cmd == "getShoutPoster":
		try:
			try:
				groupid = int(input("Please enter the groupid: "))
			except ValueError:
				print("Please enter a valid number.")
				continue
			new = pyrblx.Groups(int(groupid))
			print(str(pyrblx.Groups.group_shout_poster_name(new)))
		except pyrblx.GroupNotFound:
			print("Group is invalid. Please check the ID and try again.")

	if cmd == "thumbnailURL":
		try:
			try:
				groupid = int(input("Please enter the groupid: "))
			except ValueError:
				print("Please enter a valid number.")
				continue
			new = pyrblx.Groups(int(groupid))
			print(str(pyrblx.Groups.group_thumbnail(new)))
		except pyrblx.GroupNotFound:
			print("Group is invalid. Please check the ID and try again.")

	if cmd == "groupURL":
		try:
			try:
				groupid = int(input("Please enter the groupid: "))
			except ValueError:
				print("Please enter a valid number.")
				continue
			new = pyrblx.Groups(int(groupid))
			print(str(pyrblx.Groups.group_url(new)))
		except pyrblx.GroupNotFound:
			print("Group is invalid. Please check the ID and try again.")

	if cmd == "groupDescription":
		try:
			try:
				groupid = int(input("Please enter the groupid: "))
			except ValueError:
				print("Please enter a valid number.")
				continue
			new = pyrblx.Groups(int(groupid))
			print(str(pyrblx.Groups.group_description(new)))
		except pyrblx.GroupNotFound:
			print("Group is invalid. Please check the ID and try again.")

	# PLAYER
	if cmd == "getUsername":
		try:
			try:
				userid = int(input("Please enter the userid: "))
			except ValueError:
				print("Please enter a valid number.")
				continue
			print(str(pyrblx.Players.user_name(pyrblx.Players.get_by_id(int(userid)))))
		except pyrblx.PlayerNotFound:
			print("Player is invalid. Please check the ID and try again.")

	if cmd == "getDescription":
		try:
			try:
				userid = int(input("Please enter the userid: "))
			except ValueError:
				print("Please enter a valid number.")
				continue
			print(str(pyrblx.Players.description(pyrblx.Players.get_by_id(int(userid)))))
		except pyrblx.PlayerNotFound:
			print("Player is invalid. Please check the ID and try again.")

	if cmd == "creationDate":
		try:
			try:
				userid = int(input("Please enter the userid: "))
			except ValueError:
				print("Please enter a valid number.")
				continue
			print(str(pyrblx.Players.created_at(pyrblx.Players.get_by_id(int(userid)))))
		except pyrblx.PlayerNotFound:
			print("Player is invalid. Please check the ID and try again.")

	if cmd == "listBadges":
		try:
			try:
				userid = int(input("Please enter the userid: "))
			except ValueError:
				print("Please enter a valid number.")
				continue
			print(str(pyrblx.Players.roblox_badges(pyrblx.Players.get_by_id(int(userid)))))
		except pyrblx.PlayerNotFound:
			print("Player is invalid. Please check the ID and try again.")

	if cmd == "getURL":
		try:
			try:
				userid = int(input("Please enter the userid: "))
			except ValueError:
				print("Please enter a valid number.")
				continue
			print(str(pyrblx.Players.direct_url(pyrblx.Players.get_by_id(int(userid)))))
		except pyrblx.PlayerNotFound:
			print("Player is invalid. Please check the ID and try again.")

	if cmd == "listFriends":
		try:
			try:
				userid = int(input("Please enter the userid: "))
			except ValueError:
				print("Please enter a valid number.")
				continue
			print(str(pyrblx.Players.friends(pyrblx.Players.get_by_id(int(userid)))))
		except pyrblx.PlayerNotFound:
			print("Player is invalid. Please check the ID and try again.")

	if cmd == "latestFriend":
		try:
			try:
				userid = int(input("Please enter the userid: "))
			except ValueError:
				print("Please enter a valid number.")
				continue
			print(str(pyrblx.Players.latest_friend(pyrblx.Players.get_by_id(int(userid)))))
		except pyrblx.PlayerNotFound:
			print("Player is invalid. Please check the ID and try again.")

	if cmd == "oldestFriend":
		try:
			try:
				userid = int(input("Please enter the userid: "))
			except ValueError:
				print("Please enter a valid number.")
				continue
			print(str(pyrblx.Players.oldest_friend(pyrblx.Players.get_by_id(int(userid)))))
		except pyrblx.PlayerNotFound:
			print("Player is invalid. Please check the ID and try again.")

	if cmd == "friendCount":
		try:
			try:
				userid = int(input("Please enter the userid: "))
			except ValueError:
				print("Please enter a valid number.")
				continue
			print(str(pyrblx.Players.friends_count(pyrblx.Players.get_by_id(int(userid)))))
		except pyrblx.PlayerNotFound:
			print("Player is invalid. Please check the ID and try again.")

	if cmd == "listGroups":
		try:
			try:
				userid = int(input("Please enter the userid: "))
			except ValueError:
				print("Please enter a valid number.")
				continue
			print(str(pyrblx.Players.groups(pyrblx.Players.get_by_id(int(userid)))))
		except pyrblx.PlayerNotFound:
			print("Player is invalid. Please check the ID and try again.")

	if cmd == "latestGroup":
		try:
			try:
				userid = int(input("Please enter the userid: "))
			except ValueError:
				print("Please enter a valid number.")
				continue
			print(str(pyrblx.Players.latest_group(pyrblx.Players.get_by_id(int(userid)))))
		except pyrblx.PlayerNotFound:
			print("Player is invalid. Please check the ID and try again.")

	if cmd == "oldestGroup":
		try:
			try:
				userid = int(input("Please enter the userid: "))
			except ValueError:
				print("Please enter a valid number.")
				continue
			print(str(pyrblx.Players.oldest_group(pyrblx.Players.get_by_id(int(userid)))))
		except pyrblx.PlayerNotFound:
			print("Player is invalid. Please check the ID and try again.")

	if cmd == "groupCount":
		try:
			try:
				userid = int(input("Please enter the userid: "))
			except ValueError:
				print("Please enter a valid number.")
				continue
			print(str(pyrblx.Players.groups_count(pyrblx.Players.get_by_id(int(userid)))))
		except pyrblx.PlayerNotFound:
			print("Player is invalid. Please check the ID and try again.")

	if cmd == "avatarURL":
		try:
			try:
				userid = int(input("Please enter the userid: "))
			except ValueError:
				print("Please enter a valid number.")
				continue
			print(str(pyrblx.Players.avatar(pyrblx.Players.get_by_id(int(userid)))))
		except pyrblx.PlayerNotFound:
			print("Player is invalid. Please check the ID and try again.")

	if cmd == "thumbnailURL":
		try:
			try:
				userid = int(input("Please enter the userid: "))
			except ValueError:
				print("Please enter a valid number.")
				continue
			print(str(pyrblx.Players.thumbnail(pyrblx.Players.get_by_id(int(userid)))))
		except pyrblx.PlayerNotFound:
			print("Player is invalid. Please check the ID and try again.")

	if cmd == "quit":
		stopped = True
