%clear the workspace
clear all;
clc;

%exercise 1

%compute velocity
syms t;
h(t) = -2*(t - 2)^3 + 3*(t - 2) + 1;
v(t) = diff(h);

%plot height and velocity
figure;
hold on;
fplot(h, 'DisplayName', 'altitude');
fplot(v, 'DisplayName', 'velocity');
grid on;
legend('show');
xlim([0 4]);
title('Altitude and velocity of drone');
xlabel('time (s)');
ylabel('altitude (m) or velocity (m/s)');

%exercise 2

%part a
syms t;
v(t) = 3*t^2 + 1;
area_a = int(v, [0 4]);

%part b
syms x;
f(x) = sqrt(24 - 2*x - x^2);
area_b = int(f, [-6 4]);

%exercise 3

syms t;
A = 14.4;
b = 2.72;

%compute position
v(t) = A*(1 - exp(-t/b));
s_without_ic(t) = int(v);
s(t) = s_without_ic(t) - s_without_ic(0);

%plot position and velocity
figure;
hold on;
fplot(s, 'DisplayName', 'position');
fplot(v, 'DisplayName', 'velocity');
grid on;
legend('show');
xlim([0 15]);
title('Position and velocity of short distance runner');
xlabel('time (s)');
ylabel('position (m) or velocity (m/s)');

t_at_100_s = solve(s == 100);
v_at_100_s = v(t_at_100_s)*3.6; %speed in km/h

%exercise 4

%compute velocity and acceleration
syms t
y(t) = 15*(1 + exp(-t)*cos(t));
v(t) = diff(y);
a(t) = diff(v);

%plot velocity
figure;
hold on;
fplot(v, [0 3]);
grid on;
title('Altitude of bungee cord jumper');
xlabel('time (s)');
ylabel('altitude (m)');

v_at_1_t = v(1);
v_at_3_t = v(3);
t_at_0_a = solve(a == 0);
max_velocity = max(v(t_at_0_a));
t_at_0_v = solve(v == 0);
min_altitude = min(y(t_at_0_v));
