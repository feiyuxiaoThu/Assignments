function k_p=pressure_increase(p_live)
yy=2500;
x=yy^2/(yy*2-p_live);
k_p=yy^2/x^2;
end