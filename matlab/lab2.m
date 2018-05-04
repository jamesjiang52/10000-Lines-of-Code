%clear the workspace
clear all;
clc;

%plot the function
t = linspace(0, 4, 101);
height = -2*(t - 2).^3 + 3*(t - 2) + 1
figure;
hold on;
plot(t, height, 'DisplayName', 'trajectory');
grid on;
legend('show');
title('Altitude of drone');
xlabel('time (s)');
ylabel('altitude (m)');

%find and plot roots
roots = find(~height);
plot(t(roots), height(roots), 'ro', 'DisplayName', 'roots');
legend('show');

%find length of time within 30% of target
upper = 0.3*9;
lower = -0.3*9;
times = find(height <= upper && height >= lower);
total = (length(times) - 1)/25;

%calculate velocity at t=4
velocity = 25*(height(end) - height(end - 1));
