from pylab import *
from os import system
system("f2py -c -m spline spline.f")
import spline

xa=linspace(0,10,11)
ya=sin(xa)
y2a=zeros(ya.shape)
xx=linspace(-5,15,101)
yt=sin(xx)
yy=zeros(xx.shape)
u=zeros(ya.shape)

y2a=spline.spline(xa,ya,1.0,cos(10.0))

print( c_[xa,ya])

figure(1)
plot(xa,ya,'r',xa,y2a,'g')
legend(["ya","y2a"])
grid(True)
show()

yyb=spline.splintn(xa,ya,y2a,xx)

figure(2)
plot(xa,ya,'ro',xx,yt,'b+',xx,yyb,'k')
xlim([0,10])
ylim([-1,1])
grid(True)
show()

figure(3)
semilogy(xx,abs(yt-yyb))
grid(True)
show()
