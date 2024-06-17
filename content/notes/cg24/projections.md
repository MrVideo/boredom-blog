---
title: 'Projections'
draft: false
type: 'page'
toc: true
mathjax: true
---

---

## Parallel projections

Parallel projections are characterised by the following matrix:

$$P = \begin{bmatrix}
{1\over w} & 0 & 0 & 0 \\\
0 & {-a\over w} & 0 & 0 \\\
0 & 0 & {1\over n- f} & {n \over n - f} \\\
0 & 0 & 0 & 1
\end{bmatrix}$$

Where:

- $w$ is the half-width of the screen
- $a$ is the aspect ratio of the screen
- $n$ is the near plane
- $f$ is the far plane

> **GLM parallel projections**
>
> GLM provides a function to obtain a parallel projection matrix from the screen parameters $l, r, b, t, n, f$:
> ```cpp
> glm::mat4 matrix = glm::ortho(l, r, b, t, n, f);
> ```
> However, since GLM is based on OpenGL, the view will be upside down. To correct it, it's sufficient to flip the obtained matrix's $y$ axis:
> ```cpp
> matrix *= glm::vec3(1, -1, 1);
> ```
> and define the following macro, to fix the difference in $z$ axis definition for Vulkan:
> ```cpp
> #define GLM_FORCE_DEPTH_ZERO_TO_ONE
> ```

### Orthogonal projection

Orthogonal projections are parallel projections where the near plane is set to zero:

$$P_\text{ort} = \begin{bmatrix}
{1\over w} & 0 & 0 & 0 \\\
0 & -{a\over w} & 0 & 0 \\\
0 & 0 & -{1\over f} & 0 \\\
0 & 0 & 0 & 1
\end{bmatrix}$$

### Axonometric projections

There are three types of axonometric projections:

- Isometric projection: all three axes are angled at 120° from one another
- Dimetric projection: they use two different angles, one for the $x$ and $z$ axes and one for the $y$ axis
- Trimetric projection: all axes are separated by different angles

All these projections are obtained by applying some rotations to the parallel projection matrix we've seen earlier.

#### Isometric projection

Isometric projections are obtained by applying a rotation of $45°$ around the $y$ axis, followed by a rotation of $35.26°$ around the $x$ axis.

![](../images/Pasted%20image%2020240420121750.png)

#### Dimetric projection

Dimetric projections are obtained by applying a rotation of $45°$ around the $y$ axis, followed by an arbitrary rotation of angle $\alpha$ around the $x$ axis.

![](../images/Pasted%20image%2020240420122112.png)

#### Trimetric projection

Trimetric projections are obtained by applying an arbitrary rotation of angle $\beta$ around the $y$ axis, followed by an arbitrary rotation of angle $\alpha$ around the $x$ axis.

![](../images/Pasted%20image%2020240420122243.png)

## Oblique projections

Oblique projections can be obtained by applying shears to the parallel projection matrix.

### Cavalier projection

The Cavalier projection is an oblique projection in which the lengths on the $z$ axis are equal to the lengths on the other axes.

It is obtained applying a shear of $45°$ and shear factor $\rho = 1$.

![](../images/Pasted%20image%2020240420122746.png)

### Cabinet projection

The Cabinet projection is an oblique projection in which the lengths on the $z$ axis are halved with respect to the lengths on the other axes.

It is obtained applying a shear of $45°$ and shear factor $\rho = 0.5$.

![](../images/Pasted%20image%2020240420122934.png)

## Perspective projections

Perspective projections can be applied through the following matrix:

$$\begin{bmatrix}
{1 \over a \cdot \tan(\theta/2)} & 0 & 0 & 0 \\\
0 & -{1\over \tan(\theta/2)} & 0 & 0 \\\
0 & 0 & {f \over n - f} & {nf \over n - f} \\\
0 & 0 & -1 & 0
\end{bmatrix}$$

$\theta$ is the so-called field of view angle.

![](../images/Pasted%20image%2020240420123235.png)

> **GLM perspective projections**
>
> GLM provides a function to obtain a projection matrix given FOV, aspect ratio, near and far planes:
> ```cpp
> glm::mat4 matrix = glm::perspective(fovy, a, n, f);
> ```
> However, since GLM is based on OpenGL, the view obtained with this function will be upside down. In order to correct this, it is sufficient to invert the $(2, 2)$ element of the obtained matrix:
> ```cpp
> matrix[1][1] *= -1;
> ```
> and define the following macro, to fix the difference in $z$ axis definition for Vulkan:
> ```cpp
> #define GLM_FORCE_DEPTH_ZERO_TO_ONE
> ```
