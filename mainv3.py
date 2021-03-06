from main import *

def startMenu():
  mainCategories = ['https://indianexpress.com/section/india/page/','https://indianexpress.com/section/sports/page/',
  'https://indianexpress.com/section/entertainment/page/','https://indianexpress.com/section/technology/page/']


  statesCategories = ['https://indianexpress.com/section/cities/delhi/page/','https://indianexpress.com/section/cities/mumbai/page/','https://indianexpress.com/section/cities/chennai/page/','https://indianexpress.com/section/cities/hyderabad/page/','https://indianexpress.com/section/cities/bangalore/page/']

  print('\nHello! Welcome to the News Reader and Analysis App!\nSelect from the following Categories.\n 1. National News. \n 2. State News. \n 3. Sports News \n 4. Entertainment News. \n 5. Technology News\n')

  checkCategory = input()

  if checkCategory == '1':
    mainUrl = mainCategories[0]
  elif checkCategory == '2':
    print('\nSelect which District to view:\n 1. Delhi. \n 2. Maharashtra.\n 3. Tamil Nadu.\n 4. Telangana.\n 5. Karnataka.\n')

    selectDistrict = input()

    if selectDistrict == '1':
      mainUrl = statesCategories[0]
    elif selectDistrict == '2':
      mainUrl = statesCategories[1]
    elif selectDistrict == '3':
      mainUrl = statesCategories[2]
    elif selectDistrict == '4':
      mainUrl = statesCategories[3]
    elif selectDistrict == '5':
      mainUrl = statesCategories[4]
    else:
      print("!!! You have entered wrong choice, Please try with a valid one !!!")
  elif checkCategory == '3':
    mainUrl = mainCategories[1]
  elif checkCategory == '4':
    mainUrl = mainCategories[2]
  elif checkCategory == '5':
    mainUrl = mainCategories[3]
  else:
    print("!!! You have entered wrong choice, Please try with a valid one !!!")

  return mainUrl

if __name__=='__main__':
	lists=[]
	mainUrl = startMenu()
	print("\n HELLO!!! What do you wanna do know? : \n 1. See News \n 2. See Sentiment Value for News \n 3. See overall Sentiment for now. \n")
	check = input("Enter the number: ")
	sentValue=[]
	for x in range(1,3):
		newsPaper={}
		url = urlMaker(mainUrl, x)
		soup = soupee(url)
		titles, links = parser(soup)

		if check=='1':
			seeNews(titles,links)
		elif check=='2':
			sentimentAnalysis(newsPaper, titles, links)
		else:
			avgSentVal = avgSentiment(newsPaper, titles, links)
			sentValue.append(avgSentVal)
	if check== '3':
		avgSentiment = find_Sentiment(sum(sentValue))
		print("Average Sentiment now is : "+ avgSentiment+'. ('+str(sum(sentValue))+')')
