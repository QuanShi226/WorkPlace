def countWords(aString):
  string_dict = dict()
  string_list = removePunctuation(aString)
  string_list = string_list.lower()
  string_list = string_list.split()
  for item in string_list:
    if item in string_dict:
      string_dict[item] += 1
    else:
      string_dict[item] = 1
  return string_dict

def removePunctuation(txt):
  myList = list(txt)
  for i in range(len(myList)):
    if myList[i].isalpha() == 0:
      myList[i]=" "
  return "".join(myList)

result = countWords('He is here,HERE he is now')
print(result)