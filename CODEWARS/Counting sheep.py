#Consider an array of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present
#in the array (true means present).
#Code Wars  Stepan Zhuk    "Counting sheep"


def count_sheeps(array_of_sheep):
  count = 0
  for sheep in array_of_sheep:
      if sheep==True:
          count += 1 
  return count
