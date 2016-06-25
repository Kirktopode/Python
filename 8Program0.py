def lisChop(thang):
    del thang[0]
    del thang[len(thang)-1]
def lisMiddle(swag):
    return swag[1:len(swag)-1]
lis = ["First", "Second", "Third", "Fourth", "Fifth"]
lis2 = ["Two", "Three", "Five", "Eight"]
lis3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
lisChop(lis)
lisChop(lis2)
lisChop(lis3)
print lis
print lis2
print lis3
sil = lisMiddle(lis)
sil2 = lisMiddle(lis2)
sil3 = lisMiddle(lis3)
print sil, sil2, sil3
