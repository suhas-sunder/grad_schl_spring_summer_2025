![](../Images/20250513202017.png)

### How to plot magnitude response and phase response on MATLAB

```
fs = 720; % Sampling frequency

T = 1/fs;

n_samples = 2;

delta_T = n_samples * T; % Delta T is the number of samples times T

f = linspace(0, fs, 1000); % Full sweep from 0 to 720 Hz

omega = 2*pi*f*T; % Angular frequency = 2πfT

% Manual frequency response for: H(f) = 1.732 - 2 * e^(j*omega*delta_T)

H = 1.732 - 2 .* exp(j * omega * delta_T);

% Plotting

figure;

subplot(2,1,1);

plot(f, abs(H), 'g', 'LineWidth', 2);

title('Magnitude Response (Real-Part Filter)');

xlabel('Frequency (Hz)');

ylabel('Magnitude');

grid on;

subplot(2,1,2);

plot(f, angle(H)*180/pi, 'r', 'LineWidth', 2);

title('Phase Response (Real-Part Filter)');

xlabel('Frequency (Hz)');

ylabel('Phase (degrees)');

grid on;
```