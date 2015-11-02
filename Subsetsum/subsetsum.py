def issubsetsum(mybiglist, n, sum):

    if sum == 0:
        return True
    if n ==0 and sum!=0:
        return False
    if mybiglist[n-1]> sum:
        issubsetsum(mybiglist, n-1, sum)

    return issubsetsum(mybiglist, n-1, sum) or issubsetsum(mybiglist, n-1, sum - mybiglist[n-1])
