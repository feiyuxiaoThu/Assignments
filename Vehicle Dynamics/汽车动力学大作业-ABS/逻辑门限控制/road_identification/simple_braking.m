function bd=simple_braking(t,r)
tt=0.35;
ttt=0.4;
f=9500;
if t<tt
    bd=f*t/tt*r;
else
    if t<ttt
    bd=(f/(tt-ttt)*t+ttt*f/(ttt-tt))*r;
    else
        bd=0;
    end
end

end