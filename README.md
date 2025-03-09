Candle Mania
=================

Link to production site: 

# Introduction

The Candle Mania is a sample site for publishing blogs about candles.

## Users

There are four categories of users: a visitor, a registered user, an admin and a superuser.

A **visitor** can browse products and view each product's details.

A **registered user** can do everything a visitor can and add, edit, and delete its blogs. 

An **editor** can accept blogs.

A **superuser** can appoint a registered user to editor.

## Used technologies, frameworks, services

- HTML
- CSS
- JavaScript
- Python
- Django
- PostgreSQL
- Git
- GitHub
- Grammarly to catch grammar slips and improve the text

## Intended audience

This project's intended audience is anyone who is interested into information about candles.

Project assessors and recruiters are welcome.

# Development
This part is dedicated to the page's development.
## Development process
The Development of this site includes consequently following the stages described in detail in the next sections:
* Requirements gathering described in Strategy Plane – gathering all requirements to the Site. User Stories belong to this stage. 
* Scope definition described in Scope Plane – defining what will be included in the first release.
* The Structure plane is introduced at the start of the design, where wireframes are used to create sketches of the pages, and Entity-Relationship Diagrams (ERD) show the database structure.
* The result of a Skeleton plane is the Site’s navigation and detailed database description.
* The last in Development comes the Surface plane, where all design is completed for various screen sizes and audiences. This plane includes all JavaScript and CRUD functionality.
* Then comes the Site testing, which is performed manually using Jigsaw (CSS) and W3 Validator (HTML). Google’s Lighthouse test is used to test the site’s performance. JavaScript's syntax is tested using Beautify Tools. The database is tested by inserting data using UI and validating inserted and updated data using UI or database tools to read data directly in the database.

## Strategy plane
**User stories**
* as a site's visitor I need to
  * [US-V01] browse all blogs
  * [US-V02] have a paginator when there are more than 8 items on a page grid mode
  * [US-V03] read the full blog
* as a registered user I need to
  * [US-RU01] be able to do the same a visitor can
  * [US-RU02] be able to log in
  * [US-RU03] have a registration page
  * [US-RU04] write a blog
  * [US-RU05] update my a blog
  * [US-RU06] delete my a blog
  * [US-RU07] comment a blog
  * [US-RU08] approve blog comments to my posts
  * [US-RU09] delete my blog comments
  * [US-RU10] have my blogs protected from altering by other users
  * [US-RU11] have my blogs protected from deleting by other users
  * [US-RU12] have my comments protected from altering by other users
  * [US-RU13] have my comments protected from deleting by other users
* as an editor I need to
  * [US-A01] be able to do the same as a registered user
  * [US-A02] approve any blog
  * [US-A03] delete blog
* as a superuser I need to
  * [US-SU1] list all registered users
  * [US-SU2] grant registered user an editor role
  * [US-SU3] revoke the editor role
* as a site owner I need to 
  * [US-SO1] show my skills in front-end and back-end programming
  * [US-SO2] use PostgreSQL as a database
  * [US-SO3] use Django framework
  * [US-SO4] the site's design, look and functionality follow industry standards
  * [US-SO5] the site has 404 error page (page not found)

Site's development is performed using JetBrain's PyCharm IDE, Python version 3.12 and Django version 5.1.4.
Site uses the database PostgreSQL v16 for storing data.
Git and GitHub is used for storing code and version control.

## Scope plane
The user stories above show full functionality of the site. However, due to certain circumstances user permission 
functionality can be reduced up to the registered user. 

At the end of development will be delivered:
* Implemented User Stories
* README.md file
* Development documentation in README.md file, in particular:
  * Requirements,
  * Testing process in a separate file,
* Deployment to cPanel hosting.
* Code and version control using Git and GitHub

## Structure plane
The structure plane is concerned with design elements on pages.

**Wireframes** allow seeing what will be on pages. There is no detailed design or colours (in most cases); #
schematic elements only are placed on a page.



**Entity-Relationship Diagrams** (ERD) show relationship between [data] entities. 
It is a starting point of a database design, and it affects site's navigation and design.


## Skeleton plane

## Surface plane

# Testing
Software testing, a crucial step in software development, is the process of evaluating and verifying whether a software application meets its expected requirements and functions correctly, ensuring the end product is of high quality and meets user expectations.

It aims to identify defects, bugs, or missing features in contrast to the specified requirements.

Essentially, it answers two critical questions:

Is the software built the right way? (does the software correctly implement specific functions?)
Is it the right product? (does the software align with customer requirements or user stories?)
This project uses manual testing and acceptance testing.

During manual testing, the test operator manually checks if the system works as expected by going through all screens and simulating end-user behaviour. The user interface is also checked for look and feel during this test. In web development, web pages are tested against different screen sizes, browsers, and operational systems.

The functionality of the system can be automated using test scripts. For that purpose, automated tests are used. Automated tests are helpful for large projects to ensure the new functionality does not change old behaviour. They increase testing speed but add extra work for writing them. One of the testing frameworks for JavaScript is Jest. Automated tests are not used for this project as the project has no continuity, and writing tests adds extra work.

Acceptance tests ensure that all user requirements are met. In this project, they are user stories.

The full performed test is in a [separate file](/TESTING.md).

# Deployment

## Creating database and granting privileges

To create database and database user using SQL statements connect to the database server with commandline tool 
with user having admin privileges. Change `user`, `database` and `mypassword` in scripts with your preferred names.

**Creating database:**
```
CREATE USER myuser WITH PASSWORD 'mypassword';
CREATE DATABASE mydatabase;
```
**Privileges to database user:**
```
GRANT CONNECT ON DATABASE mydatabase TO myuser;
```

change superuser's default database with command:
```
\c mydatabase
```
Continue with granting privileges:
```
GRANT ALL PRIVILEGES ON SCHEMA public TO myuser;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO myuser;
```

Detailed database and user creation is not included in this document as it would reveal server-side information.
Overall, with cPanel database creation is straight-forward task.

## Environment variables
Environment variables for development are set in env.py file. For the production environment those should be set
on web server during deployment. The development environment is set on a local computer with postgresql installed.

**The list of environment variables:**
```
# security
SECRET_KEY: <THE KEY FROM INITIAL SETTINGS.PY FILE>
DEBUG: False
ALLOWED_HOSTS: localhost, 127.0.0.1  # a list of allowed hosts separated by coma

# database
POSTGRES_USER: <myuser>
POSTGRES_PASSWORD: <mypassword>
POSTGRES_HOST: localhost
POSTGRES_PORT: 5432  # default is 5432
POSTGRES_DATABASE_NAME: <mydatabase>
```
The secret key is copied from initial settings.py file. If you do not have it create a temporary django app, 
copy the key and destroy that django app.

## The very first installation
### Environment

### Pre-installation procedures

1. create a database and a database user with permission described above (how to configure PostgreSQL see a database documentation)
2. Enabling environment variables named above
  [images]

### Installation
1. copying files

* Download project files from github as one zip file.

![download source code from github image](/readme_assets/deployment/download_files_from_git.png)

* For copying files with cPanel's File Manager: create a folder for candlemania files. Let's call it a &lt;project root&gt;

* Upload dowloaded project's code zip into &lt;project root&gt;
* Unzip candlemania files into &lt;project root&gt; (see image)

![image of project code into <project root>](/readme_assets/deployment/copied_and_extracted_files_in_project_root.png)

3. create a domain/subdomain pointing to the &lt;project root&gt;/candlemania-main directory

2. deploying application
* in cPanel Software section choose Setup Python App.
* on the next screen cPanel will show a list of installed applications. Press the button "Create Application"

![image of create application screen](/readme_assets/deployment/create_application_screen.png)
Choose Python version 3.12, write the directory name where project code resides, choose domain name for the application 
and press the button "Create".

Additional configuration information is added to the application screen.
![image of generated configuration info](/readme_assets/deployment/generated_config_info.png)

Environment variables can be added before or during application creation.

After successful app installation site shows default web server response.
![image of default python app response](/readme_assets/deployment/it_works.png)


2. installing dependencies

* From a terminal as a user (not root) activate virtual environment and change directory to the &lt;project root&gt;.
* in virtual environment execute '''pip install -r requirements.txt'''. That will install 
all packages. If there is a problem with psycopg2 installation, in requirements.txt file change psycopg2
to psycopg2-binary. That will avoid errors.

3. building a database

PostgreSQL database server should be installed and available in cPanel. This is a high level 
guide as these tasks are not project specific.
* Create a database by pressing Databases section button PostgreSQL Database Wizard or postgreSQL Databases.
* Create a database user from PostgreSQL databases interface.
* Grant database user access rights (see above) using phpPgAdmin application (web interface).

***!NB*** button names can be different but still meaningful.

* Finalise environment variable's setup in Python application interface.
* in terminal issue command '''python manage.py makemigrations'''. If there are errors, most likely these 
are due to database user has insufficient privileges to database ane/or schema PUBLIC.
* in terminal issue command '''python manage.py migrate'''
* Once migration is finished create administrative 
account with a command '''python manage.py createsuperuser''' and enter all required information.
* restart application.

* Now application should work and have no blogs and no comments.

### Post installation procedures

***Adding the role "Editor"*** 

* open site's admin page (SITE_URL/admin/) and enter superuser's credentials.
* add Group "Editor" and press Save
![adding group "Editor"](/readme_assets/deployment/create_editor_group.png)
* Log out from administration screen.

***Granting role "Editor" to a registered user*** 

* On the site's main screen's top right corner press "Register" and fill all reequired information. That way is registered user created.
* Log into admin screen choose user and enter edit screen.
* Find section "Add group"
* on the left box select "Editor"
* press arrow pointing to the right.
* Press Save
![User as an "Editor"](/readme_assets/deployment/make_user_editor.png)


# References

# Bibliography

