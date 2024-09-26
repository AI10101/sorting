import math


class bubble_sort():

    @staticmethod
    def sort(arr, *args):
        for i in range(len(arr)):
            swaps = 0
            for j in range(len(arr) - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j+1], arr[j]
                    swaps += 1
            if not swaps: return

    @staticmethod
    def bigO(n):
        return n**2
    

class selection_sort():

    @staticmethod
    def sort(arr, *args):
        for i in range(len(arr) - 1):
            min_index = i
            for j in range(i+1, len(arr)):
                if arr[min_index] > arr[j]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
            

    @staticmethod
    def bigO(n):
        return n**2
    

class insertion_sort():

    @staticmethod
    def sort(arr, *args):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i-1

            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
            

    @staticmethod
    def bigO(n):
        return n**2
    

class merge_sort():

    @staticmethod
    def merge(arr, left, mid, right):
        n1 = mid - left + 1
        n2 = right - mid

        l = arr[left:left+n1]
        r = arr[mid+1:right+1]

        i = 0
        j = 0
        k = left

        while i < n1 and j < n2:
            if l[i] <= r[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
            k +=1

        while i < n1:
            arr[k] = l[i]
            i += 1
            k += 1

        while j < n2:
            arr[k] = r[j]
            j += 1
            k += 1

    @staticmethod
    def sort(arr, right, left=0):
        if left < right:
            mid = left + (right - left) // 2
            merge_sort.sort(arr, mid, left)
            merge_sort.sort(arr, right, mid+1)
            merge_sort.merge(arr, left, mid, right)
            

    @staticmethod
    def bigO(n):
        return n * math.log2(n)
    

class quick_sort():

    @staticmethod
    def sort(arr, end, start=0):
        if start < end:
            pivot = quick_sort.partition(arr, start, end)
            quick_sort.sort(arr, pivot-1, start)
            quick_sort.sort(arr, end, pivot+1)

    @staticmethod
    def partition(arr, start, end):
        pivot = arr[end]
        i = start - 1

        for j in range(start, end):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i+1], arr[end] = arr[end], arr[i+1]
        return i+1

    @staticmethod
    def bigO(n):
        return n * math.log2(n)
    

class python_sort():

    @staticmethod
    def sort(arr, *args):
        arr.sort()

    @staticmethod
    def bigO(n):
        pass # ???
