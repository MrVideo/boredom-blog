---
title: '3D transformations'
draft: false
type: 'page'
toc: true
mathjax: true
---

---

## Translation

When translating an object with coordinates $(x,y,z)$ by a set of distances $(d_x,d_y,d_z)$, the following transformation matrix can be applied:

$$T(d_x,d_y,d_z) = \begin{bmatrix}
1 & 0 & 0 & d_x \\\
0 & 1 & 0 & d_y \\\
0 & 0 & 1 & d_z \\\
0 & 0 & 0 & 1
\end{bmatrix}$$

## Scaling

Scaling modifies the size of an object and can be used to obtain several effects:

- Enlarge
- Shrink
- Deform
- Mirror
- Flatten

All scaling transformations have a center: a point that is not moved during the transformation.

It's possible to scale an object by factors $(s_x, s_y, s_z)$ using the following transformation matrix:

$$S(s_x,s_y,s_z) = \begin{bmatrix}
s_x & 0 & 0 & 0 \\\
0 & s_y & 0 & 0 \\\
0 & 0 & s_z & 0 \\\
0 & 0 & 0 & 1
\end{bmatrix}$$

### Mirroring

Three types of mirroring can be achieved:

- **Planar** mirroring: it creates a symmetric object with respect to a plane
- **Axial** mirroring: it creates a symmetric object with respect to one of the three axes
- **Central** mirroring: it creates a symmetric object with respect to a single point in space

We can obtain all of the above by setting the scaling factors to -1 for one, two or three directions respectively: for planar mirroring:

$$S = \begin{bmatrix}
-1 & 0 & 0 & 0 \\\
0 & 1 & 0 & 0 \\\
0 & 0 & 1 & 0 \\\
0 & 0 & 0 & 1
\end{bmatrix}$$

For axial mirroring:

$$S = \begin{bmatrix}
-1 & 0 & 0 & 0 \\\
0 & -1 & 0 & 0 \\\
0 & 0 & 1 & 0 \\\
0 & 0 & 0 & 1
\end{bmatrix}$$

For central mirroring:

$$S = \begin{bmatrix}
-1 & 0 & 0 & 0 \\\
0 & -1 & 0 & 0 \\\
0 & 0 & -1 & 0 \\\
0 & 0 & 0 & 1
\end{bmatrix}$$

### Flattening

Setting a scaling factor of zero in any of the three directions flattens the object along that axis, projecting it into two dimensions.

## Rotation

A rotations varies the orientation of an object while maintaining its size and position.

A rotation is always made along one axis: a line in which all points are subject to no transformation.

Rotations along the various axes are applied by using the following transformation matrices:

$$\begin{aligned}
R_x(\alpha) &= \begin{bmatrix}
1 & 0 & 0 & 0 \\\
0 & \cos\alpha & -\sin\alpha & 0 \\\
0 & \sin\alpha & \cos\alpha & 0 \\\
0 & 0 & 0 & 1
\end{bmatrix}\\\\\
R_y(\alpha) &= \begin{bmatrix}
\cos\alpha & 0 & \sin\alpha & 0 \\\
0 & 1 & 0 & 0 \\\
-\sin\alpha & 0 & \cos\alpha & 0 \\\
0 & 0 & 0 & 1
\end{bmatrix}\\\\\
R_z(\alpha) &= \begin{bmatrix}
\cos\alpha & -\sin\alpha & 0 & 0 \\\
\sin\alpha & \cos\alpha & 0 & 0 \\\
0 & 0 & 1 & 0 \\\
0 & 0 & 0 & 1
\end{bmatrix}
\end{aligned}$$

## Shear

A shear transform bends an object in one direction.

A shear is performed along an axis and has a center. As the value of the axis on which the shear is performed increases, the object is linearly bent into the direction specified by a bidimensional vector.

A shear can be performed by applying the following transformation matrices:

$$\begin{aligned}
H_x(h_y,h_z) &= \begin{bmatrix}
1 & 0 & 0 & 0 \\\
h_y & 1 & 0 & 0 \\\
h_z & 0 & 1 & 0 \\\
0 & 0 & 0 & 1
\end{bmatrix}\\\\\
H_y(h_x,h_z) &= \begin{bmatrix}
1 & h_x & 0 & 0 \\\
0 & 1 & 0 & 0 \\\
0 & h_z & 1 & 0 \\\
0 & 0 & 0 & 1
\end{bmatrix}\\\\\
H_z(h_x,h_y) &= \begin{bmatrix}
1 & 0 & h_x & 0 \\\
0 & 1 & h_y & 0 \\\
0 & 0 & 1 & 0 \\\
0 & 0 & 0 & 1
\end{bmatrix}\\\\\
\end{aligned}$$
