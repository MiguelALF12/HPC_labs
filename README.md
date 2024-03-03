# High-Performance Computing Experiments with Sequential and Parallel Algorithms

## Overview

This repository contains a series of computational experiments designed to explore the efficiency of sequential versus parallel execution of complex algorithms, such as matrix multiplication and PI approximation using dartboard and needle approaches. The experiments are structured into three phases:

1. **Basic Algorithm Comparison**: Initial experiments compare sequential and hand-coded parallel executions in C, analyzing both threads and processes.
2. **Framework/Library Enhancement**: Subsequent tests employ pthreads and OpenMP to emulate parallel executions, aiming to leverage these technologies for optimized performance.
3. **Distributed Network Execution**: The final set of experiments utilizes a simulated distributed network environment, using a master/slave model within a virtual box setup (one master and three slaves) on an Intel i9 PC, to further explore the advantages of parallel processing.

## Insights

These experiments underscore the necessity of parallel implementations for certain algorithms, particularly matrix multiplication, where parallel execution significantly enhances performance compared to sequential execution.

## Technologies

- C Programming
- Pthreads and OpenMP for parallel execution
- VirtualBox for distributed network simulation

## Contribution

Feedback and contributions to extend or refine these experiments are welcome.
