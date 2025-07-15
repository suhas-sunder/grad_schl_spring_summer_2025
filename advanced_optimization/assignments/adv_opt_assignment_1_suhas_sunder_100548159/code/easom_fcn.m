% Author: Suhas Sunder - 100548159
% Topic: Easom Function
% Assignment 1: Implementation of Eight Benchmark Functions in MATLAB and plotting 3D Map of their 2-D versions. 

clc; clear; close all

% Define meshgrid for clearly visible grid cells along surface of plots
[x, y] = meshgrid(-6:0.5:6, -6:0.5:6);

z = -cos(x) .* cos(y) .* exp(-((x - pi).^2 + (y - pi).^2));

% Limit z-axis to make peak visible and avoid "black top"
z(z > 0) = 0;  % Cap the top flat regions to 0

% Plot
surf(x, y, z, 'EdgeColor', 'k', 'FaceColor', 'interp')
xlabel('x')
ylabel('y')
zlabel('f(x, y)')
title('Easom Function')
colormap cool
view(-195, 30)
grid on
zlim([-1.1 0.1])

% Save the currently active figure window locally as an image file
saveas(gcf, 'easom_function.png')
