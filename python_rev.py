import colorama
from colorama import Fore, Back, Style

def create_youtube_video(title, description):
	dic = {"title":title, "description":description, "likes":0, "dislikes":0, "comments": {}}
	return dic
	
def likes(dictionary):
	if "likes" in dictionary:
		dictionary[likes]=	dictionary[likes+1]
	return dictionary

def dislikes(dictionary):
	if "dislikes" in dictionary:
		dictionary[dislikes]=	dictionary[dislikes+1]
	return dictionary

def add_comment(dic, username, comment_text):
	dic["comments"][username] = comment_text
	print(dic)
	return dic

# def add_likes(likes):
# 	for i in range (496):
# 		likes
# 		i=i+1

def main:
	print(Back.RED + Fore.BLUE + "Welcome to Youtube")
	title = input("what is the title you want for the video?")
	description = input("what is the description you want for the video?")
	video = create_youtube_video(title, description)
	print("guide lines: 1=like, 2=dislike, 3=add comment, 4=exit")
	while input!="4":
		in=input("what would you like to do?")
		if in=="1":
			video = likes(video)
		elif in=="2":
			video = dislikes(video)
		elif in=="3":
			username = input("Enter username: ")
			comment_text = "HATE THIS VIDEO!!!!!"
			video = add_comment(video, username, comment_text)