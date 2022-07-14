<p align="center">
    <a href="https://cloud.ibm.com">
        <img src="https://cloud.ibm.com/media/docs/developer-appservice/resources/ibm-cloud.svg" height="100" alt="IBM Cloud">
    </a>
</p>


<p align="center">
    <a href="https://cloud.ibm.com">
    <img src="https://img.shields.io/badge/IBM%20Cloud-powered-blue.svg" alt="IBM Cloud">
    </a>
    <img src="https://img.shields.io/badge/platform-django-lightgrey.svg?style=flat" alt="platform">
    <img src="https://img.shields.io/badge/license-Apache2-blue.svg?style=flat" alt="Apache 2">
</p>


# Create and deploy a Python Django application

> We have applications available for [Node.js Express](https://github.com/IBM/node-express-app), [Go Gin](https://github.com/IBM/go-gin-app), [Python Flask](https://github.com/IBM/python-flask-app), [Python Django](https://github.com/IBM/python-django-app), [Java Spring](https://github.com/IBM/java-spring-app), [Java Liberty](https://github.com/IBM/java-liberty-app), [Swift Kitura](https://github.com/IBM/swift-kitura-app), [Android](https://github.com/IBM/android-app), and [iOS](https://github.com/IBM/ios-app).

In this sample application, you will create a web application using Django to serve web pages in Python, complete with standard best practices, including a health check.

This app contains an opinionated set of files for web serving:

- `app/templates/index.html`
- `staticfiles/js/bundle.js`
- `staticfiles/css/default.css`

## Steps

You can [deploy this application to IBM Cloud](https://cloud.ibm.com/developer/appservice/starter-kits/python-django-app) or [build it locally](#building-locally) by cloning this repo first. Once your app is live, you can access the `/health` endpoint to build out your cloud native application.

### Deploying to IBM Cloud

**Deprecated**: IBM® Cloud Foundry is deprecated. For more information, see [Deprecation of IBM Cloud Foundry](http://ibm.biz/ibmcf-announce).

<p align="center">
    <a href="https://cloud.ibm.com/developer/appservice/starter-kits/python-django-app">
    <img src="https://cloud.ibm.com/devops/setup/deploy/button_x2.png" alt="Deploy to IBM Cloud">
    </a>
</p>

Click **Deploy to IBM Cloud** to deploy this same application to IBM Cloud. This option creates a deployment pipeline, complete with a hosted GitLab project and a DevOps toolchain. You can deploy your app to Cloud Foundry, a Kubernetes cluster, or a Red Hat OpenShift cluster. OpenShift is available only through a standard cluster, which requires you to have a billable account.

[IBM Cloud DevOps](https://www.ibm.com/cloud/devops) services provides toolchains as a set of tool integrations that support development, deployment, and operations tasks inside IBM Cloud.

### Building Locally

To get started building this application locally, you can either run the application natively or use the [IBM Cloud Developer Tools](https://cloud.ibm.com/docs/cli?topic=cloud-cli-getting-started) for containerization and easy deployment to IBM Cloud.

#### Native Application Development

* Install [Python](https://www.python.org/downloads/)

Running Django applications has been simplified with a `manage.py` file to avoid dealing with configuring environment variables to run your app. From your project root, you can download the project dependencies with:

```bash
pipenv install
```

Then, activate this app's virtualenv:

```bash
pipenv shell
```

To run your application locally, run this inside the virtualenv:

```bash
python manage.py start
```

Your application will be running at `http://localhost:3000`.  You can access the `/health` endpoint at the host. You can also verify the state of your locally running application using the Selenium UI test script included in the `scripts` directory.

##### Debugging locally
To debug a `django` project run `python manage.py runserver` with DEBUG set to True in `settings.py` to start a native django development server. This comes with the Django's stack-trace debugger, which will present runtime failure stack-traces. For more information, see [Django's documentation](https://docs.djangoproject.com/en/2.0/ref/settings/).

#### IBM Cloud Developer Tools

Install [IBM Cloud Developer Tools](https://cloud.ibm.com/docs/cli?topic=cloud-cli-getting-started) on your machine by running the following command:
```
curl -sL https://ibm.biz/idt-installer | bash
```

Create an application on IBM Cloud by running:

```bash
ibmcloud dev create
```

This will create and download a starter application with the necessary files needed for local development and deployment.

Your application will be compiled with Docker containers. To compile and run your app, run:

```bash
ibmcloud dev build
ibmcloud dev run
```

This will launch your application locally. When you are ready to deploy to IBM Cloud on Cloud Foundry or Kubernetes, run one of the commands:

```bash
ibmcloud dev deploy -t buildpack // to Cloud Foundry
ibmcloud dev deploy -t container // to K8s cluster
```

You can build and debug your app locally with:

```bash
ibmcloud dev build --debug
ibmcloud dev debug
```

## Next Steps
* Learn more about [IBM Cloud](https://cloud.ibm.com) and how to incorporate its services in your application.
* Explore other [sample applications](https://cloud.ibm.com/developer/appservice/starter-kits) on IBM Cloud.

## License

This sample application is licensed under the Apache License, Version 2. Separate third-party code objects invoked within this code pattern are licensed by their respective providers pursuant to their own separate licenses. Contributions are subject to the [Developer Certificate of Origin, Version 1.1](https://developercertificate.org/) and the [Apache License, Version 2](https://www.apache.org/licenses/LICENSE-2.0.txt).

[Apache License FAQ](https://www.apache.org/foundation/license-faq.html#WhatDoesItMEAN)

### DB2 Connection
* (MacOS) Install [Homebrew](https://brew.sh/)
* (Windows, Linux) Install [Python](https://www.python.org/downloads/)
* (MacOS) Install Python via Homebrew
  * `brew install python@3.9 # (x being the minor version)`
  * `echo "alias python3='/usr/local/bin/python3.9'" >> ~/.bashrc`
  * `echo "alias pip3='/usr/local/bin/pip3.9'" >> ~/.bashrc`
  * `echo 'export PATH="/usr/local/opt/python@3.9/bin:$PATH"' >> ~/.bashrc`
  * `source ~/.bashrc`
If this does not work you can also try unlink python3 and link to python3.9.

#### Setting up your local environment
To set up the project ensure you are running in a virtual environment so that the project is in a sandbox and not impacted by any other python dependencies
1. Open the project folder in your terminal
2. Ensure you're using the correct python version by running `python3 --version && which python3`
3. Install the IBM DB2 package: `pip3 install ibm-db`
2. Run `python3 -m venv venv` to create your virtual environment
3. Use `source venv/bin/activate` to activate your virtual environment
4. Do `pip3 install pip-tools` to install the pip-tools dependency manager (it uses pip by default, but makes it slightly better)


instal dotenv
```
pip3 install python-dotenv
```
Running Django applications has been simplified with a `manage.py` file to avoid dealing with configuring environment variables to run your app. From your project root, you can download the project dependencies with:

```bash
pip-tools sync requirements.txt #To install production packages
pip-tools sync requirements.dev #To install development packages
```

Then, activate this app's virtualenv:

```bash
source venv/bin/activate
```

(MacOS Only) If you're on MacOS, you need to run the `fix-db2-mac.sh` script to ensure that the `ibm-db2` package works for you

```bash
sh fix-db2-mac.sh
```

Test db2 connection
```
python3 db2_connect.py
```

If it still doesn't work, try fixing dyld path
```
export DYLD_LIBRARY_PATH=venv/lib/python3.9/site-packages/clidriver/lib:$DYLD_LIBRARY_PATH
```

