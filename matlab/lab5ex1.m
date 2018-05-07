%clear the workspace
clear all;
clc;

%data points
time = [0 5 10 15 20];
concentration = [200 152 118 93 74];

%compute best-fit polynomials and exponential
time_d = linspace(0, 30, 301);
coefs_3 = polyfit(time, concentration, 3);
concentration_3 = polyval(coefs_3, time_d);
coefs_4 = polyfit(time, concentration, 4);
concentration_4 = polyval(coefs_4, time_d);
concentration_exp = fit(time, concentration, 'exp1');

%plot data points and best fit functions
%symbolic expontential fit
syms t;
concentration_exp_sym = A*exp(b*t); %A and b determined from exponential fit

figure;
hold on;
plot(time, concentration);
plot(time_d, concentration_3, 'DisplayName', '3rd order polynomial');
plot(time_d, concentration_4, 'DisplayName', '4th order polynomial');
fplot(concentration_exp_sym, 'DisplayName', 'Exponential');
grid on;
legend('show');
title('Best-fit models of penicillin clearance');
xlabel('time (min)');
ylabel('concentation (ug/mL)');

t_40 = solve(concentration_exp_sym == 40);
t_20 = solve(concentration_exp_sym == 20);
