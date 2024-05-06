# Does not account for zeros - need to fix this

class SelectionSort():
    def __init__(self, myArray) -> None:
        self.myArray = myArray

    def selectionSort(self):
        for i in range(len(self.myArray)):
            min_index = i
            for j in range(i+1, len(self.myArray)):
                if self.myArray[min_index] > self.myArray[j]:
                    min_index = j
                self.myArray[i], self.myArray[min_index] = self.myArray[min_index], self.myArray[i]
        return self.myArray

testArray = [5,7,2,4,9,1,0,4]
sortedArray = SelectionSort(testArray)
print(sortedArray.selectionSort())