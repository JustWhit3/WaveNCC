# Algorithm explanation

## Table of contents

- [Phisical background](#phisical-background)
- [Algorithm description](#algorithm-description)

## Phisical background

In quantum physics, a 1-dimensional [wave-function](https://en.wikipedia.org/wiki/Wave_function) <img src="https://render.githubusercontent.com/render/math?math=\color{green}{\psi_n(x, t)}"> (with *x* space-coordinate and *t* time) is a mathematical description of a quantum state of an isolate quantum system. It is a complex-valued function and a probability amplitude, and the probabilities for the possible results of measurements made on the system can be derived from it.

The [Schrödinger equation](https://users.aber.ac.uk/ruw/teach/327/hatom.php) determines how wave-function evolve over space and time.

> **NOTE**: if equations / images are not correctly displayed, this may be probably caused by Latex equation editor website maintenance. Check [here](https://latex.codecogs.com/): if the website is not displayed, server may be temporarily down for updates, so you can come back here in a few hours / days. Sorry.

In this program, the wave-function is considered as time-independent, therefore this approximation could be applied:

<img src="https://latex.codecogs.com/svg.image?\color{DarkGreen}&space;\psi(x,t)&space;\rightarrow&space;\psi(x,0)&space;=&space;\psi(x)" title="\color{DarkGreen} \psi(x,t) \rightarrow \psi(x,0) = \psi(x)" />

The **normalization condition** says that:

<img src="https://latex.codecogs.com/svg.image?\color{DarkGreen}&space;\int_{-\infty}^{\infty}&space;|&space;\psi(x)|^2&space;dx&space;=&space;1" title="\color{DarkGreen} \int_{-\infty}^{\infty} | \psi(x)|^2 dx = 1" />

it means that if the particle is measured, there is 100% probability that it will be somewhere. The set of all the possible normalizable wave-functions <img src="https://render.githubusercontent.com/render/math?math=\color{green}{\psi_n(x)}"> forms an abstract vector space, called **Hilbert space**, in which the inner product of two wave-functions of the same set is:

<img src="https://latex.codecogs.com/svg.image?\color{DarkGreen}&space;<&space;\psi_i,&space;\psi_j>&space;=&space;\int_{-\infty}^{\infty}&space;\psi^{*}_i(x)\psi_j(x)&space;dx" title="\color{DarkGreen} < \psi_i, \psi_j> = \int_{-\infty}^{\infty} \psi^{*}_i(x)\psi_j(x) dx" />

The **norm** of a given wave-function is given by:

<img src="https://latex.codecogs.com/svg.image?\color{DarkGreen}&space;<&space;\psi_i,&space;\psi_i>&space;=&space;\|\psi_i\|^2" title="\color{DarkGreen} < \psi_i, \psi_i> = \|\psi_i\|^2" />

If the norm is 1, the wave-function is normalized, then dividing by its norm, it is possible to get the normalized wave-function.

Furthermore, two wave-functions are said orthogonal if:

<img src="https://latex.codecogs.com/svg.image?\color{DarkGreen}&space;<&space;\psi_i,&space;\psi_j>&space;=&space;0" title="\color{DarkGreen} < \psi_i, \psi_j> = 0" />

and orthonormal (orthogonal and normalized) if: 

<img src="https://latex.codecogs.com/svg.image?\color{DarkGreen}&space;<&space;\psi_i,&space;\psi_j>&space;=&space;\delta_{ij}" title="\color{DarkGreen} < \psi_i, \psi_j> = \delta_{ij}" />

where the last symbol is called *Kronecker delta*.

Wave-functions orthogonality guarantees linear independence of them. In a linear combination of orthogonal wave-functions we have:

<img src="https://latex.codecogs.com/svg.image?\color{DarkGreen}&space;\psi&space;=&space;\sum_nc_n&space;\psi_n" title="\color{DarkGreen} \psi = \sum_nc_n \psi_n" />

with <img src="https://render.githubusercontent.com/render/math?math=\color{green}{c_n}"> normalization coefficients, defined as:

<img src="https://latex.codecogs.com/svg.image?\color{DarkGreen}&space;c_n&space;=&space;\dfrac{<\psi_n,\psi>}{<\psi_n,\psi_n>}" title="\color{DarkGreen} c_n = \dfrac{<\psi_n,\psi>}{<\psi_n,\psi_n>}" />

This means that for a wave-function of an orthogonal set of wave-functions holds:

<img src="https://latex.codecogs.com/svg.image?\color{DarkGreen}&space;c_n&space;=&space;\dfrac{1}{\sqrt{\|\psi_n\|}}" title="\color{DarkGreen} c_n = \dfrac{1}{\sqrt{\|\psi_n\|}}" />

## Algorithm description

The algorithm starts with an orthogonality and orthonormality check, in which the entered wave-function is considered. If the wave-function is orthogonal, the program continues, if it is orthonormal the program stops (since it is already normalized) and if it is not orthogonal it stops too, since non-orthogonal computations are not supported (for the moment).

Once the first check, the coefficients are finally computed, using the last relation of the [Algorithm description](#algorithm-description) paragraph. To compute the integral, the **Simpson 1/3 rule** has been used:

<img src="https://latex.codecogs.com/svg.image?{\color{DarkGreen}&space;\int^a_bf(x)dx&space;\approx\frac{b-a}{6}\left[&space;f(a)&space;&plus;&space;4f\left(\frac{a&plus;b}{2}&space;\right&space;)&plus;f(b)&space;\right&space;]}" title="{\color{DarkGreen} \int^a_bf(x)dx \approx\frac{b-a}{6}\left[ f(a) + 4f\left(\frac{a+b}{2} \right )+f(b) \right ]}" />

which has been extended to two-dimensions. An additional condition has been applied for the case in which one of the two extremes was infinity:

<img src="https://latex.codecogs.com/svg.image?\color{DarkGreen}&space;\int_{-\infty}^\infty&space;f(x)dx&space;=&space;\int^{\pi}_0\dfrac{f(\tan&space;u)}{\cos^2&space;u}du" title="\color{DarkGreen} \int_0^\infty f(x)dx = \int^{\pi/2}_0\dfrac{f(\tan u)}{\cos^2 u}du" />

This integral works if

<img src="https://latex.codecogs.com/svg.image?\color{DarkGreen}&space;f(\tan&space;u)\rightarrow&space;0" title="\color{DarkGreen} f(\tan u)\rightarrow 0" />

sufficielty quick as:

<img src="https://latex.codecogs.com/svg.image?\color{DarkGreen}&space;\cos^2&space;u&space;\rightarrow&space;0" title="\color{DarkGreen} \cos^2 u \rightarrow 0" />

for *u = pi/2*, otherwise is divergent.

All the computations involve the presence of complex algebra.

Once the computations are done, the final normalized wave-function (therefore the wave-function multiplied by the normalized coefficient at a given *n*) is plotted. Plots are performed in 1D if real or imaginary parts are 0, otherwise in 2D.
