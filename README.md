# Utility Functions

``` ________________________
|  C:\> Python_Utils      |
|                        /\
|       /^\/^\           | |
|     _|__|  O|          | |
|\/~     \_/ \          _| |
| \____|______\________/ \ |
|       \_______\_____/   \|
|  utils                 /|
|________________________/ |
```

This repository contains a collection of utility functions that are frequently used in various work and personal projects. These functions are designed to simplify common tasks and improve productivity.

## Table of Contents
- Installation
- Usage
- Functions
  - restart_container
- Contributing
- License
## Installation
To use these utility functions, clone the repository to your local machine:
```bash
 git clone https://github.com/gblackard-gvtx/python-utils.git
```

**Navigate to the project directory:**

```bash
  cd python-utils
```

Install the required dependencies:

### Functions

restart_container
This function checks the status of a Docker container and restarts it if it is running.

Arguments:

service_name (str): The name of the container to check and potentially restart.
Example:
```bash
  python ./restart_container.py serviceName
```

## Other Functions

Additional utility functions will be documented here as they are added to the repository.

## Contributing

Contributions are welcome! If you have a utility function that you think would be useful to others, please feel free to submit a pull request.

1. Fork the repository
3. Create a new branch
  ```bash
  git checkout -b feature-branch
```
4. Commit your changes
   ```bash
   git commit -am 'Add new feature
   ```
6. Push to the branch
   ```bash
   git push origin feature-branch
   ```
8. Create a new Pull Request

##License

This project is licensed under the MIT License. See the LICENSE file for details.
