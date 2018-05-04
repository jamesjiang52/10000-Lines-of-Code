%clear the workspace
clear all;
clc;

%assign initial variables
P = 50000;
E = 10^9*[70 204 190];
A = 4*(1/100^2);
d = linspace(0, 16, 101);

%create blank arrays for forces
F_AD = zeros(1, 101);
F_BE = zeros(1, 101);
F_CG = zeros(1, 101);

%populating force arrays for every value of d
for i = 1:101
    forces = [6 -20 5 0; 0 10 16 d(i)*P; 1 1 1 P];
    forces_reduced = rref(forces);
    F_AD(i) = forces_reduced(1, 4);
    F_BE(i) = forces_reduced(2, 4);
    F_CG(i) = forces_reduced(3, 4);
end

%create arrays for percent elongation of each bar
%E(i) has a parameter that can be manually adjusted
L_AD = F_AD/(E(1)*A)*100;
L_BE = F_BE/(E(1)*A)*100;
L_CG = F_CG/(E(1)*A)*100;

%create plot
%title can be changed according to the parameter mentioned above
figure;
hold on;
plot(d, L_AD, 'k.', 'MarkerSize', 10);
plot(d, L_BE, 'b.', 'MarkerSize', 10);
plot(d, L_CG, 'r.', 'MarkerSize', 10);
grid on;
legend('AD', 'BE', 'CG');
title('Elongation of aluminum alloy bars vs distance');
xlabel('distance (m)');
ylabel('elongation (%)');
