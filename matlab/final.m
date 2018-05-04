%clear the workspace
clear all;
clc;

%first part

%load data and store in arrays (put file in same directory as saved script)
load('robpos.mat');
time = robpos(:, 1);
x_position = robpos(:, 2);
y_position = robpos(:, 3);

%plot discretized position of robot
figure;
hold on;
plot(x_position, y_position);
grid on;
title('Position of robot (discretized)');
xlabel('x position (m)');
ylabel('y position (m)');

%find x and y velocities
x_velocity = diff(x_position)./diff(time);
y_velocity = diff(y_position)./diff(time);

%find x and y accelerations
x_acceleration = diff(x_velocity)./diff(time(1:end - 1));
y_acceleration = diff(y_velocity)./diff(time(1:end - 1));

%initialize a variable representing time symbolically
syms t;

%compute best-fit polynomials
coefs_x_position = polyfit(time, x_position, 6);
coefs_y_position = polyfit(time, y_position, 6);
x_position_f = poly2sym(coefs_x_position, t);
y_position_f = poly2sym(coefs_y_position, t);
coefs_x_velocity = polyfit(time(1: end - 1), x_velocity, 5);
coefs_y_velocity = polyfit(time(1: end - 1), y_velocity, 5);
x_velocity_f = poly2sym(coefs_x_velocity, t);
y_velocity_f = poly2sym(coefs_y_velocity, t);
coefs_x_acceleration = polyfit(time(1: end - 2), x_acceleration, 4);
coefs_y_acceleration = polyfit(time(1: end - 2), y_acceleration, 4);
x_acceleration_f = poly2sym(coefs_x_acceleration, t);
y_acceleration_f = poly2sym(coefs_y_acceleration, t);

%plot individual velocities
figure;
hold on;
plot(time(1:end - 1), x_velocity, 'DisplayName', 'x velocity (discretized)');
fplot(x_velocity_f, [0 60],  'DisplayName', 'x velocity (symbolic)');
plot(time(1:end - 1), y_velocity, 'DisplayName', 'y velocity (discretized)');
fplot(y_velocity_f, [0 60],  'DisplayName', 'y velocity (symbolic)');
grid on;
legend('show');
title('x and y velocities of robot');
xlabel('time (s)');
ylabel('velocity (m/s)')

%plot individual accelerations
figure;
hold on;
plot(time(1:end - 2), x_acceleration, 'DisplayName', 'x acceleration (discretized)');
fplot(x_acceleration_f, [0 60],  'DisplayName', 'x acceleration (symbolic)');
plot(time(1:end - 2), y_acceleration, 'DisplayName', 'y acceleration (discretized)');
fplot(y_acceleration_f, [0 60],  'DisplayName', 'y acceleration (symbolic)');
grid on;
legend('show');
title('x and y accelerations of robot');
xlabel('time (s)');
ylabel('acceleration (m/s^2)');

%replot discretized position, add the symbolic function
figure;
hold on;
plot(x_position, y_position, 'DisplayName', 'discretized');
fplot(x_position_f, y_position_f, [0 60], 'DisplayName', 'symbolic');
grid on;
legend('show');
title('Position of robot');
xlabel('x position (m)');
ylabel('y position (m)');

%second part

%plot position of robot
figure;
hold on;
x_position = 2.4*(cos(pi*(t - 30)/60))^2;
y_position = 2.4*cos(pi*t/60)*sin(pi*t/60);
fplot(x_position, y_position, [0 60]);
grid on;
title('Position of robot');
xlabel('x position (m)');y
label('y position (m)');

%find and plot individual positions
figure;
hold on;
fplot(x_position, [0 60], 'DisplayName', 'x position');
fplot(y_position, [0 60], 'DisplayName', 'y position');
grid on;
legend('show');
title('x and y positions of robot');
xlabel('time (s)');
ylabel('position (m)');

%find and plot individual velocities
figure;
hold on;
x_velocity = diff(x_position);
y_velocity = diff(y_position);
fplot(x_velocity, [0 60], 'DisplayName', 'x velocity');
fplot(y_velocity, [0 60], 'DisplayName', 'y velocity');
grid on;
legend('show');
title('x and y velocities of robot');
xlabel('time (s)');
ylabel('velocity (m/s)');

%find and plot individual accelerations
figure;
hold on;
x_acceleration = diff(x_velocity);
y_acceleration = diff(y_velocity);
fplot(x_acceleration, [0 60], 'DisplayName', 'x acceleration');
fplot(y_acceleration, [0 60], 'DisplayName', 'y acceleration');
grid on;
legend('show');
title('x and y accelerations of robot');
xlabel('time (s)');
ylabel('velocity (m/s^2)');
