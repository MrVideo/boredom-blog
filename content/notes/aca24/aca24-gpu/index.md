---
title: 'Graphics Processing Units'
draft: false
type: 'page'
toc: true
mathjax: true
---

---

For a price[^1], anyone can buy a GPU with hundreds of parallel floating-point units, which makes high-performance computing more accessible. The interest in GPU computing was born when this potential was combined with a programming language that made GPUs easier to program. Hence, many programmers of scientific and multimedia applications today are pondering whether to use GPUs or CPUs.

GPUs and CPUs do not go back in computer architecture genealogy to a common ancestor; there is no *missing link* that explains both. The primary ancestors of GPUs are **graphics accelerators**, as doing graphics well is the reason why GPUs exist.

While GPUs are moving towards mainstream computing, they can’t abandon their responsibility to continue to excel at graphics. Thus, the design of GPUs may make more sense when architects ask, given the hardware invested to do graphics well, how can we supplement it to improve the performance of a wider range of applications?

## Programming the GPU

The challenge for the GPU programmer is not simply getting good performance on the GPU, but also in coordinating the scheduling of the computation on the system processor and the GPU and the transfer of data between system memory and GPU memory. Moreover, GPUs have virtually **every type of parallelism** that can be captured by the programming environment: [multithreading](../aca24-multithreading), [MIMD](../aca24-parallelism#parallel-architectures), [SIMD](../aca24-parallelism#parallel-architectures) and even [instruction-level](../aca24-ilp).

### CUDA

NVIDIA decided to develop a C-like language and programming environment that would improve the productivity of GPU programmers by attacking both the challenges of heterogeneous computing and of multifaceted parallelism.

The name of their system is [CUDA](https://en.wikipedia.org/wiki/CUDA), for *Compute Unified Device Architecture*. Using this lowest level of parallelism as the programming primitive, the compiler and the hardware can gang thousands of CUDA threads together to utilise the various styles of parallelism within a GPU. Hence, NVIDIA classifies the CUDA programming model as *Single Instruction, Multiple Thread* or **SIMT**. For reasons we’ll see briefly, these threads are blocked together and executed in groups of thirty-two. We call the hardware that executes a whole block of threads a **multithreaded SIMD processor**.

We need just a few details before we can give an example of a CUDA program:

- To distinguish between functions for the GPU and for the system processor, CUDA uses keywords such as `__device__` or `__global__` for the former and `__host__` for the latter.
- CUDA variables declared as in the `__device__` or `__global__` functions are allocated to the GPU memory, making them accessible to all multithreaded SIMD processors.
- The extended function call syntax for the function `name` that runs on the GPU is:
	```c
	name <<<dimGrid, dimBlock>>>(/*parameter list*/)
	```
	where `dimGrid` and `dimBlock` specify respectively the dimensions of the code in blocks, and the dimensions of a block in threads.
- In addition to the identifier for blocks `blockIdx` and the identifier for threads per block `threadIdx`, CUDA provides a keyword for the number of threads per block `blockDim`, which comes from the `dimBlock` parameter described earlier.

In order to show a snipped of CUDA code, let’s first write a simple DAXPY loop in standard C:

```c
// Call daxpy function
daxpy(n, 2.0, x, y);

//daxpy implementation
void daxpy(int n, double a, double *x, double *y) {
	for (int i = 0; i < n; ++i) {
		y[i] = a * x[i] + y[i];
	}
}
```

If we were to translate the above code to CUDA, we’d have to first launch $n$ threads, one per vector element, with 256 CUDA threads per block in a multithreaded SIMD processor. The GPU function starts by calculating the corresponding element index `i` based on the block ID, the number of threads per block and the thread ID. As long as this index is within the array, it performs the calculation. This looks like so:

```c
// Call daxpy with 256 threads per block
__host__
int nblocks = (n + 255) / 256;
daxpy<<<nblocks, 256>>>(n, 2.0, x, y);

// daxpy implementation, now in CUDA
__device__
void daxpy(int n, double a, double *x, double *y) {
	int i = blockIdx.x * blockDim.x + threadIdx.x;
	if (i < n) {
		y[i] = a * x[i] + y[i];
	}
}
```

We can clearly see that in the loop in the C version of the code, all iterations are independent from one another, which makes it possible for a GPU to parallelise the execution in a similar way as we’ve seen for [vector architectures](../aca24-vector#how-vector-processors-work-an-example).

It is **up to the programmer** to determine the parallelism in CUDA by explicitly specifying the grid dimensions and the number of threads per SIMD processor, as is clear from the snippet of code above. The GPU hardware, on the other hand, handles parallel execution and thread management.

To simplify scheduling by the hardware, CUDA requires that thread blocks be able to execute independently and in any order. Different thread blocks cannot communicate directly, although they can coordinate using atomic memory operations in global memory.

[^1]: The book says “For a few hundred dollars”, which really speaks about the time it was written in—2012.
