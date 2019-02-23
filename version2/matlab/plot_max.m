function createfigure(xdata1, ydata1, zdata1)
%CREATEFIGURE(xdata1, ydata1, zdata1)
%  XDATA1:  surface xdata
%  YDATA1:  surface ydata
%  ZDATA1:  surface zdata

%  由 MATLAB 于 15-Dec-2018 23:42:44 自动生成

% 创建 figure
figure('OuterPosition',[869 401 721 514]);

% 创建 axes
axes1 = axes;
hold(axes1,'on');

% 创建 surf
surf(xdata1,ydata1,zdata1);

% 创建 zlabel
zlabel({'delay'});

% 创建 ylabel
ylabel({'b'});

% 创建 xlabel
xlabel({'a'});

% 创建 title
title({'max'});

view(axes1,[-3.57272040661216 51.1254385964912]);
grid(axes1,'on');
