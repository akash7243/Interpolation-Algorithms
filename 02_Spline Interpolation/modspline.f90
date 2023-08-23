      SUBROUTINE spline(x,y,n,yp1,ypn,y2,u)
c
cf2py intent(out) :: y2
cf2py intent(hide) :: n
cf2py intent(hide) :: u
cf2py double precision :: u(n)
cf2py double precision :: x(n)
cf2py double precision :: y(n)
cf2py double precision :: yp1
cf2py double precision :: ypn
c
      INTEGER n
      DOUBLE PRECISION yp1,ypn,x(n),y(n),y2(n)
      INTEGER i,k
      DOUBLE PRECISION p,qn,sig,un,u(n)
      if (yp1.gt..99e30) then
         y2(1)=0.d0
         u(1)=0.d0
      else
         y2(1)=-0.5d0
         u(1)=(3./(x(2)-x(1)))*((y(2)-y(1))/(x(2)-x(1))-yp1)
      endif
      do i=2,n-1
         sig=(x(i)-x(i-1))/(x(i+1)-x(i-1))
         p=sig*y2(i-1)+2.
         y2(i)=(sig-1.)/p
         u(i)=(6.*((y(i+1)-y(i))/(x(i+
     *        1)-x(i))-(y(i)-y(i-1))/(x(i)-x(i-1)))/(x(i+1)-x(i-1))-sig*
     *        u(i-1))/p
      end do
      if (ypn.gt..99d30) then
         qn=0.d0
         un=0.d0
      else
         qn=0.5d0
         un=(3.d0/(x(n)-x(n-1)))*(ypn-(y(n)-y(n-1))/(x(n)-x(n-1)))
      endif
      y2(n)=(un-qn*u(n-1))/(qn*y2(n-1)+1.d0)
      do k=n-1,1,-1
         y2(k)=y2(k)*y2(k+1)+u(k)
      end do
      return
      END
      
      SUBROUTINE notaknot(x,y,n,y2)
c
cf2py intent(out) :: y2
cf2py intent(hide) :: n
cf2py double precision :: x(n)
cf2py double precision :: y(n)
c

      INTEGER n
      DOUBLE PRECISION x(n),y(n),y2(n)
      INTEGER i
      DOUBLE PRECISION A(n-2),B(n-2),C(n-2),D(n-2),h(n-1)

c Create step size array      
      do i=1,n-1
         h(i) = x(i+1)-x(i)
      end do
      
      B(1)=2.d0*h(2)+h(1)
      C(1)=h(2)-h(1)
      D(1)=((y(3)-y(2))/h(2))-((y(2)-y(1))/h(1))
      D(1)=6.d0*D(1)*(h(2)/(h(2)+h(1)))

c  Array constructor for A,B,C,D in TDMA excluding boundary points, make D(i) eval more efficient (multiple allocations/loop!)     
      do i=2,n-3
         A(i) = h(i)
         B(i) = 2.d0*(h(i)+h(i+1))
         C(i) = h(i+1)
         D(i) = (y(i+2)-y(i+1))/h(i+1)
         D(i) = D(i)-(y(i+1)-y(i))/h(i)
         D(i) = 6.d0*D(i)
      end do 
      
      A(n-2)=h(n-2)-h(n-1)
      B(n-2)=2.d0*h(n-2)+h(n-1)
      D(n-2)=((y(n)-y(n-1))/h(n-1))-((y(n-1)-y(n-2))/h(n-2))
      D(n-2)=6.d0*D(n-2)*(h(n-2)/(h(n-1)+h(n-2)))      
      
      do i=2,n-3
         B(i+1)=B(i+1)-((A(i+1)*C(i))/B(i))
         D(i+1)=D(i+1)-((A(i+1)*C(i))/B(i))
      end do
      
      y2(n-1)=D(n-2)/B(n-2)
      
      do i=n-2,2,-1
         y2(i)= (D(i-1)-(C(i-1)*y2(i+1)))/B(i-1)
      end do
      
      y2(1)=(1.d0+(h(1)/h(2)))*y2(2)
      y2(1)=y2(1)-(h(1)*y2(3)/h(1))
      y2(n)=(1.d0+(h(n-1)/h(n-2)))*y2(n-1)
      y2(n)=y2(n)-(h(n-1)*y2(n-2)/h(n-2))
      
      return
      END
      
      SUBROUTINE splint(xa,ya,y2a,n,x,y)
c
cf2py intent(hide) :: n
cf2py double precision :: xa(n)
cf2py double precision :: ya(n)
cf2py double precision :: y2a(n)
cf2py double precision :: x
cf2py intent(out) :: y
c
      INTEGER n
      DOUBLE PRECISION x,y,xa(n),y2a(n),ya(n)
      INTEGER k,khi,klo
      DOUBLE PRECISION a,b,h
      klo=1
      khi=n
      do while(khi-klo.gt.1)
         k=(khi+klo)/2
         if(xa(k).gt.x)then
            khi=k
         else
            klo=k
         endif
      end do
      h=xa(khi)-xa(klo)
      if (h.eq.0.d0) pause 'bad xa input in splint'
      a=(xa(khi)-x)/h
      b=(x-xa(klo))/h
      y=a*ya(klo)+b*ya(khi)+((a**3-a)*y2a(klo)+(b**3-b)*y2a(khi))*(h**
     *     2)/6.d0
      return
      END
C  (C) Copr. 1986-92 Numerical Recipes Software Qk.

      SUBROUTINE splintn(xa,ya,y2a,n,xx,yy,m)
c
cf2py intent(hide) :: n
cf2py double precision :: xa(n)
cf2py double precision :: ya(n)
cf2py double precision :: y2a(n)
cf2py intent(hide) :: m
cf2py double precision :: xx(m)
cf2py intent(out) :: yy(m)
c     
      INTEGER n,m
      DOUBLE PRECISION xx(m),yy(m),xa(n),y2a(n),ya(n)
      INTEGER k,khi,klo
      DOUBLE PRECISION a,b,h,x
      do j=1,m
         x=xx(j)
         klo=1
         khi=n
         do while(khi-klo.gt.1)
            k=(khi+klo)/2
            if(xa(k).gt.x)then
               khi=k
            else
               klo=k
            endif
         end do
         h=xa(khi)-xa(klo)
         if (h.eq.0.d0) pause 'bad xa input in splint'
         a=(xa(khi)-x)/h
         b=(x-xa(klo))/h
         yy(j)=a*ya(klo)+b*ya(khi)+((a**3-a)*y2a(klo)+(b**3-b)*
     *        y2a(khi))*(h**2)/6.d0
      end do
      return
      END
