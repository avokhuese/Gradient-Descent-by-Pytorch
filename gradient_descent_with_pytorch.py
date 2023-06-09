# -*- coding: utf-8 -*-
"""Gradient Descent with PyTorch

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zl--kkWOMt-ZKsvJhPl4zHlh7UXJ1q1A
"""

# Commented out IPython magic to ensure Python compatibility.
# %pylab inline

x=[2,3,4,6]
y=[2.5,3.5,4.5,6.2]
plt.plot(x,y)
plt.legend()

import torch
import torch.nn as nn
import numpy as np

torch.manual_seed(0)

N=100
D=1
x=torch.rand(N,1)*5
y_true=5.3*x + 2.6
y_obs=y_true +0.8*torch.randn(N,D)
plt.plot(y_obs)

plt.plot(x)

plt.plot(y_true)

scatter(y_obs,y_true)

scatter(x,y_true)

scatter(x, y_obs)

y_obs

x

y_true

w=torch.randn(D, requires_grad=True)
b=torch.randn(1, requires_grad=True)

def predict(X):
    return torch.unsqueeze(torch.matmul(X,w)+b,1)

def mse_loss(y_pred, y_true):
    return torch.mean((y_pred-y_true)**2)

def regularized_loss(y_pred, y_true, reg_coeff=0):
    return mse_loss(y_pred, y_true)+reg_coeff * (w**2).sum()

def zero_gradients(*params):
    for p in params:
      p.grad.zero_()

nb_epochs=500
lr=0.01
regularization_coeff = 1e-4

losses = []

for epoch in range(nb_epochs):

    # make prediction
    y_pred = predict(x)

    # compute the loss
    loss = regularized_loss(y_pred, y_obs, regularization_coeff)

    # reverse mode autodiff
    loss.backward()

    # gradient descent (don't track gradients)
    with torch.no_grad():
        w -= lr * w.grad
        b -= lr * b.grad

    # set gradients to zero so they don't accumulate
    zero_gradients(w, b)

    # save loss for plotting
    losses.append(loss.item())

print(f'w={w[0]:0.3f} b={b[0]:0.4f}')

plot(losses)

plot(losses[50:])

x_test=torch.unsqueeze(torch.linspace(x.min(), x.max(), 100),1)
y_test=predict(x_text).detach().numpy()
plot(x_test, y_test, color='r')
scatter(x, y_obs, color='g')