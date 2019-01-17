function [a]=classification_a(aa)
g=9.8;
if aa<-5*g
    a=-1;
else
    if aa<5*g
        a=0;
    else
        if aa<10*g
            a=1;
        else
            a=2;
        end
    end
end


end