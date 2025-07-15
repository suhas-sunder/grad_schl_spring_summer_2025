% Author: Suhas Sunder - 100548159
% Topic: Ackley Function
% Assignment 1: Implementation of Eight Benchmark Functions in MATLAB and plotting 3D Map of their 2-D versions. 

clc; clear; close all

% Define meshgrid for clearly visible grid cells along surface of plots
[x, y] = meshgrid(-10:0.25:10, -10:0.25:10);

% Compute Ackley function
z = -20 * exp(-0.2 * sqrt(0.5 * (x.^2 + y.^2))) ...
    - exp(0.5 * (cos(2*pi*x) + cos(2*pi*y))) + 20 + exp(1);

% Plot: surface with black mesh + smooth shading
surf(x, y, z, 'EdgeColor', 'k', 'FaceColor', 'interp')
xlabel('x')
ylabel('y')
zlabel('f(x, y)')
title('Ackley Function')
colormap cool
view(-120, 30)
grid on

% Save the currently active figure window locally as an image file
saveas(gcf, 'ackley_function.png')
