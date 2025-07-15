% Author: Suhas Sunder - 100548159
% Topic: Schaffer Function N.6
% Assignment 1: Implementation of Eight Benchmark Functions in MATLAB and plotting 3D Map of their 2-D versions. 

clc; clear; close all

% Define meshgrid for clearly visible grid cells along surface of plots
[x, y] = meshgrid(-10:0.75:10, -10:0.75:10);

% Compute Schaffer N.6
r = sqrt(x.^2 + y.^2);
z = 0.5 + (sin(r).^2 - 0.5) ./ (1 + 0.001*(x.^2 + y.^2)).^2;

% Plot
surf(x, y, z, 'EdgeColor', 'k', 'FaceColor', 'interp')
xlabel('x')
ylabel('y')
zlabel('f(x, y)')
title('Schaffer Function N.6')
colormap cool
view(-45, 80)
grid on

% Save the currently active figure window locally as an image file
saveas(gcf, 'schaffer_n6_function.png')
