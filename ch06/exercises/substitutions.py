import json

def main():
    news = open("assets/news.txt", "r").read().lower()
    subs_pointer = open("assets/subs.json", "r")
    subs = json.load(subs_pointer) #Now need to use one list to modify another list, so which list should we loop through? 
    for k, v in subs.items(): #Usually easier to loop through the dictionary list 
        news = news.replace(k,v)

    fptr = open("assets/betternews.txt", "w") #Creates new file 
    fptr.write(news)
    fptr.close()

main()