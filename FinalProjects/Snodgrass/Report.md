# **Physics-Informed Neural Networks (PINNs)**

# Abstract
Physics-Informed Neural Networks (PINNs) are a class of machine learning models that integrate physical laws into the training process. By embedding the governing mathematical equations of physical systems directly into the loss function, PINNs can learn complex relationships from data while adhering to known physical constraints. This project studies the architecture of PINNs, their training methodologies, and their applications in solving problems in physics.

# 1. Introduction

## 1.1 Motivation

## 1.2 Neural Network as Function Approximators
$u_\theta(x,y,t)$ 


## 1.3 Neural Network Training
Loss minimization, backpropagation, and optimization algorithms are key components of training neural networks. The loss function quantifies the difference between the predicted output and the true output, guiding the optimization process to adjust the network's parameters for improved performance. The backpropagation algorithm computes the gradients of the loss function with respect to the network's parameters, allowing for efficient updates during training. Optimization algorithms, such as stochastic gradient descent (SGD) or Adam, are used to iteratively minimize the loss function and enhance the model's accuracy.

## 1.4 Physics-Informed Neural Networks (PINNs)

## 1.5 Application, Advantages, and Limitations of PINNs
- 2D Heat Equation
- Gaussian initial conditions
- Dirichlet and Neumann boundary conditions


# 2. Problem Formulation

## 2.1 Governing Equations
The two dimensional heat equation is given by:
```math
\frac{\partial u}{\partial t} = \alpha \left( \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} \right)
```
where $u(x,y,t)$ is the temperature distribution, $\alpha$ is the thermal diffusivity, and $t$ is time. This equation describes how heat diffuses through a given region over time, making it a fundamental model in various fields such as physics, engineering, and environmental science. The goal of this project is to use PINNs to solve the 2D heat equation under specific initial and boundary conditions, demonstrating the effectiveness of this approach in capturing the underlying physics of the problem.

## 2.2 Initial and Boundary Conditions
The **initial condition** for the 2D heat equation is defined as:
```math
u(x,y,0) = f(x,y)
```
where $f(x,y)$ is a Gaussian function representing the initial temperature distribution. 

The **boundary conditions** can be of two types: Dirichlet and Neumann. The Dirichlet boundary condition specifies the temperature at the boundaries, while the Neumann boundary condition specifies the heat flux across the boundaries. For example, the Dirichlet boundary conditions can be expressed as:
```math
u(x,0,t) = u(x,L_y,t) = u(0,y,t) = u(L_x,y,t) = 0.
```
Which fix the temperature at the boundaries to zero. On the other hand, the Neumann boundary conditions can be expressed as:

```math
\frac{\partial u}{\partial n} = 0
```
for Neumann boundary conditions, where $\frac{\partial u}{\partial n}$ denotes the derivative of $u$ normal to the boundary. This condition implies that there is no heat flux across the boundaries, meaning that the temperature gradient normal to the boundary is zero. The choice of boundary conditions depends on the physical scenario being modeled and can significantly influence the solution of the PDE. In this project, both types of boundary conditions are studied to demonstrate the versatility of PINNs in solving PDEs under different constraints.


## 2.3 Analytical Solution
The analytical solution to the 2D heat equation with Gaussian initial conditions can be derived using separation of variables and Fourier series. The solution is given by:
```math
u(x,y,t) = \frac{1}{4\pi \alpha t} \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(\xi,\eta) e^{-\frac{(x-\xi)^2 + (y-\eta)^2}{4\alpha t}} \mathrm{d}\xi \mathrm{d}\eta
```
where $f(\xi,\eta)$ is the initial temperature distribution and where $\xi$ and $\eta$ are dummy variables of integration representing the spatial coordinates. This solution represents the evolution of the temperature distribution over time, starting from the initial Gaussian profile. The integral form of the solution indicates that the temperature at any point $(x,y)$ and time $t$ is influenced by the initial conditions across the entire spatial domain, weighted by a Gaussian kernel that accounts for the diffusion process. This analytical solution serves as a benchmark for evaluating the performance of PINNs in approximating the solution to the 2D heat equation under the specified conditions.

# 3. Architecture of PINNs

## 3.1 Neural Network Structure and Layers
The architecture of a Physics-Informed Neural Network (PINN) typically consists of multiple layers, including an input layer, several hidden layers, and an output layer. The input layer receives the spatial and temporal coordinates (e.g., $x$, $y$, and $t$), while the output layer produces the predicted solution (e.g., temperature $u_\theta$). The hidden layers can be fully connected or may include other types of layers such as convolutional or recurrent layers, depending on the specific problem being addressed. The choice of *activation functions* in the hidden layers is crucial for capturing the non-linear relationships in the data and ensuring that the network can learn complex patterns effectively. 

## 3.2 Activation Functions
Common activation functions include `ReLU`, `sigmoid`, and `tanh`, each with its own advantages and disadvantages in terms of convergence and performance. The architecture of the PINN must be carefully designed to balance model complexity with computational efficiency, ensuring that it can accurately approximate the solution to the governing PDE while remaining tractable for training.

WHY TANH?
- smooth and differentiable, which is important for computing derivatives in the PDE loss

## 3.3 Automatic Differentiation
Automatic differentiation is a key feature of PINNs that allows for the efficient computation of derivatives required for the PDE loss. This technique enables the network to compute gradients with respect to its parameters and inputs, facilitating the training process and ensuring that the physical constraints are properly enforced during optimization.

## 3.4 Loss Function

### 3.4.1 PDE Residual Loss
The PDE residual loss quantifies how well the predicted solution satisfies the governing PDE. For the 2D heat equation, the PDE residual can be defined as:
```math
r(x, y, t) = u_t - \alpha (u_{xx} + u_{yy})
```

### 3.4.2 Initial Condition Loss

### 3.4.3 Boundary Condition Loss

### 3.4.4 Total Loss
The total loss function for training the PINN is a weighted sum of the PDE residual loss, initial condition loss, and boundary condition loss. This can be expressed as:
```math
\mathcal{L}_{\text{total}} = \lambda_{\text{data}} \mathcal{L}_{\text{data}} + \lambda_{\text{physics}} \mathcal{L}_{\text{physics}} + \lambda_{\text{IC}} \mathcal{L}_{\text{IC}} + \lambda_{\text{BC}} \mathcal{L}_{\text{BC}}
```
```python
loss = (lambda_data * data_loss)
     + (lambda_phys * physics_loss)
     + (lambda_ic * ic_loss)
     + (lambda_bc * bc_loss)
```

# 4. Implementation Details

## 4.1 Software
The implementation of the PINN for solving the 2D heat equation was carried out using Python, leveraging libraries such as `PyTorch` for building and training the neural network. These libraries provide powerful tools for automatic differentiation, optimization, and GPU acceleration, which are essential for efficiently training PINNs.
- Autograd for automatic differentiation
- Optimizers for training the network
- Data handling and visualization tools
- GPU support for faster computations

## 4.2 Network Architecture
The specific network architecture used in this project...
- changed it around though...
### Number of Layers and Neurons


## 4.3 Training Methodology

### 4.3.1 Sampling Data Points
> Explain the code used to create the intial contion points, boundary condition points, and collocation points. 

### 4.3.2 Training Process
#### Optimizer
#### Learning rate
#### Epochs

### 4.3.3 Boundary Condition Enforcement


# 5. Summary of PINN

## 5.1 What does a PINN do?

## 5.2 What does a PINN **not** do?


# 6. Accuracy and Performance Evaluation

## 6.1 Metrics for Evaluating PINN Performance

## 6.2 Comparison with Analytical Solution

## 6.3 Computational Efficiency

## 6.4 Sensitivity Analysis


# 7. Results

## 7.1 Visualization of Predicted Solutions

## 7.2 Training Curves and Convergence Analysis

## 7.3 Error Analysis


# 8. Conclusion