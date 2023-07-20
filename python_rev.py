import colorama
from colorama import Fore, Back, Style

def create_youtube_video(title, description):
	dic = {"title":title, "description":description, "likes":0, "dislikes":0, "comments": {}, "hashtag":["fun", "nice", "good", "great"]}
	return dic
	
def likes(dictionary):
	if "likes" in dictionary:
		dictionary["likes"]= dictionary["likes"]+1
	return dictionary

def dislikes(dictionary):
	if "dislikes" in dictionary:
		dictionary["dislikes"]=dictionary["dislikes"]+1
	return dictionary

def add_comment(dic, username, comment_text):
	dic["comments"][username] = comment_text
	print(dic)
	return dic

def similarity_to_video(video1, video2):
	counter=0
	for word in video1["hashtag"]:
		if word in video2["hashtag"]:
			counter=counter+1
	return counter*20

def main():
	video1 = {"title":"", "description":"description", "likes":0, "dislikes":0, "comments": {}, "hashtag":["fun", "nice", "good", "great", " "]}
	video2 = {"title":"", "description":"description", "likes":0, "dislikes":0, "comments": {}, "hashtag":["fu", "nice", "good", "great", " fun"]}
	

	#similarity = similarity_to_video(video1, video2)
	print("The similarity between the videos is: " + str(similarity_to_video(video1, video2)) + "%")
	print(Back.RED + Fore.BLUE + "Welcome to Youtube")
	title = input("what is the title you want for the video?")
	description = input("what is the description you want for the video?")
	video = create_youtube_video(title, description)
	print("guide lines: 1=like, 2=dislike, 3=add comment, 4=exit")
	inp=0
	while inp!="4":
		inp=input("what would you like to do?")
		if inp=="1":
			video = likes(video)
			print(video["likes"])
		elif inp=="2":
			video = dislikes(video)
			print(video["dislikes"])
		elif inp=="3":
			username = input("Enter username: ")
			comment_text = "HATE THIS VIDEO!!!!!"
			print(video["comments"])
			video = add_comment(video, username, comment_text)



main()