%clear the workspace
clear all;
clc;

%assign initial variables
v_0 = 10;
y_0 = 10;
time = linspace(0, , 1001);

%plot trajectories for different angles
x_15 = v_0*cos(15)*time;
y_15 = -4.905*time.^2 + v_0*sin(15)*time + y_0;
y_15(y_15 < 0) = 0;
x_35 = v_0*cos(35)*time;
y_35 = -4.905*time.^2 + v_0*sin(35)*time + y_0;
y_35(y_35 < 0) = 0;
x_50 = v_0*cos(50)*time;
y_50 = -4.905*time.^2 + v_0*sin(50)*time + y_0;
y_50(y_50 < 0) = 0;

figure;
hold on;
plot(x_15, y_15, 'r:', 'DisplayName', '15 degrees');
plot(x_35, y_35, 'k:', 'DisplayName', '35 degrees');
plot(x_50, y_50, 'b:', 'DisplayName', '50 degrees');
grid on;
legend('show');
title('Trajectories of projectile launched at different angles');
xlabel('distance (m)');
ylabel('height (m)');
