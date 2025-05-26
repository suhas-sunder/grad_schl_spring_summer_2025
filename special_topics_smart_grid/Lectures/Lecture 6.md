
### Least Error Square Algo
- Start with simple model with pure sine with single frequency. Finding the real and imaginary parts.
- Left pseudo offline of A can be done before hand. Don't need to calculate this every time.
- v = Vpsin(wt)cos(theta) + Vp cos(wt)sin(theta)
	- If we know frequency and time, we can calculate cos(theta) and sin(theta) which makes up our matrix A (the known).
- **Make sure we can vary delta T, number of samples (window length), time reference (location of V0), the model itself (determines the unknowns) in matlab code**
- num rows = num of columns
- num samples (window) = num of rows
- Smaller the coefficients, the better the frequency response (general rule). Still have to do freq response, but it's a good indicator. Coefficients meaning the values in front of V0, V1, V2, etc.

### Frequency Lecture
- Why do we want to measure frequency?
	- 1) If there isn't a balanced between frequency and load, you will be kicked out of the system. This is one reason, is to keep it within limits. For Canada it's 60Hz.
	- 2) What happens to phasors if you change the waveform to 69Hz? The peak value.
		- If we do 59 Hz, the peak  values will oscillate. If it drifts too much then it's a big issue.
	- 3) Proacting Equipment, generators, transformers etc.
	- 4) Use it for controlling sampling rate. This is where the problem happens. 
		- eg. with DFT designed for 59Hz for 720Hz sampling rate. If we use 59Hz instead, we won't get perfect 12 samples because 12 x 59 is less than 720Hz.
	- It may sound simple, measuring freq, but it's not. We are trying to measure between 60 plus and minus 0.005 Hz.
- Frequency is always estimated from the voltage signals.
- There are numerical algorithms that will obviously affected by signal pollution, sinusoidal, or if the frequency is changing rapidly. The algorithm needs to be able to handle this.
- Principals of estimation include two main for estimating frequency
	- Zero crossing (old method)
	- Phasor based techniques (We still calculate phasors, but from phasors we estimate frequency.)
- Wed June 4th will be Least Error Square 

### Zero Crossing Method
- 