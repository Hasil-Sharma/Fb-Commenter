token = ''
base_url = 'https://graph.facebook.com/v2.1/'
parameters = {'access_token' : token}
import requests
import time

def likePost(id):
	requests.post(base_url + id + "/likes",params = parameters)
	print id

def commentonPost(id,msg):
	print msg
	requests.post(base_url + id + "/comments", params = {'access_token': token, 'message' : msg})

def main():
	count = 0
	flag = True
	temp = "me/feed?since=" + str(int(time.time()) - 24*3600) 
	response = requests.get(base_url + temp,params = parameters)
	while flag:
		json_data = response.json()
		posts = json_data["data"]
		paging = json_data["paging"]

		for post in posts:
				count += 1
				name = post["from"]["name"]
				sender_id = post["from"]["id"]
				post_id = post["id"]
				if sender_id == "689754367729816":
					flag = False
					break
				comment = "Hi, " + name + " :D, Thanks for wishing me. Your wishes made my day."
				likePost(post_id)
				commentonPost(post_id,comment)
		if flag:
			response = requests.get(paging["next"])
	print count


if __name__ == '__main__':
	main()
