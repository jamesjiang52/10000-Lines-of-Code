%clear the workspace
clear all;
clc;

%initialize variables
micah_grades = [62 52 71 80 83];
chirag_grades = [82 55 60 56 79];

total_gpa_micah = 0;
c_counter_micah = 0;
total_gpa_chirag = 0;
c_counter_chirag = 0;

%loop through Micah’s grades
for i = 1:length(micah_grades)
    total_gpa_micah = total_gpa_micah + gpa(micah_grades(i));
    if gpa(micah_grades(i)) >= 2.3
        c_counter_micah = c_counter_micah + 1;
    end    
end

%loop through Chirag’s grades
for i = 1:length(chirag_grades)
    total_gpa_chirag = total_gpa_chirag + gpa(chirag_grades(i));
    if gpa(chirag_grades(i)) >= 2.3
        c_counter_chirag = c_counter_chirag + 1;
    end    
end

%check eligibility for each scholarship
if total_gpa_micah/5 >= 1.3
    disp('Micah is eligible for the Orange Scholarship');
end

if total_gpa_micah/5 >= 2.2
    disp('Micah is eligible for the Blue Scholarship');
end

if c_counter_micah >= 3
    disp('Micah is eligible for the Yellow Scholarship');
end

if total_gpa_chirag/5 >= 1.3
    disp('Chirag is eligible for the Orange Scholarship');
end

if total_gpa_chirag/5 >= 2.2
    disp('Chirag is eligible for the Blue Scholarship');
end

if c_counter_chirag >= 3
    disp('Chirag is eligible for the Yellow Scholarship');
end

%define function (in percent -> out gpa)
function gpa1 = gpa(n)
    if (n >= 90) && (n <= 100)
        gpa1 = 4;
    elseif (n >= 85) && (n <= 89)
        gpa1 = 4;
    elseif (n >= 80) && (n <= 84)
        gpa1 = 3.7;
    elseif (n >= 77) && (n <= 79)
        gpa1 = 3.3;
    elseif (n >= 73) && (n <= 76)
        gpa1 = 3;
    elseif (n >= 70) && (n <= 72)
        gpa1 = 2.7;
    elseif (n >= 67) && (n <= 69)
        gpa1 = 2.3;
    elseif (n >= 63) && (n <= 66)
        gpa1 = 2;
    elseif (n >= 60) && (n <= 62)
        gpa1 = 1.7;
    elseif (n >= 57) && (n <= 59)
        gpa1 = 1.3;
    elseif (n >= 53) && (n <= 56)
        gpa1 = 1;
    elseif (n >= 50) && (n <= 52)
        gpa1 = 0.7;
    elseif (n >= 0) && (n <= 49)
        gpa1 = 0;
    else
        error('Input out of range')
    end
end
