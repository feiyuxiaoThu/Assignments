function [p_after,mm,nn,in_out,level_1,level_2,level_3,level]=road_iden(p_before,dt,nn,miu,miu_max,dp,T,lmd_best,wa_level)
% dp=20000*dt;
% T=0.01;%%control period length
in_out=0;
if nn<=T/dt
    nn=nn+1;
    %%here decide the operation in one control period
    p_after=p_before+dp*pressure_increase(p_before);
else
    if (miu_max-miu)/miu_max>0.05
    in_out=1;
    end
    nn=1;
    p_after=p_before+dp*pressure_increase(p_before);
end
    level=lmd_best;
    level_1=-wa_level;
    level_2=wa_level;
    level_3=2*wa_level;
    mm=-1;
end