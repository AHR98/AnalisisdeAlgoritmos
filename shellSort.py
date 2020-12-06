def shellSort(array):
    n = len(array)//2
    while n > 0:
        for i in range(n):
            gap_InsertionSort(array, i, n)
            n = n // 2

def gap_InsertionSort(narray, nstart, ngap):
  for i in range(nstart+ngap, len(narray)):
    value = narray[i]
    position = i
    while position >= ngap and narray[position-ngap] > value:
      narray[position] = narray[position-ngap]
      position = position-ngap

    narray[position] = value
