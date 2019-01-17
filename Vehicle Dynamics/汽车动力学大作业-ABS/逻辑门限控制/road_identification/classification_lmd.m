function [lmd]=classification_lmd(lmd_in,level)
if lmd_in>level
    lmd=1;
else
    lmd=0;
end
end