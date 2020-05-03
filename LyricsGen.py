import numpy as np

## k denote window size => type 4 characters 5th one will get predicated

def generateTable(data, k = 4):
  T={}

  for i in range(len(data) - k):
    x = data[i:i+k]
    y = data[i+k]

    if T.get(x) is None:
      T[x] = {}       ## T = { hell : { 'o' : 1} .... }
      T[x][y] = 1
    else:
      if T[x].get(y) is None:
        T[x][y] = 1
      else:
        T[x][y] +=1
  return T



def convertFrequencyIntoProb(T):
  for kx in T.keys():
    s=float(sum(T[kx].values())) ## getting value sum them n converting into float
    for k in T[kx].keys():
      T[kx][k] = T[kx][k]/s; ## finding probability
  
  return T





def trainMarkovChain(text, k=4):
  T= generateTable(text)
  T = convertFrequencyIntoProb(T)
  return T



def sample_text(ctx, T, k=4):   ## this function will return single characters according to the markov Chain
  ctx = ctx[-k:]
  if T.get(ctx) is None:
    return " "            # if not in return return " "

  possible_chars = list(T[ctx].keys())
  possible_prob = list(T[ctx].values())

  return np.random.choice(possible_chars, p=possible_prob)


def generatetext(starting_sent, k=4, maxLen=10000): # this will generate language of 10000 characters by appending them character by character
  sentence = starting_sent
  ctx=starting_sent[-k:]

  for ix in range(maxLen):
    next_pred = sample_text(ctx,T,k)
    sentence += next_pred
    ctx =sentence[-k:]
  return sentence

if __name__ == "__main__":
  with open("english_speech_2.txt") as f:  ##Reading Text File
    text = f.read().lower() ## converting all characters to lower case
  
  T=trainMarkovChain(text)
  msg = generatetext("dear") ##dear is the starting word

  print(msg)
