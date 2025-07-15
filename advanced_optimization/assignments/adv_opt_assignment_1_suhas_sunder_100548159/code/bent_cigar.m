% Author: Suhas Sunder - 100548159
% Topic: Bent Cigar Function 
% Assignment 1: Implementation of Eight Benchmark Functions in MATLAB and plotting 3D Map of their 2-D versions. 

clc; clear; close all

% Define meshgrid for clearly visible grid cells along surface of plots
[x, y] = meshgrid(-5:0.5:5, -5:0.5:5);

% Function
z = x.^2 + 1e6 * y.^2;

% Plot
surf(x, y, z, 'EdgeColor', 'k', 'FaceColor', 'interp')
xlabel('x')
ylabel('y')
zlabel('f(x, y)')
title('Bent Cigar Function')
colormap cool
view(45, 30)
grid on

% Save the currently active figure window locally as an image file
saveas(gcf, 'bent_cigar_function.png')
