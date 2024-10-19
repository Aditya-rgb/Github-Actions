# Github-Actions

This repository contains a Flask application that renders an `index.html` file. It demonstrates a CI/CD workflow using GitHub Actions, enabling automatic testing and deployment to an EC2 instance across multiple environments.

## Table of Contents
- [Features](#features)
- [Directory Structure](#directory-structure)
- [Workflow](#workflow)
- [Testing](#testing)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Features
- Flask application to render a static HTML page.
- Automated testing with pytest.
- Continuous Integration and Deployment (CI/CD) setup using GitHub Actions.
- Supports multiple environments: development, staging, and production.

## Directory Structure
your-repo/
├── app.py
├── tests/
│   └── test_app.py
├── requirements.txt
└── .github/
    └── workflows/
        └── deploy.yml  # Your GitHub Actions workflow file


## Workflow
The GitHub Actions workflow is defined in `.github/workflows/deploy.yml` and is triggered on pushes and pull requests to the `dev`, `stage`, and `prod` branches. The workflow includes the following steps:
1. Checkout the repository code.
2. Set up the Python environment and install dependencies.
3. Run tests using pytest.
4. Copy files to the EC2 instance for deployment.

## Infrastructure setup

To deploy the application to EC2, follow these steps:

Configure your EC2 instance and ensure it is accessible via SSH.
The Public IP, Default username and the SSH key which you can fetch from the .pem file which was created at the time of EC2 instance creation.
Set up your GitHub repository secrets for EC2_HOST_NAME, EC2_USERNAME, and EC2_SSHKEY by doiung the following
- fvfvf
- dvd
- sdv



## Development, Staging, and Production Environments

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
- **Outcome:** Successful execution of tests confirmed that the changes were functioning correctly before proceeding to the next stage.

### Staging Environment
- **Branch Name:** `stage`
- **Purpose:** The staging environment is a replica of the production environment and is used for final testing before deployment. This stage allows for additional testing in a production-like setting.
- **Actions Taken:**
  - Created a `stage` branch from the `dev` branch to prepare for staging deployment.
  - Updated the GitHub Actions workflow to reflect any necessary changes for the staging environment.
  - Triggered the workflow by pushing changes to the `stage` branch, which included running the same tests that were executed in the development phase.
  - Conducted manual testing and user acceptance testing (UAT) to ensure all features work as intended in the staging environment.
- **Outcome:** After passing all tests and UAT in staging, the application was deemed ready for production deployment.

### Production Environment
- **Branch Name:** `prod`
- **Purpose:** The production environment is the live environment where the application is accessed by end-users. This stage is critical as it directly impacts user experience.
- **Actions Taken:**
  - Created a `prod` branch from the `stage` branch for the final deployment.
  - Made necessary adjustments to the GitHub Actions workflow for the production environment, ensuring that it aligns with production standards.
  - Triggered the workflow by pushing changes to the `prod` branch, which included running the complete suite of tests to confirm that everything is functioning correctly.
  - Deployed the application to the EC2 instance using the configured GitHub Actions, which automated the deployment process.
- **Outcome:** The application was successfully deployed to the production environment, and the workflow confirmed that the deployment was completed without issues.



## Summary
By maintaining separate branches for development, staging, and production, this project ensures that code is rigorously tested at each stage of the development lifecycle. This structured approach minimizes the risk of deploying untested code and facilitates a smoother transition from development to production.
