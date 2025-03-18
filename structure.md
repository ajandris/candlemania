CandleMania table description
=============================

## Table: blog_comments
Table comment: Blogs Post Comments


### Primary Key: 
"blog_comments_pkey" on column "id"

### Foreign Key constraints: 

"blog_comments_author_id_883440ef_fk_auth_user_id" FOREIGN KEY (author_id) REFERENCES auth_user(id)

"blog_comments_blog_post_id_174b68b4_fk_blog_posts_id" FOREIGN KEY (blog_post_id) REFERENCES blog_posts(id)

### Columns
| |Column Name|Data Type| Key | Description             |
|---|---|---|-----|-------------------------|
|1|id|bigint | YES |                         |
|2|content|text |     | Comment                 |
|3|approved|boolean |     | Comment Approval status |
|4|created_at|datetime |     | Created at              |
|5|updated_at|datetime |     | Updated at              |
|6|author_id|integer |     | Comment author          |
|7|blog_post_id|bigint |     | Blog Post               |


## Table: blog_posts
Table comment: Blogs Posts


### Primary Key: 
"blog_posts_pkey" on column "id"


### Unique Key: 
"blog_posts_slug_key" on column "slug"

### Foreign Key constraints: 

"blog_posts_author_id_6f561d00_fk_auth_user_id" FOREIGN KEY (author_id) REFERENCES auth_user(id)

### Referenced-by: 

TABLE "blog_posts" CONSTRAINT "blog_comments_blog_post_id_174b68b4_fk_blog_posts_id" FOREIGN KEY (id) REFERENCES blog_comments(blog_post_id)

### Columns
| |Column Name|Data Type| Key | Description          |
|---|---|---|-----|----------------------|
|1|id|bigint | YES |                      |
|2|title|varchar(250) |     | Blog title           |
|3|content|text |     | Blog post            |
|4|slug|varchar(255) |     | Blog post slug       |
|5|approved|boolean |     | Blog Approval status |
|6|created_at|datetime |     | Created at           |
|7|updated_at|datetime |     | Updated at           |
|8|author_id|integer |     | Author               |
