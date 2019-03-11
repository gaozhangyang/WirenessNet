function [a,b,c] = cal_line(x1,y1,x2,y2)
%UNTITLED 此处显示有关此函数的摘要
%   此处显示详细说明
    format rat
    a=-(y1-y2)/(x1-x2);
    b=1;
    c=-(a*x1+y1);
end

