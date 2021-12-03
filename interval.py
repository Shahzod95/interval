import math
nan = float('nan')
oo = float('inf')
class Interval:
    def __init__(x,a,b):
        if a > b:
            x.lb, x.ub = nan
        else:
            x.lb, x.ub = a,b

    def is_empty(x):
        return math.isnan
    
    def __add__(x,y):
        return Interval(x.lb+y.lb, x.ub+y.ub)

    def __sub__(x,y):
        return Interval(x.lb-y.ub, x.ub-y.lb)

    def __mul__(x,y):
        L=[x.lb*y.lb,x.lb*y.ub,x.ub*y.lb,x.ub*y.ub]
        return Interval(min(L), max(L))

    def __rmul__(x,y):
        return x.__mul__(Interval(y,y))

    def __contains__(x,a):
        return (x.lb<=a<=x.ub)

    def __truediv__(x,y):
        if 0 in y:
            return Interval(-oo, oo)
        else:
            return x*Interval(1./y.ub,1./y.lb)
        
    def __repr__(x):
        return ("[%f,%f]"%(x.lb,x.ub))

def sqr(x):
    L=[x.lb**2,x.ub**2]
    if 0 in x:
        return Interval(0,max(L))
    else:
        return Interval(min(L),max(L))

def mini(x,y):
    return (Interval(min(x.lb,y.lb),min(x.ub,y.ub))


def maxi(x,y):
    return (Interval(max(x.lb,y.lb),max(x.ub,y.ub))

def exp(x):
    return (Interval(math.exp(x.lb),math.exp(x.ub)))

def log(x):
    if x.ub<=0:
        return Interval(1,0)
    elif 0 in x:
        return Interval(-oo,math.log(x.ub))
    else:
        return (Interval(math.log(x.lb),math.log(x.ub)))


if __name__ == '__main__':
    x = Interval(-2,2)
    y = Interval(3,4)
    print(x+y)
            
