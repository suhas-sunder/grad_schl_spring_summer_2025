% Author: Suhas Sunder - 100548159
% Topic: Rosenbrock Function (Valley)
% Assignment 1: Implementation of Eight Benchmark Functions in MATLAB and plotting 3D Map of their 2-D versions. 

clc; clear; close all

% Define meshgrid for clearly visible grid cells along surface of plots
[x, y] = meshgrid(-2:0.1:2, -1:0.1:3); 

% Compute the 2D Rosenbrock function
z = 100 * (y - x.^2).^2 + (x - 1).^2;

% Plot the surface with mesh
surf(x, y, z, 'EdgeColor', 'k', 'FaceColor', 'interp')
xlabel('x')
ylabel('y')
zlabel('f(x, y)')
title('Rosenbrock Function')
colormap cool
view(130, 30)  % Adjusted to match lecture-style perspective
grid on

% Save the currently active figure window locally as an image file
saveas(gcf, 'rosenbrock_function.png')
