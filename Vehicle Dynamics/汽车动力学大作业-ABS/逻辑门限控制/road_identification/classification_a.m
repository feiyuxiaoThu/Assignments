function [a]=classification_a(aa,level_1,level_2,level_3)
cc=0.1;
if aa<level_1*cc
    a=-1;
else
    if aa<level_2*cc
        a=0;
    else
        if aa<level_3*cc
            a=1;
        else
            a=2;
        end
    end
end
end