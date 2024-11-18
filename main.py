#Program to solve ordinary differential equation of order n<=5 using Runge-Kutta Method of fourth order by Maciej Cichosz
import numpy
import matplotlib.pyplot
#here the user needs to define the n-th derivative of sought function as a function of other derivatives, the function and a variable
#def f(x,y,d1y,d2y,d3y,d4y):
def f(x,dy):
    #print (dy)
    return -0.1*dy[1]
    #return numpy.float64(dy[1])**2-numpy.float64(dy[0])
#dy[i] is the (i)th derivative. dy[0] is the value of y.

print ("Please enter the order of the equation.")
order=int(input())
#order=int(5)

print ("Please enter the number of steps the program has to calculate.")
steps=int(input())

print ("Please enter the step between x values.")
h=float(input())

#The program uses initial conditions for the same x for all derivatives of the function y.
x=[0]*(steps+1)
print ("Please enter the initial value of the variable x.")
x[0]=float(input())

#y=[0]*(steps+1)
#print ("Please enter the initial value of the function y.")
#y[0]=int(input())

#derivatives=[[0]*order+1]*(steps+1)
derivatives=numpy.zeros([order+1, steps+1])

for i in range (0, order):
    if i>3:
        print("Please enter the initial value of", i, "-th derivative.")
        derivatives[i,0]=float(input())
    elif i==0:
        print ("Please enter the initial value of the function y.")
        derivatives[i,0]=float(input())
    elif i==1:
        print("Please enter the initial value of first derivative.")
        derivatives[i,0]=float(input())
    elif i==2:
        print("Please enter the initial value of second derivative.")
        derivatives[i,0]=float(input())
    elif i==3:
        print("Please enter the initial value of third derivative.")
        derivatives[i,0]=float(input())

f0=[0]*(order+1)
f1=[0]*(order+1)
f2=[0]*(order+1)
f3=[0]*(order+1)
fh=[0]*(order+1)
#for i in range (1,steps+1):
#    print (derivatives[:,i-1])
'''
#for i in range (1,steps+1):
    #dy=derivatives[:,i-1]
for i in range (1,steps+1):
    for j in range (0,order+1):
        if j==order:
            #f0[j]=f(x[i-1],y[i-1],derivatives[0][i-1],derivatives[1][i-1],derivatives[2][i-1],derivatives[3][i-1])
            #f0=f(x[i-1],y[i-1],derivatives[:,i-1])
            f0[j] = f(x[i-1], derivatives[:,i-1])
        else:
            f0[j]=derivatives[j+1,i-1]*h
    for j in range (0,order+1):
        for k in range(0, order + 1):
            fh[k] = f0[k]/ 2
        if j==order:
            #f1[j]=f(x[i-1]+h/2,y[i-1]+h/2*f0[0],derivatives[0][i-1]+h/2*f0[1],derivatives[1][i-1]+h/2*f0[2],derivatives[2][i-1]+h/2*f0[3],derivatives[3][i-1]+h/2*f0[4])
            #f1[j] = f(x[i-1]+h/2,y[i-1]+h/2*f0[0],(derivatives[:,i-1]+))
            f1[j] = f(x[i-1]+h/2, derivatives[:,i-1]+fh)
        elif j==order-1:
            f1[j] = f1[j+1]*h
        else:
            f1[j]=(derivatives[j+1][i-1]+f0[j+1]/2)*h
            #f1[j]=f0[j]
    for j in range (0,order+1):
        for k in range(0, order + 1):
            fh[k] = f1[k]/ 2
        if j==order:
            #f2[j]=f(x[i-1]+h/2,y[i-1]+h/2*f1[0],derivatives[0][i-1]+h/2*f1[1],derivatives[1][i-1]+h/2*f1[2],derivatives[2][i-1]+h/2*f1[3],derivatives[3][i-1]+h/2*f1[4])
            f2[j] = f(x[i-1]+h/2, derivatives[:,i-1]+fh)
        elif j == order - 1:
            f2[j] = f2[j + 1] * h
        else:
            f2[j]=(derivatives[j+1][i-1]+f1[j+1]/2)*h
            #f2[j] = f1[j]
    for j in range (0,order+1):
        for k in range(0, order + 1):
            fh[k] = f2[k]
        if j==order:
            #f3[j]=f(x[i-1]+h,y[i-1]+h*f2[0],derivatives[0][i-1]+h*f2[1],derivatives[1][i-1]+h*f2[2],derivatives[2][i-1]+h*f2[3],derivatives[3][i-1]+h*f2[4])
            f3[j] = f(x[i-1]+h, derivatives[:,i-1]+fh)
        elif j == order - 1:
            f3[j] = f3[j + 1] * h
        else:
            f3[j]=(derivatives[j+1][i-1]+f2[j+1])*h
            #f3[j] = f2[j]
    x[i] = x[i - 1] + h
    #f1[order] = f0[order]
    #f2[order] = f0[order]
    #f3[order] = f0[order]
    for j in range(0,order+1):
        if j == order:
            derivatives[j][i]=derivatives[j][i-1]+(f0[j]+f1[j]*2+f2[j]*2+f3[j])/6
        else:
            derivatives[j][i]=derivatives[j][i-1]+(f0[j]+f1[j]*2+f2[j]*2+f3[j])/6
'''

'''for i in range (1,steps+1):
    x[i]=x[i-1]+h
    #y[i]=y[i-1]+h/6*(f0[0]+f1[0]*2+f2[0]*2+f3[0])
    derivatives[order][i]=f(x[i-1],derivatives[:,i-1])
    #derivatives[order][i]=1
    for j in range(0, order):
        derivatives[j][i]=derivatives[j][i-1]+derivatives[j+1][i-1]*h
    #for j in range(0,order+1):
        #derivatives[j][i]=derivatives[j][i-1]+(f0[j]*h+f1[j]*2*h+f2[j]*2*h+f3[j]*h)/6
'''
derivatives[order][0]=0
derivatives[order][0]=f(x[0],derivatives[:,i-1])

for i in range (1,steps+1):
    x[i]=x[i-1]+h
    #derivatives[order][i]=f(x[i-1],derivatives[:,i-1])
    f0[order]=f(x[i-1],derivatives[:,i-1])
    for j in range (0,order+1):
        if j==0:
            f0[order-j] = f(x[i - 1], derivatives[:, i - 1])
        elif j==1:
            f0[order - j] = f(x[i - 1], derivatives[:, i - 1]) * h
        else:
            f0[order - j] = derivatives[order-j+1][i-1] * h

    for k in range(0, order + 1):
        fh[k] = f0[k] / 2

    for j in range(0, order + 1):
        if j == 0:
            f1[order - j] = f(x[i - 1] + h / 2, derivatives[:, i - 1] + fh)
        elif j == 1:
            f1[order - j] = f(x[i - 1] + h / 2, derivatives[:, i - 1] + fh) * h
        else:
            f1[order - j] = (derivatives[order - j + 1][i - 1] + f0[order - j + 1] / 2) * h

    for k in range(0, order + 1):
        fh[k] = f1[k] / 2

    for j in range(0, order + 1):
        if j == 0:
            f2[order - j] = f(x[i - 1] + h / 2, derivatives[:, i - 1] + fh)
        elif j == 1:
            f2[order - j] = f(x[i - 1] + h / 2, derivatives[:, i - 1] + fh) * h
        else:
            f2[order - j] = (derivatives[order - j + 1][i - 1] + f1[order - j + 1] / 2) * h

    for k in range(0, order + 1):
        fh[k] = f2[k]

    for j in range(0, order + 1):
        if j == 0:
            f3[order - j] = f(x[i - 1] + h, derivatives[:, i - 1] + fh)
        elif j == 1:
            f3[order - j] = f(x[i - 1] + h, derivatives[:, i - 1] + fh) * h
        else:
            f3[order - j] = (derivatives[order - j + 1][i - 1] + f2[order - j + 1]) * h
        #derivatives[order-j][i]=derivatives[order-j+1][i-1]*h+derivatives[order-j][i-1]

    for j in range(0, order + 1):
        derivatives[order - j][i]=derivatives[order - j][i-1] + (f0[order - j] +2*f1[order - j] +2*f2[order - j] +f3[order - j])/6

y=derivatives[0,:]
z=derivatives[1,:]
#w=derivatives[2,:]
#print (derivatives[0,:])
#print (derivatives[1,:])
#print (derivatives[2,:])
#print (y)
matplotlib.pyplot.plot(x,y)
matplotlib.pyplot.plot(x,z)
#matplotlib.pyplot.plot(x,w)
matplotlib.pyplot.show()