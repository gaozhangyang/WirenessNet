function createfigure(xdata1, ydata1, zdata1)
%CREATEFIGURE(xdata1, ydata1, zdata1)
%  XDATA1:  surface xdata
%  YDATA1:  surface ydata
%  ZDATA1:  surface zdata

%  �� MATLAB �� 15-Dec-2018 23:42:44 �Զ�����

% ���� figure
figure('OuterPosition',[869 401 721 514]);

% ���� axes
axes1 = axes;
hold(axes1,'on');

% ���� surf
surf(xdata1,ydata1,zdata1);

% ���� zlabel
zlabel({'delay'});

% ���� ylabel
ylabel({'b'});

% ���� xlabel
xlabel({'a'});

% ���� title
title({'max'});

view(axes1,[-3.57272040661216 51.1254385964912]);
grid(axes1,'on');
