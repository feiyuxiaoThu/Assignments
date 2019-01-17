function [miu]=magic_high(lmd,fz)
%% unit: lmd is under % force is under KN
fz=fz/1000;
b0=2.37272;
b1=-9.46;%% top value will decrease as this value decrease
b2=1490;
b3=130;%% the x location of top point will move right as this value decrease
b4=276;
b5=0.0886;
b6=0.00402;%% the tail hight will drease as this value drease
b7=-0.0615;
b8=1.2;
b9=0.0299;
b10=-0.176;

c=b0;
d=b1*fz.^2+b2*fz;
bcd=(b3*fz.^2+b4*fz)*exp(-b5*fz);
b=bcd/(c*d);
sh=b9*fz+b10;
sv=0;
e=b6*fz.^2+b7*fz+b8;

x1=lmd+sh;

if lmd<=100&&lmd>=-100
f_ris=(d*sin(c*atan(b*x1-e*(b*x1-atan(b*x1)))))+sv;
miu=f_ris/fz/1000;
else
    if lmd>=100
    x1=100+sh;
    f_ris=(d*sin(c*atan(b*x1-e*(b*x1-atan(b*x1)))))+sv;
    miu=f_ris/fz/1000;
    else
    x1=-100+sh;
    f_ris=(d*sin(c*atan(b*x1-e*(b*x1-atan(b*x1)))))+sv;
    miu=f_ris/fz/1000;
    end
end
end