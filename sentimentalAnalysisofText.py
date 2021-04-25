from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer #import SentimentIntensityAnalyzer from vaderSentiment

def sentiment_scores(text):
  obj = SentimentIntensityAnalyzer() # creating object
  sent_dict = obj.polarity_scores(text) 

  print("Sentiment analysis of text:-", sent_dict)
  print("Text was rated as ", sent_dict['pos']*100, "% Positive") 
  print("Text was rated as ", sent_dict['neu']*100, "% Neutral") 
  print("Text was rated as ", sent_dict['neg']*100, "% Negative") 
  
  print("Text Overall Rated As", end = " ") 

  if sent_dict['compound'] >= 0.05:
    print("Positive")
  elif sent_dict['compound'] <= -0.05:
    print("Negative")
  else:
    print("Neutral")


if __name__ =="__main__":
  with open('resEt.txt','r',encoding='utf-8') as f:
    text = f.read() 
  sentiment_scores(text) 

