import numpy as np

"""
This should from any input create a numpy array and return a matrix that splits the array
into 2^n parts. For odd array lengths, the mid-value is inserted to get an even value.
"""

class data_structure:

    kind_list = []

    def __init__(self, number):
        self.kind_list = np.random.permutation(number)
    
    def __get__(self, position):
        return self.kind_list[position]

    """

    The above will get into defining the various initialisations and methods
    to interact with data_structure without the functions bellow

    """
    def multiple(self,number):
        i = 0
        multiples=[]
        while i < number:
            i+=1
            for mult in range(0, number+1, i):
                if number == mult:
                    multiples.append(i)
        return np.asarray(multiples) #return these multiples in a numpy list
        #ADD A MID VALUE:

    def mid_value(self, number, no_array = False):
        self._mid_value = self.multiple(number) #set _mid_value as the multiples list
        if no_array == False:
            if len(self._mid_value) %2 != 0:
                mid_value = int((len(self._mid_value) - 1)/2)
                for ind, middle in enumerate(self._mid_value):
                    if middle == self._mid_value[mid_value]:
                        test=np.insert(self._mid_value, ind, middle)
                        return test
            else:
                return self._mid_value
        else:
            pass

    def reshape_array(self,number): 
        _array_ = self.mid_value(number, no_array = False).copy()
        array_ = self.mid_value(number, no_array = False)
        
        len_arr_ = len(array_)
        n = 0
        reduced_arrays = []
        if len_arr_ > 2:
            while n < len_arr_: # select only powers of 2
                n += 2
                if len_arr_ > n: #if the length of the array is greater than the power of 2 do conditional
                    splice = len_arr_-(n-1) #we want to splice the outer two values and delete then reduce
                    reduced_arrays.append(array_[::splice])
                    search_reduce = np.searchsorted(array_, array_[::splice])
                    reduce_array = np.delete(array_, search_reduce)
                    array_ = reduce_array #this is to return to the spliced value when reduced
                    if len(array_) == 2:
                        reduced_arrays.append(array_) #we do not get the reduced values above so get the value two values
                    else:
                        continue
        else:
            return _array_
        return np.column_stack(reduced_arrays).T   #this should stack them and return a matrix with maximum 2 columns and 2^n rows
 


data = data_structure(5)
print(data.kind_list)