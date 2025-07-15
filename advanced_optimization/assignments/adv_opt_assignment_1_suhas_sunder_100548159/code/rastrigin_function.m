% Author: Suhas Sunder - 100548159
% Topic: Rastrigin Function
% Assignment 1: Implementation of Eight Benchmark Functions in MATLAB and plotting 3D Map of their 2-D versions. 

clc; clear; close all

% Define meshgrid for clearly visible grid cells along surface of plots
[x, y] = meshgrid(-5:0.1:5, -5:0.1:5);

% Compute the Rastrigin function in 2D
z = 20 + x.^2 + y.^2 - 10 * (cos(2*pi*x) + cos(2*pi*y));

% Plot the surface
surf(x, y, z, 'EdgeColor', 'k', 'FaceColor', 'interp')
xlabel('x')
ylabel('y')
zlabel('f(x, y)')
title('Rastrigin Function')
colormap cool
view(-120, 60)
grid on

% Save the currently active figure window locally as an image file
saveas(gcf, 'rastrigin_function.png')
