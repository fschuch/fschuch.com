---
title: "Sandbox flow configuration: A rapid prototyping tool inside XCompact3d"
summary: ""
authors: []
tags: []
categories: []
date: "2019-02-05T00:00:00Z"
slides:
  # Choose a theme from https://github.com/hakimel/reveal.js#theming
  theme: simple
  # Choose a code highlighting style (if highlighting enabled in `params.toml`)
  #   Light style: github. Dark style: dracula (default).
  highlight_style: atom-one-light
---

### Sandbox flow configuration: A rapid prototyping tool inside XCompact3d

<div class="animations">
  <img alt="Flow Visualization with Passive Scalar Field" width="50%" height=auto src="square.gif" >
</div>

**Felipe N. Schuch**_, LaSET, School of Technology, PUCRS._

<img alt="" height="90px" width=auto src="logo.laset.png" style="background:none; border:none; box-shadow:none;">
<img alt="" height="90px" width=auto src="technology-267x90.png" style="background:none; border:none; box-shadow:none;">

---

# Motivation

{{< speaker_note >}}
- There are two main points motivating this work
{{< /speaker_note >}}

---

### How can we speed up our workflow?

![alt text](https://mermaid.ink/svg/eyJjb2RlIjoiZmxvd2NoYXJ0IFJMXG4gICAgSChbSHlwb3RoZXNpc10pIC0tPiBFeHBlcmltZW50c1xuICAgIHN1YmdyYXBoIEV4cGVyaW1lbnRzXG4gICAgICAgIENvZGUgLS0-IENvbXBpbGUgLS0-IERlYnVnIC0tPiBSdW4gLS0-IENvZGVcbiAgICBlbmRcbiAgICBFeHBlcmltZW50cyAtLT4gUihbUmVzdWx0c10pXG4gICAgUiAtLT4gQyhbQ29uY2x1c2lvbnNdKVxuICAgIEMgLS0-IEhcbiIsIm1lcm1haWQiOnsidGhlbWUiOiJiYXNlIiwidGhlbWVWYXJpYWJsZXMiOnsiZm9udEZhbWlseSI6ImFyaWFsIiwiZm9udFNpemUiOiIyMHB4In19LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ)

{{< speaker_note >}}
The first is:
- How can we speed up our workflow;
- I mean, the iterations in the scientific process.
{{< /speaker_note >}}

---

### Can we improve the learning curve for beginners in our code?

{{< speaker_note >}}
and second:
- Can we improve the learning curve for beginners in our code?
- And especially, how to help them to **code new** flow configurations, going beyond the benchmark cases.
{{< /speaker_note >}}

---

### Identifying the main challenges

- Using parallel computation in a distributed-memory system and Message Passing Interface;

<img alt="" height="85%" width=auto src="2d_decomp.png">

<small> _Illustration of the 2D domain decomposition from [2DECOMP&FFT](http://www.2decomp.org/decomp.html)._ </small>

- Coding, compiling, testing, debugging and handling I/O in Fortran.


---

# Methodology

---

Sandbox Flow Configuration ([BC-Sandbox.f90](https://github.com/fschuch/Xcompact3d/blob/master/src/BC-Sandbox.f90))

![alt text](mermaid-diagram-20210310173223.svg)


- The entire initial set-up for any given flow configuration can be imported from external files;
- XCompact3d can be compiled just once.
<!-- - There is no need to worry about parallel computation in a distributed-memory system and Message Passing Interface (MPI). -->

---

### External Tool

![alt text](mermaid-diagram-20210310111106.svg)


- The choice is up to the user:
  - Fortran (in Shared-Memory Architecture);
  - Matlab/Octave;
  - Python with just [Numpy](https://numpy.org/) or more specific tools ([Py4Incompact3D ](https://github.com/xcompact3d/Py4Incompact3D) or [Xcompact3d-toolbox](https://github.com/fschuch/xcompact3d_toolbox));
- It adds no extra dependency to the workflow.

---

### Variables handled by `Sandbox`

- Initial condition for velocity and scalar field(s);
- Inflow profiles for velocity and scalar field(s) (if `nclx1=nclxS1=2`);
- Top and bottom boundary values for scalar field(s) (if `ncly1=2` or `nclySn=2`);
- Customized operator for the imposition of constant flow rate (if `nclx1=nclxn=0`);
- $\epsilon$ array, describing the solid geometry for IBM (if `iibm $\ne$ 0`).

<small>See [README](https://github.com/fschuch/Xcompact3d/blob/master/examples/Sandbox/README.md) for more details.</small>

---

### An example using Python and Numpy

```python
import numpy as np

ux = np.zeros(shape=(nx, ny, nz), dtype=np.float64)
uy = np.zeros_like(ux)
uz = np.zeros_like(ux)
phi = np.zeros(shape=(nx, ny, nz, numscalar), dtype=np.float64)

# Sequence of operations to set the initial condition

ux.T.tofile('./data/ux.bin')
uy.T.tofile('./data/uy.bin')
uz.T.tofile('./data/uz.bin')
for n in range(numscalar):
    phi[:,:,:,n].T.tofile('./data/phi{}.bin'.format(n+1))
```

---

### Cases Covered by `Sandbox`

| Case | IC | BC | FRC | IBM | LMN |
| ---- |:--:|:--:|:---:|:----|:---:|
| Channel-Flow | :heavy_check_mark: | | :heavy_check_mark: | | |
| Cylinder | :heavy_check_mark: |  :heavy_check_mark: | |  :heavy_check_mark: | |
| Lock-exchange | :heavy_check_mark: | :heavy_check_mark: | | | :warning: |
| Periodic Hill | :heavy_check_mark: | | :heavy_check_mark: | :heavy_check_mark: | |
| Taylor–Green vortex | :heavy_check_mark: | | | | |
| TBL | :heavy_check_mark: | :warning: | :warning: | | |

<small>**Note**: Initial Condition (**IC**); Boundary Conditions (**BC**); Flow rate Control (**FRC**); Immersed Boundary Method (**IBM**); Low Mach Number (**LMN**).</small>

<!-- ---

### It supports Initial Condition

| Filename    | Shape | Demanded |
| ----------- | ------| -------- |
| `ux.bin`    | (nx, ny, nz) | always |
| `uy.bin`    | (nx, ny, nz) | always |
| `uz.bin`    | (nx, ny, nz) | always |
| `phi<n>.bin` | (nx, ny, nz) | `numscalar $>$ 0` |

---

### It supports Boundary Condition

| Filename    | Shape | Demanded |
| ----------- | ------| -------- |
| `bxx1.bin` | (ny, nz) | `nclx1=2` |
| `bxy1.bin` | (ny, nz) | `nclx1=2` |
| `bxz1.bin` | (ny, nz) | `nclx1=2` |
| `bxphi1<n>.bin` | (ny, nz) | `nclxS1=2` |
| `byphi1<n>.bin` | (nx, nz) | `nclyS1=2` |
| `byphin<n>.bin` | (nx, nz) | `nclySn=2` |



---

### It supports other arrays

| Filename    | Description | Demanded |
| ----------- | ----------- | -------- |
| `geometry.bin` | $\epsilon$ array set to 1 inside the solid and zero otherwise | `iibm $\ne$ 0` |
| `vol_frc.bin` | Customized operator to impose constant flow rate | `nclx1=nclxn=0` |

--- -->

---

# Case Study

---

### Periodic Heat Exchanger

<img alt="Flow Visualization with Passive Scalar Field" width="35%" height=auto src="Heat-exchanger.jpg">

- Periodic boundary conditions in x and z;
- A cylinder at the center with low temperature;
- No-slip conditions for velocity at top and bottom, besides, high temperature at the walls.

---

### Initialization

```python
>>> import xcompact3d_toolbox as x3d
>>> import xcompact3d_toolbox.sandbox
>>> prm = x3d.Parameters(loadfile='input.i3d')
>>> dataset = x3d.sandbox.init_dataset(prm)
>>> dataset
```
```text
<xarray.Dataset>
Dimensions:  (n: 1, x: 128, y: 129, z: 8)
Coordinates:
  * x        (x) float64 0.0 0.04688 0.09375 0.1406 ... 5.812 5.859 5.906 5.953
  * y        (y) float64 0.0 0.04688 0.09375 0.1406 ... 5.859 5.906 5.953 6.0
  * z        (z) float64 0.0 0.04688 0.09375 0.1406 0.1875 0.2344 0.2812 0.3281
  * n        (n) int32 0
Data variables:
    byphi1   (n, x, z) float64 0.0 0.0 0.0 0.0 0.0 0.0 ... 0.0 0.0 0.0 0.0 0.0
    byphin   (n, x, z) float64 0.0 0.0 0.0 0.0 0.0 0.0 ... 0.0 0.0 0.0 0.0 0.0
    ux       (x, y, z) float64 0.0 0.0 0.0 0.0 0.0 0.0 ... 0.0 0.0 0.0 0.0 0.0
    uy       (x, y, z) float64 0.0 0.0 0.0 0.0 0.0 0.0 ... 0.0 0.0 0.0 0.0 0.0
    uz       (x, y, z) float64 0.0 0.0 0.0 0.0 0.0 0.0 ... 0.0 0.0 0.0 0.0 0.0
    phi      (n, x, y, z) float64 0.0 0.0 0.0 0.0 0.0 ... 0.0 0.0 0.0 0.0 0.0
    vol_frc  (x, y, z) float64 0.0 0.0 0.0 0.0 0.0 0.0 ... 0.0 0.0 0.0 0.0 0.0
```

---

### Boundary Conditions

High temperature at the bottom and top walls:

$$
\Theta(x,y=0,z,t) = 1
$$

$$
\Theta(x,y=L_y,z,t) = 1
$$

```python
>>> dataset["byphi1"] += 1
>>> dataset["byphin"] += 1
```

---

### Initial Condition

<img alt="" width="40%" height=auto src="vertical_vel_prot.svg">

```python
>>> dataset["ux"] += velocity_profile + random_noise
>>> dataset["uy"] += random_noise
>>> dataset["uz"] += random_noise
>>> dataset["phi"] += 1.0
```

<small>**Note:** Part of the code was not presented, for simplicity.</small>

---

### Geometry

```python
>>> epsi = x3d.sandbox.init_epsi(prm)
>>> for array in epsi.values():
...     array = array.geo.cylinder(x=prm.xlx / 2.0, y=prm.yly / 2.0)
...
>>> epsi["epsi"].isel(z=0).plot()
```

<img alt="" width="40%" height=auto src="epsi.jpg">

---

### Flow rate Control

```python
>>> dataset["vol_frc"] += prm.dy / prm.yly / prm.nx / prm.nz
>>> dataset["vol_frc"][dict(y=0)] *= 0.5
>>> dataset["vol_frc"][dict(y=-1)] *= 0.5
>>> dataset["vol_frc"] = dataset.vol_frc.where(epsi == False, 0.0)
>>> dataset.vol_frc.isel(z=0).plot()
```

<img alt="" width="40%" height=auto src="frc.jpg">

---

- Now we save the arrays in the disk:

```python
>>> dataset.x3d.write(prm)
>>> x3d.gene_epsi_3D(epsi, prm)
```

- End run the simulation:

```bash
mpirun -n [number of cores] ./xcompact3d |tee log.out
```

- There is no need to recompile the code every time;
- We can code, test, plot and debug the initial set-up interactively in Jupyter (or any other tool).

---


Periodic Heat Exchanger

<div class="animations">
  <img alt="Flow Visualization with Passive Scalar Field" width="50%" height=auto src="heat.gif">
</div> 

<small>[View the code online](https://xcompact3d-toolbox.readthedocs.io/en/latest/examples/Heat-exchanger.html).</small>

---

<div class="animations">
  <img alt="Flow Visualization with Passive Scalar Field" width="100%" height=auto src="axisymmetric.gif">
</div> 

<small>[View the code online](https://xcompact3d-toolbox.readthedocs.io/en/latest/examples/Axisymmetric_flow.html).</small>

---

<div class="animations">
  <img alt="Flow Visualization with Passive Scalar Field" width="100%" height=auto src="square.gif">
</div> 

<small>[View the code online](https://xcompact3d-toolbox.readthedocs.io/en/latest/examples/Square.html).</small>

---

# Bonus

---

User Interface with IPywidgets ([try it online](https://xcompact3d-toolbox.readthedocs.io/en/latest/tutorial/parameters.html#))

<div class="animations">
  <img alt="Flow Visualization with Passive Scalar Field" width="100%" height=auto src="Output.gif">
</div> 

<!-- <small>[Try it online](https://xcompact3d-toolbox.readthedocs.io/en/latest/tutorial/parameters.html#).</small> -->

---

# Conclusion

---

### The outcome of this work benefits users from different levels:

- **For students in CFD**, it provides **direct hands-on experience** and a safe place for practising and learning;
- **For advanced users** and code developers, it works as a **rapid prototyping tool**;
- Furthermore, it is a useful advance in terms of **research reproducibility**.

---

# Questions?

> <small>**Felipe N. Schuch**, LaSET, School of Technology, PUCRS.<br></small>
> <small>:house: [fschuch.com](www.fschuch.com/en) :envelope: felipe.schuch@edu.pucrs.br</small>