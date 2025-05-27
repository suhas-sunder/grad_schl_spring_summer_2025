
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

% ----- Real part of filter response -----

r1 = (c / 2) * d;

i1 = (s * d); % unchanged

phasor1 = complex(r1, i1) * 0.5;

% ----- Imaginary part of filter response (rotated 90°) -----

phasor3 = complex(i1, r1) * 0.5; % swap real/imag and rotate 90°

phasor3 = phasor3 * 0.5;

% ----- Magnitude and Phase of real part -----

m1 = abs(phasor1);

p1 = unwrap(angle(phasor1)) * (180/pi);

% ----- Magnitude and Phase of imaginary part -----

m3 = abs(phasor3) * 0.5;

p3 = unwrap(angle(phasor3)) * (180/pi) + 90 * 0.5;

% ----- FIR bandpass filter applied to input signal -----

fc = 60; % Center frequency

bw = 10; % Bandwidth

b = fir1(100, [(fc/2 - bw)/(fs), (fc/2 + bw)/(fs)]); % Normalized band

filt_d = filter(b, 1, d); % Apply filter

% ----- Phasor estimation of filtered signal -----

r2 = (c * filt_d);

i2 = (s * filt_d) / (n / 2);

phasor2 = complex(r2, i2) * 0.5;

m2 = abs(phasor2) * 0.5;

p2 = unwrap(angle(phasor2)) * (180/pi) * 0.5;

% ----------- Plot 1: Real Filter Response -----------

figure;

subplot(2,1,1);

plot(f, m1, 'b');

xlabel('Frequency (Hz)');

ylabel('Magnitude');

title('Real Filter Component - Magnitude Response');

xlim([1 fs/2]);

grid on;

subplot(2,1,2);

plot(f, p1, 'r');

xlabel('Frequency (Hz)');

ylabel('Phase (degrees)');

title('Real Filter Component - Phase Response');

xlim([1 fs/2]);

grid on;

% ----------- Plot 2: Imaginary Filter Response -----------

figure;

subplot(2,1,1);

plot(f, m3, 'b');

xlabel('Frequency (Hz)');

ylabel('Magnitude');

title('Imaginary Filter Component - Magnitude Response');

xlim([1 fs/2]);

grid on;

subplot(2,1,2);

plot(f, p3, 'r');

xlabel('Frequency (Hz)');

ylabel('Phase (degrees)');

title('Imaginary Filter Component - Phase Response');

xlim([1 fs/2]);

grid on;

% ----------- Plot 3: Input Signal Passed Through Filter -----------

figure;

subplot(2,1,1);

plot(f, m2, 'm');

xlabel('Frequency (Hz)');

ylabel('Magnitude');

title('Filtered Signal - Magnitude Response');

xlim([1 fs/2]);

grid on;

subplot(2,1,2);

plot(f, p2, 'k');

xlabel('Frequency (Hz)');

ylabel('Phase (degrees)');

title('Filtered Signal - Phase Response');

xlim([1 fs/2]);

grid on;
```