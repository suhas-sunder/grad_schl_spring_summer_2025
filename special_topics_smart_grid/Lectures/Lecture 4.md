
### Gilbert and SHovling Algorithm
- Not a digital filter
	- Vp is non-linear
	- Also, we're multiplying coefficients V- and V+
	- Nonlinear eqn because we have v0^2 and V+ times V-
- Doing a fourier analysis of decaying DC component, it will show that it contains DC and many low frequencies. Doesn't contain many high frequencies. This filter eliminates DC components but doesn't do well eliminating lower frequencies. Therefore, there is some oscillation because of the decaiying dc component on the magnitude plot.
- Mann and morrison is a filter that does a good job of filtering lower frequencies.

### Assignment 1:
- 1 hour will be done in class. It will be submitted in class. If anything is left over, it will be completed at home and submitted later.
- Can give a different sampling frequency and frequency response.


### Correlation Algorithms
- Will have a better frequency response than Trig Algos, but will require more samples and calculations.
- What is correlation? We are seeing how close a signal is to a reference signal.
	- We can do that by correlating both signals.
	- When correlating, you multiply both signals and integrate over time.
	- Whatever value you get, will give you an indication of how close both signals are.
- Correlation is multiplication and integration over one period.
- Cannot have a different frequency omega. Omega must be the same as the reference frequency. So if your interested in 60Hz, reference waveform must also be 60Hz for both sin and cos.
- Always integrate over one cycle. There is a reason for this which prof will explain later.
- Orthogonal waveforms are those that are 90 degrees apart. To check if the waveforms are orthogonal, multiply them and integrate by one period. If the integral is 0, then it is orthogonal.
- If sampling rate is 8000 for 60Hz, you can't use it because 8000/60 produces a decimal value 133.33... So, the sampling frequency chosen must produce a whole number when divided by the frequency.