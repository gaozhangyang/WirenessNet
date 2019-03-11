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
xlabel('X(a)');ylabel('Y(b)');zlabel('max delay');

%%
fitdata1=[];
for i=21:70
    fitdata1=[fitdata1;x(i,i-1) y(i,i-1) maxz(i,i-1)];
end

fita=fitdata1(:,1);
fitb=fitdata1(:,2);
fitdelay=fitdata1(:,3);

figure;
plot(fita,fitdelay);
xlabel('a','FontSize',16),ylabel('max delay','FontSize',16);

%%
%分奇偶组
fita_even=fita(1:2:50);
fita_odd=fita(2:2:50);
fitdelay_even=fitdelay(1:2:50);
fitdelay_odd=fitdelay(2:2:50);

figure;
plot(fita_even,fitdelay_even);

figure;
plot(fita_odd,fitdelay_odd);

%%
%拟合检验
data1=[];
for i=2:100
    data1=[data1;x(i,i-1) y(i,i-1) maxz(i,i-1)];
end

fit_even=fiteven(data1(:,1));
fit_odd=fitodd(data1(:,1));
plot(data1(:,1),data1(:,3));
hold on;
plot(data1(:,1),fit_even);
hold on;
plot(data1(:,1),fit_odd);
xlabel('a','FontSize',16);ylabel('delay','FontSize',16);
legend('read delay','fit a=2k','fit a=2k+1','FontSize',12);