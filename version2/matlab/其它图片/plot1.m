%平均发现延迟对比图
t=0:0.1:25;
plot(t,t.^0.5/5)
hold on
plot(t,t./25)
xlabel('t')
ylabel('delay')
legend('A','B')