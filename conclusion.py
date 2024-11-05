import matplotlib.pyplot as plt

def convolution(x, h):
    N = len(x)
    M = len(h)
    y = [0] * (N + M - 1)
    for n in range(N + M - 1):
        for k in range(N):
            if 0 <= n - k < M:
                y[n] += x[k] * h[n - k]
    return y

def plot_convolution(x, h, y_convolution):
    plt.figure(figsize=(12, 8))

    # Plot x(n)
    plt.subplot(3, 1, 1)
    plt.stem(range(len(x)), x, use_line_collection=True)
    plt.title('x(n)')
    plt.xlabel('n')
    plt.ylabel('Amplitude')

    # Plot h(n)
    plt.subplot(3, 1, 2)
    plt.stem(range(len(h)), h, use_line_collection=True)
    plt.title('h(n)')
    plt.xlabel('n')
    plt.ylabel('Amplitude')

    # Plot y(n) - Convolution result
    plt.subplot(3, 1, 3)
    plt.stem(range(len(y_convolution)), y_convolution, use_line_collection=True)
    plt.title('y(n) - Convolution')
    plt.xlabel('n')
    plt.ylabel('Amplitude')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    x = [1, 2, 3, 4, 5]
    h = [2, 3, 4]
    y_convolution = convolution(x, h)
    plot_convolution(x, h, y_convolution)
