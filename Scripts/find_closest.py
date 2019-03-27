def find_closest(list,x):
    idx= list.searchsorted(x)
    idx= np.clip(idx,1,len(list)-1)
    left=list[idx-1]
    right= list[idx]
    idx-= x - left<right - x
    return idx