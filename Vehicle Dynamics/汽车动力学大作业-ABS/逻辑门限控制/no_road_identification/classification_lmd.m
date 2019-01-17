function [lmd]=classification_lmd(lmd_in)
lmd_1=5;
if lmd_in>lmd_1
    lmd=1;
else
    lmd=0;
end
end