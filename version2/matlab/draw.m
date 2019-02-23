%%
clear all
load('../results/all_results.mat')
a=r(:,1);b=r(:,2);max_=r(:,3);
[x,y]=meshgrid(1:100,1:100);

maxz=ones(100,100)*Inf;
for i=1:length(a)
    index1=a(i);
    index2=b(i);
    maxz(index2,index1)=max_(i);
end
figure
surf(x,y,maxz)

%%
fitdata1=[];
for i=21:100
    fitdata1=[fitdata1;x(i,i-1) y(i,i-1) maxz(i,i-1)];
end

fita=fitdata1(:,1);
fitb=fitdata1(:,2);
fitdelay=fitdata1(:,3);