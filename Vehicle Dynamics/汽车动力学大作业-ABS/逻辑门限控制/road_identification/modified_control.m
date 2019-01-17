%% here we just consider the high adhesion road 

function [p_after,mm,nn]=modified_control(p_before,wa,lmd_in,dt,mm,nn,level_1,level_2,level_3,level,dp,T)
%%p=risistent torque,wa=wheel accelaration,cv=car velocity,dt=time step
ccc=2;%%this parameter is used to control the lmd limit
if nn<=T/dt
    
    nn=nn+1;
    %%here decide the operation in one control period
    if mm==1
        p_after=p_before+dp*pressure_increase(p_before);
    else
        if mm==0
        p_after=p_before;
        else
            p_after=p_before-dp*pressure_increase(p_before);
        end
    end
else
%%here is the judgment of control 
%%first judge the wa and lmd
wa=classification_a(wa,level_1,level_2,level_3);
lmd=classification_lmd(lmd_in,level);
if lmd==0&&wa==0||lmd==1&&wa==2&&lmd_in<=ccc*level||lmd_in<=level/ccc
    
        if mm==1
            mm=0;
        else
                mm=1;
        end

else
if lmd==1&&wa==-1||lmd_in>ccc*level%%here, one more judgment is added
    mm=-1;
else
    mm=0;
end
end
    if mm==1
        p_after=p_before+dp*pressure_increase(p_before);
    else
        if mm==0
        p_after=p_before;
        else
            p_after=p_before-dp*pressure_increase(p_before);
        end
    end
nn=1;
end
    if p_after<0
        p_after=0;
    end
end