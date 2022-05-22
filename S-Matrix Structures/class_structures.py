import numpy as np

class DataStructure:
    """
    For a positive number, this should create a numpy array of all divisors and
    return a matrix that splits the array into 2 parts. For odd array lengths,
    the mid-value is repeated to get an even length.
    """
    def __init__(self,number):
        _small_divisors = np.asarray([ i for i in range(1,int(number**.5)+1) if number%i==0 ])
        _large_divisors = number//_small_divisors
        self.divisors_with_mid_value = np.concatenate([_small_divisors,[*reversed(_large_divisors)]])
        self.divisors_as_matrix = np.column_stack([_small_divisors,_large_divisors])
        if ( _small_divisors[-1] == _large_divisors[-1] ):
            self.divisors = np.concatenate([_small_divisors[:-1],[*reversed(_large_divisors)]])
        else:
            self.divisors = self.divisors_with_mid_value

if __name__=='__main__':
    for number in (7,16,30):
        data = DataStructure(number)
        print(data.divisors_as_matrix,data.divisors,data.divisors_with_mid_value)
