# Github-Actions

This repository contains a Flask application that renders an `index.html` file. It demonstrates a CI/CD workflow using GitHub Actions, enabling automatic testing and deployment to an EC2 instance across multiple environments.

## Table of Contents
- [Features](#features)
- [Directory Structure](#directory-structure)
- [Workflow](#workflow)
- [Infrastructure Setup](#infrastructure-setup)
- [Development and Deployment](#development-and-deployment)
- [GitHub Actions Workflow](#GitHub-Actions-Workflow)
- [Summary](#summary)
- [Contributing](#contributing)
- [Contact](#Contact)


## Features
- Flask application to render a static HTML page.
- Automated testing with pytest.
- Continuous Integration and Deployment (CI/CD) setup using GitHub Actions.
- Supports multiple environments: development, staging, and production.

## Directory Structure
```bash
your-repo/
├── app.py                  # Main Flask application
├── tests/                  # Directory for test files
│   └── test_app.py         # Pytest file for unit tests
├── requirements.txt        # Python dependencies
└── .github/
    └── workflows/
        └── main.yml      # GitHub Actions workflow for CI/CD
```




## Workflow
The GitHub Actions workflow is defined in `.github/workflows/deploy.yml` and is triggered on pushes and pull requests to the `dev`, `stage`, and `prod` branches. The workflow includes the following steps:
1. Checkout the repository code.
2. Set up the Python environment and install dependencies.
3. Run tests using pytest.
4. Copy files to the EC2 instance for deployment.

## Infrastructure Setup

To deploy the application to an EC2 instance, follow these steps:

### 1. EC2 Instance Configuration
Ensure that your EC2 instance is properly configured and accessible via SSH. You will need:
- **Public IP:** The public IP address of your EC2 instance.
- **Default Username:** The default username for your EC2 instance (commonly `ubuntu` for Ubuntu instances).
- **SSH Key:** The private SSH key (`.pem` file) that was generated when you created the EC2 instance. This is required to securely connect to your instance via SSH.

### 2. Setting Up GitHub Repository Secrets
To securely transfer files and execute commands on the EC2 instance through GitHub Actions, you will need to configure the following repository secrets:

- **EC2_HOST_NAME:** The public IP address or hostname of your EC2 instance.
- **EC2_USERNAME:** The SSH username for your EC2 instance (e.g., `ubuntu`).
- **EC2_SSHKEY:** Your EC2 private key stored as a secret, which should be the contents of the `.pem` file used for SSH access.

#### Steps to Add Secrets:
1. Navigate to your GitHub repository.
2. Go to **Settings** > **Secrets and variables** > **Actions**.
3. Click **New repository secret** and add the following:
   - `EC2_HOST_NAME`
   - `EC2_USERNAME`
   - `EC2_SSHKEY` (add the private key content)
4. Save each secret.

### 3. Deploying via GitHub Actions
With the EC2 instance properly configured and the secrets set up in your GitHub repository, you can deploy your application directly from GitHub using the automated workflow in place.

Make sure the GitHub Actions workflow is triggered by a push to the designated branch, and the necessary files will be securely copied to your EC2 instance.




## Development and Deployment

This project follows a structured workflow across three distinct environments: **Development**, **Staging**, and **Production**. Each environment serves a specific purpose in the development lifecycle, allowing for thorough testing and safe deployments.

### Development Environment
- **Branch Name:** `dev`
- **Purpose:** The development environment is where new features and bug fixes are initially implemented. This is the first stage in the CI/CD pipeline where code is actively developed.
- **Testing:** To run tests locally, ensure you have pytest installed. You can run the tests using:
     ```bash
     pytest tests/
     ```

- **Actions Taken:**
  - Developed the Flask application locally in VS Code, focusing on rendering `index.html`.
  - Post development in local pushed the code to git repository into the main branch first.
  - Created a separate `dev` branch to work on new features without affecting the main branch.
  - Set up a GitHub Actions workflow that triggers on pushes to the `dev` branch.
  - Configured the workflow to install dependencies and run tests using pytest to ensure that the new features are working as expected.
  - Triggered the workflow by pushing changes to the `dev` branch.
  - The application successfully cleared the Pytest tests and the code base was deployed to the EC2 instance using the configured GitHub Actions, which automated the deployment process.
- **Outcome:** Successful execution of tests confirmed that the changes were functioning correctly before proceeding to the next stage.

### Staging Environment
- **Branch Name:** `stage`
- **Purpose:** The staging environment is a replica of the production environment and is used for final testing before deployment. This stage allows for additional testing in a production-like setting.
- **Actions Taken:**
  - Created a `stage` branch from the `dev` branch to prepare for staging deployment.
  - Updated the GitHub Actions workflow to reflect any necessary changes for the staging environment.
  - Triggered the workflow by pushing changes to the `stage` branch, which included running the same tests that were executed in the development phase.
  - The application successfully cleared the Pytest tests and the code base was deployed to the EC2 instance again using the configured GitHub Actions, which automated the deployment process.
- **Outcome:** After passing all tests and UAT in staging, the application was deemed ready for production deployment.

### Production Environment
- **Branch Name:** `prod`
- **Purpose:** The production environment is the live environment where the application is accessed by end-users. This stage is critical as it directly impacts user experience.
- **Actions Taken:**
  - Created a `prod` branch from the `stage` branch for the final deployment.
  - Made necessary adjustments to the GitHub Actions workflow for the production environment, ensuring that it aligns with production standards.
  - Triggered the workflow by pushing changes to the `prod` branch, which included running the complete suite of tests to confirm that everything is functioning correctly.
  - The application successfully cleared the Pytest tests and the code base was deployed to the EC2 instance again using the configured GitHub Actions, which automated the deployment process.
- **Outcome:** The application was successfully deployed to the production environment, and the workflow confirmed that the deployment was completed without issues.

## GitHub Actions Workflow

This workflow automates the deployment process to an AWS EC2 instance. It triggers on two events: a push or pull request to the `prod` branch. The following steps outline the workflow's operations:

### Steps Overview

1. **Checkout Code**:
   - This step retrieves the latest code from the repository, ensuring that the workflow operates on the most recent version.

2. **Set Up Python Environment**:
   - A specific version of Python (`3.12`) is set up in the environment, allowing for consistent dependencies and behavior across runs.

3. **Install Dependencies**:
   - This step upgrades `pip` and installs necessary Python packages from the `requirements.txt` file, preparing the environment for the application.

4. **Run Tests**:
   - Executes the test suite using `pytest`, verifying that the application functions correctly and adheres to the expected standards.

5. **Copy Files to EC2**:
   - This step securely transfers files from the GitHub Actions runner to the specified EC2 instance using SCP (Secure Copy Protocol). It uses the instance's public IP, SSH credentials, and specifies the files and destination for the transfer.

### Final outcome of this workflow

This automated workflow streamlines the deployment process, ensuring that code is tested and seamlessly deployed to an AWS EC2 instance with each update to the `dev`, `test` or `prod` branch.

## Summary
By maintaining separate branches for development, staging, and production, this project ensures that code is rigorously tested at each stage of the development lifecycle. This structured approach minimizes the risk of deploying untested code and facilitates a smoother transition from development to production.

## Contributing

We welcome contributions! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes with clear messages.
4. Submit a pull request for review.

Make sure to follow the code style guidelines and include proper documentation for any new features.


## Contact

For any queries, feel free to contact me:

- **Email:** adityavakharia@gmail.com
- **GitHub:** [Aditya-rgb](https://github.com/Aditya-rgb/Github-Actions)

You can also open an issue in the repository for questions or suggestions.

