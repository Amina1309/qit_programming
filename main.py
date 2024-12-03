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

inputfromfilequestion=0
while inputfromfilequestion==0:
    print ("Do you want to load the input from a file in the program directory? (Y/N)")
    input_from_file=input()

    if input_from_file=="Y" or input_from_file=="y":
        inputfile=open("input.txt", "r")
        order = int(inputfile.readline())
        steps = int(inputfile.readline())
        h = float(inputfile.readline())
        x = [0] * (steps + 1)
        x[0] = float(inputfile.readline())
        derivatives = numpy.zeros([order + 1, steps + 1])
        for i in range(0, order):
            if i > 3:
                derivatives[i, 0] =float(inputfile.readline())
                #print(derivatives[i, 0])
            elif i == 0:
                derivatives[i, 0] =float(inputfile.readline())
                #print(derivatives[i, 0])
            elif i == 1:
                derivatives[i, 0] =float(inputfile.readline())
                #print(derivatives[i, 0])
            elif i == 2:
                derivatives[i, 0] =float(inputfile.readline())
                #print(derivatives[i, 0])
            elif i == 3:
                derivatives[i, 0] =float(inputfile.readline())
                #print(derivatives[i, 0])
        inputfile.close()
        inputfromfilequestion = 1
    elif input_from_file=="N" or input_from_file=="n":
        print ("Please enter the order of the equation.")
        order=int(input())
        #order=int(5)

        print ("Please enter the number of steps the program has to calculate.")
        print ("WARNING: The program may crash for too many steps if the solution diverges to infinity.")
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
        inputfromfilequestion = 1
    else:
        print("Invalid input. Please use Y or N.")



f0=[0]*(order+1)
f1=[0]*(order+1)
f2=[0]*(order+1)
f3=[0]*(order+1)
fh=[0]*(order+1)
#for i in range (0,10):
    #print (type(derivatives[:,0]))


derivatives[order][0]=0
derivatives[order][0]=f(x[0],derivatives[:,0])

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