
### Phasor Based Techniques
- There are three. We should program at least one of those. Programming all 3 would be the best, but do at least one.

### LES Technique
- Can assume voltage waveform is a pure sine waveform whose frequency may change.
	- Vp sin(2pi f t + theta) where f is unknown.
- Since we don't know frequency, we won't know sin(2 Pi f t) and cos(2 Pi f t)
	- We need to linearize the two terms using Tailor series expansion because it is not linear.
- Don't want to use first equation when Vpcos theta is small because when dividing by a small number the overall value becomes bigger. So if there is a small amount of noise, it will get amplified.

### Iterative LES Technique
- Requires a lot of calculations.
- Done over a wide range. Not limited close to fundamental. eg. not limited to 58 to 62 Hz. 
- 