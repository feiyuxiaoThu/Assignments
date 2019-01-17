%% here we just consider the high adhesion road 

function [p_after,mm,nn]=control(p_before,wa,lmd,dt,mm,nn)
%%p=risistent torque,wa=wheel accelaration,cv=car velocity,dt=time step
%%length
dp=50000*dt;
T=0.01;%%control period length
if nn<=T/dt
    
    nn=nn+1;
    %%here decide the operation in one control period
    if mm==1
        p_after=p_before+dp;
    else
        if mm==0
        p_after=p_before;
        else
            p_after=p_before-dp;
        end
    end
    
else
%%here is the judgment of control 
%%first judge the wa and lmd
wa=classification_a(wa);
lmd=classification_lmd(lmd);
if lmd==0&&wa==0||lmd==1&&wa==2
    
        if mm==1
            mm=0;
        else
            if mm==0
                mm=1;
            else
                mm=1;
            end
        end

else
if lmd==1&&wa==-1
    mm=-1;
else
    mm=0;
end
end

%%lmd limit control
% if lmd==2
%     mm=-1;
% end

    if mm==1
        p_after=p_before+dp;
    else
        if mm==0
        p_after=p_before;
        else
            p_after=p_before-dp;
        end
    end
nn=1;
end
end