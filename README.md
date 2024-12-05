Candle Mania
=================

Link to production site: 

# Introduction

The Candle Mania is a sample site for publishing blogs about candles and candle-related products.

The site has two parts: blogs and affiliated products.

## Users

There are four categories of users: a visitor, a registered user, an admin and a superuser.

A **visitor** can browse products and view each product's details.

A **registered user** can do everything a visitor can and add, edit, and delete its products. It can change its name, surname and password in the profile section.

An **admin** can add, edit and delete catalogue items.

A **superuser** can appoint a registered user to admin.

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

This project's intended audience is anyone who is interested into information about candles and wants to by some 
candles and their accessories.

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
  * [US-V01] browse all items
  * [US-V02] have a paginator when there are more than 20 items on a page in list mode
  * [US-V03] sort items by name
  * [US-V04] filter items by categories
  * [US-V05] search items and categories by a phrase (classic search)
  * [US-V06] see item details
  * [US-V07] have a link to a marketplace to buy a product
* as a registered user I need to
  * [US-RU01] be able to do the same a visitor
  * [US-RU02] have a login page
  * [US-RU03] have a profile where I can change password and a name
  * [US-RU04] add product
  * [US-RU05] update my product
  * [US-RU06] delete my product
  * [US-RU07] list my products
  * [US-RU08] write a blog
  * [US-RU09] comment a blog
  * [US-RU10] delete my profile
* as an admin I need to
  * [US-A01] be able to do the same as a registered user
  * [US-A02] list categories
  * [US-A03] add category
  * [US-A04] delete category if there is no product listed on that category
  * [US-A05] update category name
  * [US-A06] approve blog
  * [US-A07] approve blog comments
  * [US-A08] delete blog comments
  * [US-A09] approve product feedback
  * [US-A10] delete product feedback
* as a superuser I need to
  * [US-SU1] list all registered users
  * [US-SU2] grant registered user an admin role
  * [US-SU3] revoke admin the admin role
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



**Entity-Relationship Diagrams** (ERD) show relationship between [data] entities. It is a starting point of a database design 
and it affects site's navigation and design.


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
GRANT USAGE ON SCHEMA public TO myuser;
GRANT CREATE ON SCHEMA public TO myuser;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO myuser;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO myuser;
```

## Environment variables
Environment variables for development are set in env.py file. For the production environment those should be set
on web server during deployment. The development environment is set on a local computer with postgresql installed.

**The list of environment variables:**
```
# security
os.environ.setdefault('SECRET_KEY', '<THE KEY FROM INITIAL SETTINGS.PY FILE>')
os.environ.setdefault('DEBUG', 'True')
os.environ.setdefault('ALLOWED_HOSTS', 'localhost, 127.0.0.1') # list of allowed hosts

# database
os.environ.setdefault('POSTGRES_USER', 'myuser')
os.environ.setdefault('POSTGRES_PASSWORD', 'mypassword'),
os.environ.setdefault('POSTGRES_HOST', 'localhost'),
os.environ.setdefault('POSTGRES_PORT', '5432'),
os.environ.setdefault('POSTGRES_DATABASE_NAME', 'mydatabase')
```
The secret key is copied from initial settings.py file. If you do not have it create a temporary django app, 
copy the key and destroy that django app.


# References

# Bibliography

