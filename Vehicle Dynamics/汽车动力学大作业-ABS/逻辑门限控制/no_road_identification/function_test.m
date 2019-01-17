%%test of classification of acceleration
clear
x=[-1000:1:1000];
for i=1:2001
    y(i)=classification_a(x(i));
end
plot(x,y)
%% test of claasification_lmd
clear 
x=[0:0.01:1];
for i=1:101
    y(i)=classification_lmd(x(i));
end
plot(x,y)

%% test of magic function
clear 
fz=5000*ones(1,1001);
lmd=[0:0.1:100];

for i=1:1001
    miu(i)=magic_low(lmd(i),fz(i));
end
plot(lmd,miu)
hold on
clear 
fz=5000*ones(1,1001);
lmd=[0:0.1:100];

for i=1:1001
    miu(i)=magic_high(lmd(i),fz(i));
end
plot(lmd,miu)
hold on
%% test of simple_braking
clear 
x=[0:0.001:1];

for i=1:1001
    miu(i)=simple_braking(x(i),0.4);
end
plot(x,miu)
hold on