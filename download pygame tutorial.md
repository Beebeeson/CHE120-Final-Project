DOWNLOADING PYGAME USING ANACONDA:



Great! You've successfully upgraded `pip` to the latest version (`20.3.4`). Now that the `pip` version is updated, let's continue with the next steps to resolve the `pygame` installation issue.

### Step 1: Uninstall the Old `pygame` Version

Since you had `pygame 1.9.2a0` installed, it's best to uninstall this older version first. Run the following command:

```bash
pip uninstall pygame
```

When prompted, type `y` to confirm the uninstallation.

### Step 2: Install the Latest Stable Version of `pygame`

Now that the older version is removed, let's install the latest stable version of `pygame`:

```bash
pip install pygame
```

This should install the latest version of `pygame` compatible with your Python version.

### Step 3: Verify the Installation

Once the installation is complete, you can verify that `pygame` was installed correctly by opening a Python interpreter and checking its version:

1. Run Python in the terminal:
   ```bash
   python
   ```

2. Try importing `pygame` and checking its version:
   ```python
   import pygame
   print(pygame.__version__)
   ```

This should output the version of `pygame` you just installed (e.g., something like `2.x.x`), confirming that it's working correctly.

### Alternative: Install via `conda-forge`

If the `pip` installation doesn't work or you encounter any other issues, you can try installing `pygame` from the `conda-forge` channel, which is often more reliable when managing dependencies in an Anaconda environment.

To install `pygame` using `conda`:

```bash
conda install -c conda-forge pygame
```

### Step 4: Run a Simple `pygame` Script

After installation, you can run a simple test script to make sure `pygame` is working. Here's a basic `pygame` script to test:

```python
import pygame

# Initialize pygame
pygame.init()

# Create a window
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Test Pygame")

# Game loop
running = True
while running:
    for event in pygame.event
