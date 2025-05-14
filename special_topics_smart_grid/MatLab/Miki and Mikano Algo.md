![](../Images/20250513202017.png)

### How to plot magnitude response and phase response on MATLAB

```
% --- Example Signal Data ---
fs = 1000;               % Sampling frequency in Hz
f0 = 60;                 % Signal frequency in Hz
T = 1/fs;                % Sampling period
t = 0:T:0.1;             % Time vector
v = sin(2*pi*f0*t);      % Example signal (replace with your real data)

% --- Initialize Variables ---
omega = 2*pi*f0;         % Angular frequency
Vp_mag = zeros(size(t));
Vp_angle = zeros(size(t));

% --- Loop Over Data Points Starting from Second Sample ---
for n = 2:length(t)
    v0 = v(n);           % Current sample
    v_minus1 = v(n-1);   % Previous sample
    
    % Apply Miki and Mikano Algorithm
    Imag_part = v0;   % Equation 1.1: Vp*sin(theta) = v0
    Real_part = (v0*cos(omega*T) - v_minus1) / sin(omega*T); % Equation 1.3

    Vp_mag(n) = sqrt(Imag_part^2 + Real_part^2);
    Vp_angle(n) = atan2(Imag_part, Real_part); % Use atan2 for correct angle
end

% --- Plot Magnitude and Phase ---
figure;

subplot(2,1,1);
plot(t, Vp_mag, 'b', 'LineWidth', 2);
title('Estimated Magnitude of V_p');
xlabel('Time (s)');
ylabel('|V_p|');
grid on;

subplot(2,1,2);
plot(t, rad2deg(Vp_angle), 'r', 'LineWidth', 2);
title('Estimated Phase of V_p');
xlabel('Time (s)');
ylabel('Phase (degrees)');
grid on;

```

```
% Parameters
fs = 1000;                        % Sampling frequency
T = 1/fs;
f = linspace(1, fs/2, 1000);      % Frequency sweep from 1 Hz to Nyquist
omega = 2*pi*f;

% Allocate response
H = zeros(size(f));

% Compute magnitude and phase at each frequency
for k = 1:length(omega)
    w = omega(k);
    num = [cos(w*T), -1];
    den = sin(w*T);
    H(k) = (num(1)*exp(-1j*0*w*T) + num(2)*exp(-1j*1*w*T)) / den; % DTFT
end

% Plot
figure;

subplot(2,1,1);
plot(f, abs(H), 'g', 'LineWidth', 2);
title('Magnitude Response of Real-Part Filter');
xlabel('Frequency (Hz)');
ylabel('Magnitude');
grid on;

subplot(2,1,2);
plot(f, angle(H)*180/pi, 'r', 'LineWidth', 2);
title('Phase Response of Real-Part Filter');
xlabel('Frequency (Hz)');
ylabel('Phase (degrees)');
grid on;

```

``` 
fs = 720;                         % Sampling frequency
b = [1.732, -2];                  % Filter coefficients from lecture
a = 1;                            % FIR filter => no denominator

[H, f] = freqz(b, a, 1024, fs);   % Compute frequency response

% Plot
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