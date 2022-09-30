def like_or_dislike(list_):
  result = list_[0]
  for i in range(1, len(list_)):
    if list_[i] == result:
      result = "nothing"
    else:
      result = list_[i]
  return result