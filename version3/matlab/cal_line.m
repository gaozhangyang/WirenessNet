function [a,b,c] = cal_line(x1,y1,x2,y2)
%UNTITLED �˴���ʾ�йش˺�����ժҪ
%   �˴���ʾ��ϸ˵��
    format rat
    a=-(y1-y2)/(x1-x2);
    b=1;
    c=-(a*x1+y1);
end

