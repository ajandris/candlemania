Product Catalogue
=================

Link to 

# Introduction

The Product Catalogue is a sample site for publishing products.

A site user can publish, update, and delete its products. A user can only see other users' products as a visitor.

Each product has a picture, title, description and an affiliated product link.

There is a category. Each product can be placed into only one category.

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
- PostgreSQL with SQL
- Git
- GitHub
- Grammarly to catch grammar slips and improve the text

## Intended audience

This project's intended audience is anyone who wants insight into a simple product catalogue with user management,
and project assessors and recruiters.

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
  * [US-V1] browse all items
  * [US-V2] have a paginator when there are many items on a page
  * [US-V3] sort items by categories
  * [US-V4] filter items by categories
  * [US-V5] search items and categories by a phrase (classic search)
  * [US-V6] see item details
  * [US-V7] have a link to a marketplace to buy a product
* as a registered user I need to
  * [US-RU1] be able to do the same a visitor
  * [US-RU2] have a login page
  * [US-RU3] have a profile where I can change password and a name
  * [US-RU4] add product
  * [US-RU5] update my product
  * [US-RU6] delete my product
  * [US-RU7] list my products
* as an admin I need to
  * [US-A1] be able to do the same as a registered user
  * [US-A2] list categories
  * [US-A3] add category
  * [US-A4] delete category if there is no product listed on that category
  * [US-A5] update category name
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

Site's development is performed using JetBrain's PyCharm IDE, Python version 3.12 and Flask version 3.0.3.
Site uses the database PostgreSQL v16 for storing data.
Git and GitHub is used for storing code and version control.

## Scope plane
The user stories above show full functionality of the site. However, due to certain circumstances user permission 
functionality can be reduced up to the registered user. 

At the end of development will be delivered:
* Implemented User Stories
* User Manual as a section in README.md file
* Development documentation in README.md file, in particular:
  * Requirements,
  * Functional specifications,
  * Testing process in a separate file,
* Deployment to cPanel hosting.
* Code and version control using Git and GitHub

## Structure plane
The structure plane is concerned with design elements – what will be on pages.

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

# References

# Bibliography

