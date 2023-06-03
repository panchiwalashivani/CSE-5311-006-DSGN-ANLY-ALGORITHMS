import time
def linear_search(arr, value):
    t1_start = time.perf_counter()
    for i in range(len(arr)):

        if (arr[i] == value):
            t1_stop = time.perf_counter()
            #print("--- %s seconds ---" % str(t1_stop - t1_start))
            e1 = str(t1_stop - t1_start) + "s"  # Get running time
            #return True
            return (i, e1)
    t1_stop = time.perf_counter()
    e1 = str(t1_stop - t1_start) + "s"
    #print("--- %s seconds ---" % str(t1_stop - t1_start))
    #return False
    return (-1, e1)
#https://www.geeksforgeeks.org/python-program-for-linear-search/
#https://www.geeksforgeeks.org/time-perf_counter-function-in-python/


