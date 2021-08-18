#Агоритм сортировки массива по возрастанию.

def findSmallest(arr): #Функция для поиска наименьшего элемента массива
  smallest = arr[0]   #Здесь будет храниться наименьшее значение
  smallest_index = 0  #Здесь хранится индекс наименьшего значения
  for i in range(1, len(arr)):
    if arr[i] < smallest:
      smallest = arr[i]
      smallest_index = i
  return smallest_index

#Далее - функция сортировки выбором

def selectionSort(arr):   #Сортирует массив
  newArr = []
  for i in range (len(arr)):
    smallest = findSmallest(arr) #Находит наименьший элемент в массиве и добавляет его в новый массив
    newArr.append(arr.pop(smallest))
  return newArr

print selectionSort([5, 8, 9, 3, 16, 23]) 
  
