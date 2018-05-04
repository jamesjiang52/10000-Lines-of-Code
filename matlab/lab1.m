%clear the workspace
clear all;
clc;

%plot function for different numbers of points
%101 points
figure;
hold on;
x = linspace(0, 5, 101);
y1 = exp(-x);
y2 = sin(4*pi*x);
y = y1.*y2;
plot(x, y1, x, y2, x, y);
grid on;
xlabel('x');
ylabel('exp(-x)*sin(4*pi*x)');

%11 points
figure;
hold on;
x = linspace(0, 5, 11);
y1 = exp(-x);
y2 = sin(4*pi*x);
y = y1.*y2;
plot(x, y1, x, y2, x, y);
grid on;
xlabel('x');
ylabel('exp(-x)*sin(4*pi*x)');

%5000001 points
figure;
hold on;
x = linspace(0, 5, 5000001);
y1 = exp(-x);
y2 = sin(4*pi*x);
y = y1.*y2;
plot(x, y1, x, y2, x, y);
grid on;
xlabel('x');
ylabel('exp(-x)*sin(4*pi*x)');
