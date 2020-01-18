#include<stdio.h>
int main()
{
	int a1,a2,a3,b1,b2,b3;
	scanf("%d %d",&a1,&b1);
	scanf("%d %d",&a2,&b2);
	scanf("%d %d",&a3,&b3);
	double s1,s2,y1,y2,t1,t2;
	s1=(a1+a2)*1.0/2;
	s2=(a2+a3)*1.0/2;
	y1=(b1+b2)*1.0/2;
	y2=(b2+b3)*1.0/2;
	t1=(a2-a1)*1.0/(b2-b1)*(-1);
	t2=(a3-a2)*1.0/(b3-b2)*(-1);
	double a4,b4;
	a4=t1*s1-t2*s2+y2-y1;
	b4=t1*(a4-s1)+y1;
	printf("%.3lf %.3lf",a4,b4);
    
	return 0;
}