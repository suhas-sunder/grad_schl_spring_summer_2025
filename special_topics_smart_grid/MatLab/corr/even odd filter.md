
```
fs = 720; % Sampling frequency

n = 12; % Number of samples

d = [714, 2218, 2314, 1233, -99, -1195, -1699, -1029, 714, 2219, 2314, 1233]';

% Time vector for n samples

t = (1:n) / fs/2;

% Frequency range

f = 1:fs/2;

% Angular frequency

w = 2 * pi * f';

a = w * t;

% Basis signals

c = cos(a); % cosine basis (real part)

s = sin(a); % sine basis (imaginary part)

% Separate even and odd indices (MATLAB indexing starts at 1)

odd_idx = 1:2:n;

even_idx = 2:2:n;

d_odd = d(odd_idx);

d_even = d(even_idx);

c_odd = c(:, odd_idx);

c_even = c(:, even_idx);

s_odd = s(:, odd_idx);

s_even = s(:, even_idx);

%% --- 1) Real part of filter response (phasor1) ---

r_even_1 = c_even * d_even;

r_odd_1 = c_odd * d_odd;

i_even_1 = s_even * d_even;

i_odd_1 = s_odd * d_odd;

r1 = r_even_1 + r_odd_1;

i1 = i_even_1 + i_odd_1;

phasor1 = complex(r1, i1) * 0.5;

m1 = abs(phasor1);

p1 = unwrap(angle(phasor1)) * (180/pi);

%% --- 2) Imaginary part rotated 90° (phasor3) ---

% Swap real and imaginary parts and rotate 90°, applying same even/odd split

% Use same approach but swapped components

r_even_3 = i_even_1; % Imaginary part goes to real

r_odd_3 = i_odd_1;

i_even_3 = r_even_1; % Real part goes to imag

i_odd_3 = r_odd_1;

r3 = r_even_3 + r_odd_3;

i3 = i_even_3 + i_odd_3;

phasor3 = complex(r3, i3) * 0.5; % rotate 90°

phasor3 = phasor3 * 0.5; % additional scale as in original code

m3 = abs(phasor3) * 0.5;

p3 = unwrap(angle(phasor3)) * (180/pi) + 90 * 0.5;

%% --- 3) FIR bandpass filter and phasor estimation of filtered signal (phasor2) ---

% FIR filter

fc = 60; % Center frequency

bw = 10; % Bandwidth

b = fir1(100, [(fc/2 - bw)/(fs), (fc/2 + bw)/(fs)]); % Normalized band

filt_d = filter(b, 1, d); % Apply filter

% Separate filtered signal into even and odd samples

filt_d_odd = filt_d(odd_idx);

filt_d_even = filt_d(even_idx);

% Phasor estimation with even/odd split

r_even_2 = c_even * filt_d_even;

r_odd_2 = c_odd * filt_d_odd;

i_even_2 = s_even * filt_d_even;

i_odd_2 = s_odd * filt_d_odd;

r2 = r_even_2 + r_odd_2;

i2 = i_even_2 + i_odd_2;

phasor2 = complex(r2, i2) * 0.5;

m2 = abs(phasor2) * 0.5;

p2 = unwrap(angle(phasor2)) * (180/pi) * 0.5;

%% ----------- Plot 1: Real Filter Response -----------

figure;

subplot(2,1,1);

plot(f, m1, 'b');

xlabel('Frequency (Hz)');

ylabel('Magnitude');

title('Real Filter Component - Magnitude Response (Even/Odd split)');

xlim([1 fs/2]);

grid on;

subplot(2,1,2);

plot(f, p1, 'r');

xlabel('Frequency (Hz)');

ylabel('Phase (degrees)');

title('Real Filter Component - Phase Response (Even/Odd split)');

xlim([1 fs/2]);

grid on;

%% ----------- Plot 2: Imaginary Filter Response -----------

figure;

subplot(2,1,1);

plot(f, m3, 'b');

xlabel('Frequency (Hz)');

ylabel('Magnitude');

title('Imaginary Filter Component - Magnitude Response (Even/Odd split)');

xlim([1 fs/2]);

grid on;

subplot(2,1,2);

plot(f, p3, 'r');

xlabel('Frequency (Hz)');

ylabel('Phase (degrees)');

title('Imaginary Filter Component - Phase Response (Even/Odd split)');

xlim([1 fs/2]);

grid on;

%% ----------- Plot 3: Filtered Signal Phasor -----------

figure;

subplot(2,1,1);

plot(f, m2, 'm');

xlabel('Frequency (Hz)');

ylabel('Magnitude');

title('Filtered Signal - Magnitude Response (Even/Odd split)');

xlim([1 fs/2]);

grid on;

subplot(2,1,2);

plot(f, p2, 'k');

xlabel('Frequency (Hz)');

ylabel('Phase (degrees)');

title('Filtered Signal - Phase Response (Even/Odd split)');

xlim([1 fs/2]);

grid on;
```