def words(n):
  result = {}
  word_list = n.split()
  for words in word_list:
    if words.isdigit():
      result [int(words)] = word_list.count(words)
    else:
      result[words] = word_list.count(words)
  return result
words("olly olly in come free")