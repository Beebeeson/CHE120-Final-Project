DOWNLOADING PYGAME USING ANACONDA:

To install `pygame` using Anaconda, you can use the `conda` package manager, which is the default for Anaconda environments. Here’s how you can do it:

### Step 1: Open Anaconda Prompt

1. Open the **Anaconda Prompt** from your Start menu (on Windows) or terminal (on macOS/Linux).
2. If you're working in a specific virtual environment, make sure you activate it first using:
   ```bash
   conda activate your_environment_name
   ```

### Step 2: Install Pygame with Conda

To install `pygame` in your Anaconda environment, use the following command in the Anaconda Prompt:

```bash
conda install -c cogsci pygame
```

### Explanation:
- The `-c cogsci` flag specifies that you want to install `pygame` from the **cogsci** channel (which is a popular channel for `pygame` in the Anaconda ecosystem).
- This will download and install the latest compatible version of `pygame` for your environment.

### Step 3: Verify Installation

After installation is complete, you can verify that `pygame` is installed by opening a Python session and importing `pygame`:

1. Open the Python interpreter by typing `python` in the Anaconda Prompt:
   ```bash
   python
   ```

2. Try importing `pygame`:
   ```python
   import pygame
   print(pygame.__version__)  # This will print the installed version of pygame
   ```

If there are no errors, `pygame` has been successfully installed and is ready to use!

### Step 4: Creating a New Anaconda Environment (Optional)

If you'd like to create a new environment with `pygame` installed, you can do the following:

1. Create a new environment and install `pygame` in it:
   ```bash
   conda create -n myenv pygame
   ```

2. Activate the environment:
   ```bash
   conda activate myenv
   ```

3. Verify that `pygame` is installed by running the import command as shown earlier.

That's it! You’ve successfully installed `pygame` using Anaconda.

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
