  def binary_search(list, item):
    low = 0
    high - len(list)-1 #Переменные low и high содержат границы той части списка, в которой выполняется поиск.
    while low <= high:
      mid = (low + high)/2 #mid - средний элемент
      guess = list[mid]
      if guess == item:
        return mid
      if guess > item:
        high = mid - 1
        else:
          low - mid + 1
    return None
  
  my_list = [1, 3, 5, 7, 9]
  
  
