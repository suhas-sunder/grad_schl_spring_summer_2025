% Author: Suhas Sunder - 100548159
% Topic: Michalewicz Function
% Assignment 1: Implementation of Eight Benchmark Functions in MATLAB and plotting 3D Map of their 2-D versions. 

clc; clear; close all

% Parameter m controls steepness and local minima
m = 10;

% Define meshgrid for clearly visible grid cells along surface of plots
% Domain x,y subset of [0, pi]
[x, y] = meshgrid(0:0.09:pi, 0:0.09:pi);

% Compute the 2D Michalewicz function
z = - (sin(x) .* (sin(x.^2 / pi)).^(2*m) + sin(y) .* (sin(2 * y.^2 / pi)).^(2*m));

% Plot
surf(x, y, z, 'EdgeColor', 'k', 'FaceColor', 'interp')
xlabel('x')
ylabel('y')
zlabel('f(x, y)')
title('Michalewicz Function')
colormap cool
view(120, 50)
grid on

% Save the currently active figure window locally as an image file
saveas(gcf, 'michalewicz_function.png')
