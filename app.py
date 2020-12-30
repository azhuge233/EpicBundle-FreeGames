import sys
from MyClass.LOG import *
from MyClass.GETSOUP import *
from MyClass.json_op import *
from MyClass.PUSH import *

'''Configs'''
TOKEN = ""  # Bot token
CHAT_ID = ""  # Admin ID

'''Static Variables'''
URL = "https://www.epicbundle.com/category/article/for-free/"
PATH = "./records.json"
WORDLIST = ["humble choice bundle",
			"follow us on facebook",
			"more games for free here",
			"\"limitless $10 epic coupons\"",
			"add your comment."]

'''Global Variables'''
logger.name = "EpicBundle-FreeGames"


def send_notification(msg_list):  # send messages to Telegram Bot
	if len(msg_list) != 0:
		try:
			for each in msg_list:
				Push().tg_bot(msg=each, chat_id=CHAT_ID, token=TOKEN, htmlMode=True)
				time.sleep(1)
		except Exception as e:
			logger.error("Send message error!")
			sys.exit(e)


def record(path, data):  # write data to json file
	if len(data) != 0:
		write_json(path=path, data=data)


def try_get_link(url): # try to get the free game link
	results = []
	
	soup = get_url_single(url)
	links = soup.select("div .entry-content a")
	
	for each in links:
		if (each.text.lower() not in WORDLIST):
			link = each.get('href').split("?")[0] # delete ref
			
			if "#disqus_thread" in link: # skip comment button link
				continue
				
			logger.info("Get possible link: " + link)
			results.append(link)
			
	return results


def process(previous, soup):
	records = list([])
	notifications = list([])
	
	articles = soup.select("div .post-column article header h2 a")
	
	for each in articles:
		
		'''get article's title and url'''
		link = each.get('href')
		if each.string is not None:
			title = each.string
		else:
			title = each.text
			
		logger.info("Found new info: " + title)
		
		'''add article to the records list'''
		temp = dict({})
		temp["title"] = title
		temp["url"] = link
		records.append(temp)
		
		'''determine if push or not'''
		is_push = True
		for each in previous:
			if each["title"] == title and each["url"] == link:
				is_push = False
				
		'''generate push messages'''
		if is_push:
			logger.info("Add " + title + " to push list")
			
			possible_links = try_get_link(url=link)
			
			tmp = "<b>EpicBundle 信息</b>\n\n"
			tmp += "<i>" + title + "</i>\n"
			tmp += "文章链接: " + link + "\n\n"
			tmp += "可能的领取链接:\n"
			
			for each in possible_links:
				tmp += each + "\n"
			
			notifications.append(tmp)
			
	'''do push'''
	if len(notifications) == 0:
		logger.info("No new messages")
	else:
		logger.info("Sending notifications")
		send_notification(notifications)
		
	'''write records'''
	if len(records) == 0:
		logger.info("No records to be written")
	else:
		logger.info("Writing records")
		record(PATH, records)
		
		

def main():
	logger.warning("------------------- Start job -------------------")
	
	logger.warning("Loading previous records")
	records = load_json(path=PATH)
	logger.warning("Done")
	
	logger.warning("Getting page source")
	soup = get_url_single(url=URL)
	
	logger.warning("Start processing")
	process(previous=records, soup=soup)
	logger.warning("Done")
	
	logger.info("\n\n")


if __name__ == "__main__":
	main()
