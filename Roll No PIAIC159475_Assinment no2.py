{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Numpy_Assignment_2::"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Question:1"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Convert a 1D array to a 2D array with 2 rows?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Desired output::"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "array([[0, 1, 2, 3, 4],\n",
    "        [5, 6, 7, 8, 9]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])"
      ]
     },
     "metadata": {},
     "execution_count": 2
    }
   ],
   "source": [
    "import numpy as np\n",
    "arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])\n",
    "arr"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "array([[0, 1, 2, 3, 4],\n",
       "       [5, 6, 7, 8, 9]])"
      ]
     },
     "metadata": {},
     "execution_count": 3
    }
   ],
   "source": [
    "arr_2d = np.reshape(arr, (2, 5))\n",
    "arr_2d"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Question:2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "###  How to stack two arrays vertically?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Desired Output::"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "array([[0, 1, 2, 3, 4],\n",
    "        [5, 6, 7, 8, 9],\n",
    "       [1, 1, 1, 1, 1],\n",
    "       [1, 1, 1, 1, 1]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "array([[1],\n",
       "       [2],\n",
       "       [3],\n",
       "       [2],\n",
       "       [3],\n",
       "       [4]])"
      ]
     },
     "metadata": {},
     "execution_count": 4
    }
   ],
   "source": [
    "a = np.array([[1], [2], [3]])\n",
    "b = np.array([[2], [3], [4]])\n",
    "np.vstack((a,b))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Question:3"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### How to stack two arrays horizontally?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Desired Output::"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "array([[0, 1, 2, 3, 4, 1, 1, 1, 1, 1],\n",
    "       [5, 6, 7, 8, 9, 1, 1, 1, 1, 1]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "array([1, 2, 3, 2, 3, 4])"
      ]
     },
     "metadata": {},
     "execution_count": 5
    }
   ],
   "source": [
    "a = np.array((1,2,3))\n",
    "b = np.array((2,3,4))\n",
    "np.hstack((a,b))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Question:4"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### How to convert an array of arrays into a flat 1d array?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Desired Output::"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "array([1, 2, 3, 4, 5, 6])"
      ]
     },
     "metadata": {},
     "execution_count": 8
    }
   ],
   "source": [
    "a = np.array([[1,2,3], [4,5,6]])\n",
    "b = a.ravel()\n",
    "b"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Question:5"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### How to Convert higher dimension into one dimension?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Desired Output::"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "array([[ 0.04209389, -1.16123207, -0.29433705],\n",
       "       [-2.51391943,  0.45454411,  0.45047521]])"
      ]
     },
     "metadata": {},
     "execution_count": 11
    }
   ],
   "source": [
    "x=np.random.randn(2,3)\n",
    "x\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "array([ 0.04209389, -1.16123207, -0.29433705, -2.51391943,  0.45454411,\n",
       "        0.45047521])"
      ]
     },
     "metadata": {},
     "execution_count": 12
    }
   ],
   "source": [
    "x.ravel()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Question:6"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Convert one dimension to higher dimension?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Desired Output::"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "array([[ 0, 1, 2],\n",
    "[ 3, 4, 5],\n",
    "[ 6, 7, 8],\n",
    "[ 9, 10, 11],\n",
    "[12, 13, 14]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "array([0, 1, 2, 3, 4, 5])"
      ]
     },
     "metadata": {},
     "execution_count": 13
    }
   ],
   "source": [
    "x=np.arange(6)\n",
    "x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "array([[0, 1, 2],\n",
       "       [3, 4, 5]])"
      ]
     },
     "metadata": {},
     "execution_count": 15
    }
   ],
   "source": [
    "y=x.reshape((2, 3))\n",
    "y"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Question:7"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Create 5x5 an array and find the square of an array?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "array([[-2.10688711, -0.01009833, -1.44004359,  0.26130877,  0.2420662 ],\n",
       "       [ 0.90804045, -0.50342864, -0.89207988, -0.53411743,  1.06393345],\n",
       "       [-2.52409601, -0.08119505, -0.88989763, -0.49730387, -0.76855163],\n",
       "       [-0.67180381,  0.21166924,  0.39471296, -0.96636466, -0.07864266],\n",
       "       [-1.38294292,  0.37777959, -0.79147626,  0.78403449,  0.19365616]])"
      ]
     },
     "metadata": {},
     "execution_count": 21
    }
   ],
   "source": [
    "x = np.random.randn(5,5)\n",
    "x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "array([[4.43897328e+00, 1.01976270e-04, 2.07372553e+00, 6.82822716e-02,\n",
       "        5.85960468e-02],\n",
       "       [8.24537455e-01, 2.53440399e-01, 7.95806507e-01, 2.85281430e-01,\n",
       "        1.13195439e+00],\n",
       "       [6.37106067e+00, 6.59263649e-03, 7.91917785e-01, 2.47311142e-01,\n",
       "        5.90671601e-01],\n",
       "       [4.51320358e-01, 4.48038654e-02, 1.55798324e-01, 9.33860653e-01,\n",
       "        6.18466825e-03],\n",
       "       [1.91253112e+00, 1.42717421e-01, 6.26434669e-01, 6.14710086e-01,\n",
       "        3.75027072e-02]])"
      ]
     },
     "metadata": {},
     "execution_count": 22
    }
   ],
   "source": [
    "np.square(x)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Question:8"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Create 5x6 an array and find the mean?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "array([[ 1.20949096, -1.06068095, -0.64849569,  0.7317532 , -0.13657707,\n",
       "        -1.52156582],\n",
       "       [ 0.69085731,  0.64338838,  0.81945215, -0.53582066,  0.95839999,\n",
       "         0.63132923],\n",
       "       [ 0.44001784, -1.2302449 ,  1.01186337, -1.0497929 ,  1.834982  ,\n",
       "        -0.7868694 ],\n",
       "       [-1.08265671,  0.79275508,  0.70018845, -0.95300595,  1.60960312,\n",
       "         0.00338204],\n",
       "       [-1.07827306,  0.45173888, -1.12918178,  0.92994129,  0.66756694,\n",
       "        -0.44698684]])"
      ]
     },
     "metadata": {},
     "execution_count": 23
    }
   ],
   "source": [
    "x = np.random.randn(5,6)\n",
    "x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "0.08221861664234824"
      ]
     },
     "metadata": {},
     "execution_count": 24
    }
   ],
   "source": [
    "np.mean(x)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Question:9"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Find the standard deviation of the previous array in Q8?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "0.9416865901585803"
      ]
     },
     "metadata": {},
     "execution_count": 27
    }
   ],
   "source": [
    "np.std(x)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Question:10"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Find the median of the previous array in Q8?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "0.4458783613479492"
      ]
     },
     "metadata": {},
     "execution_count": 28
    }
   ],
   "source": [
    "np.median(x)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Question:11"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Find the transpose of the previous array in Q8?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "array([[ 1.20949096,  0.69085731,  0.44001784, -1.08265671, -1.07827306],\n",
       "       [-1.06068095,  0.64338838, -1.2302449 ,  0.79275508,  0.45173888],\n",
       "       [-0.64849569,  0.81945215,  1.01186337,  0.70018845, -1.12918178],\n",
       "       [ 0.7317532 , -0.53582066, -1.0497929 , -0.95300595,  0.92994129],\n",
       "       [-0.13657707,  0.95839999,  1.834982  ,  1.60960312,  0.66756694],\n",
       "       [-1.52156582,  0.63132923, -0.7868694 ,  0.00338204, -0.44698684]])"
      ]
     },
     "metadata": {},
     "execution_count": 29
    }
   ],
   "source": [
    "np.transpose(x)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Question:12"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Create a 4x4 an array and find the sum of diagonal elements?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [],
   "source": [
    "arr = np.array([[5, 2, 1, 6], \n",
    "                    [9, 4, 5, 2], \n",
    "                    [11, 5, 3, 9], \n",
    "                    [7, 5, 9, 3]]) \n",
    "                    \n",
    "  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "array([5, 4, 3, 3])"
      ]
     },
     "metadata": {},
     "execution_count": 32
    }
   ],
   "source": [
    "diag = np.diagonal(arr) \n",
    "diag"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "15"
      ]
     },
     "metadata": {},
     "execution_count": 33
    }
   ],
   "source": [
    "result=(sum(diag))\n",
    "result"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Question:13"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Find the determinant of the previous array in Q12?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "-164.0000000000002"
      ]
     },
     "metadata": {},
     "execution_count": 37
    }
   ],
   "source": [
    "np.linalg.det(arr)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Question:14"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Find the 5th and 95th percentile of an array?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "85.0"
      ]
     },
     "metadata": {},
     "execution_count": 41
    }
   ],
   "source": [
    "a = [154, 400, 1124, 82, 94, 108]\n",
    "np.percentile(a,5)\n",
    " "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "943.0"
      ]
     },
     "metadata": {},
     "execution_count": 42
    }
   ],
   "source": [
    "np.percentile(a,95)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Question:15"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### How to find if a given array has any null values?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "array([[-0.05405585,  0.03858816,  0.28547468],\n",
       "       [-2.44068582, -0.89064605,  1.77604171]])"
      ]
     },
     "metadata": {},
     "execution_count": 50
    }
   ],
   "source": [
    "x = np.random.randn(2,3)\n",
    "x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "array([[False, False, False],\n",
       "       [False, False, False]])"
      ]
     },
     "metadata": {},
     "execution_count": 51
    }
   ],
   "source": [
    "np.isnan(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5-final"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}