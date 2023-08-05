# Why Inspired Ink?
The thought behind Inspired Ink is to invite creative minds with an itch for expressing themselves in writing to get those ideas down on 'paper', so to say, while also prodiving the opportunity to enjoy fellow writers work and leave comments or feedback.

With many forums for writing singling out a specific kind of creative writing, say fiction or poems, Inspired Ink offers a wider variety of categories for your work so that you don't have to search for one site per category. This makes it easier for beginners and master alike to share their work in one single space as well as for others to find a varied asortment of works without having to scour the internet depending on what they're looking for.

#

- [Introduction](#introduction)
    - [User Goals](#user-goals)
    - [Site Goals](#site-goals)
- [Agile and User stories](#agile-and-user-stories)
- [Scope](#scope)
- [Wireframes](#wireframes)
- [Design](#design)
    - [Colors](#colors)
    - [Fonts](#fonts)
- [Features](#features)
- [Structure](#structure)
- [CRUD](#crud)
- [Testing](#testing)
    - [Validator](#validator-testing)
    - [Code](#code)
    - [No errors](#no-errors)
    - [Errors](#errors)
        - [Accessability](#accessability)
    - [Manual testing](#manual-testing)
- [Bugs](#bugs)
- [Future implements - nice to have](#future-implements---nice-to-haves)
- [Deployment](#deployment)
- [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Frameworks](#frameworks)
    - [Tools](#tools)
    - [Libraries](#libraries)
    - [Packages](#packages)
- [Resourses](#resourses)
    - [Assisting](#assisting)
    - [Images](#images)
    - [Icons](#icons)
    - [Sources for example posts](#sources-for-example-posts)
    - [Credits](#credits)

# Introduction

## User goals
- To join a community of like-minded creative writers
- To share my writing and interract with other's writing
- To get inspiration from other's writing to try something new, like a haiku for the first time
- To learn about types of creative writing from fellow writers by viewing their work

## Site goals
The goal of Inspired Ink is to provide writers from all different skill-levels to have a place to express themselves without feeling the preassure of comparing themselves to the grand minds of poetry or novel sites, where famous writers are often quoted or used as inspiration.

Writing doesn't have to be complicated or up to a certain standard, which is what I want to offer with Inspired Ink; a basic, age-less, relaxed place to write down whatever creative blurb floating around your head and categorize it the best you can.

# Agile and User Stories
The baseline of my User Stories are collected in an Excel file that I then transferred into a Github Project that uses an agile approach. See [Here](https://github.com/users/AuroraStorm-sw/projects/7) for the full project.

Each User Story is made up of an Epic, Acceptance critera, and a number of tasks, each User Story being tagged with either "must have" and/or "nice to have". I decided to collect all "must have" and "nice to have" tasks in the same User Story to keep it nice and neat.
To view all User Stories, please see the above link.

# Scope
For the site to reach its full potential for a user, these features are included in the release:

# Wireframes

I began with very little inspiration for the layout of the webpage, knowing only what it should look like when viewing an Ink, and that the home page should have an introductionary part followed with posts.

Throughout the project, and from browsing the internet for different examples of poetry and creative writing websites, I settled for something uncomplicated, seeing the, in my opinion, cluttered examples in the wild. I want the focus to be on the submitted stories and poems, and nothing more.

<details>
<summary>View Wireframes</summary>
<br>

![Post](https://res.cloudinary.com/dg4yefryk/image/upload/v1691147698/post_d3jc7l.png)

![Home](https://res.cloudinary.com/dg4yefryk/image/upload/v1691146803/home_yl07ap.png)

![Account](https://res.cloudinary.com/dg4yefryk/image/upload/v1691146802/account_e88rih.png)
</details>
<br>

# Design

The overall idea for the design was based on parchment - old, stained brown parchment which gives a bit of an old cozy feeling without coming across as pretentious. 
The issue I find with some blogs and forums for creative writing is that they can portray this sense of professionalism that scares beginners away from joining in on writing, which is something I don't want on my website. 
I want it to feel welcoming and homey, which is another reason for the choice of colors and layouts.

Given the name of the website, I decided to implement a few drops of ink here and there, mainly for the logo and for user to "ink" a post in the same way you "like" a post, giving the webpage a bit more character and staying true to its name.

No more endless scrolling through cluttered pages overflowing with thin lines of post links; no more uncomfortable brightness that has you reaching for sunglasses; this webpage offers calming nuances of brown with a splash of color.

## Colors
I based the colors around the background image and used [Coolors](https://coolors.co) to create a palette based on one of the nuances. 

![Palette](https://res.cloudinary.com/dg4yefryk/image/upload/v1691166288/palette_e1c8em.png)

From this palette, I ended up focusing on the colors #3a2202 and #b96e46, and a few details of #774605. With black text on top of these reddish brown colors pop enough to make the font visible, but not without taking away from the calm vibes.

## Fonts

For fonts I ended up with Inkut Antiqua for main headers and links. I searched for "Ink" on [Google Fonts](https://fonts.google.com) and stumbled across this font by accident, but felt immediately that it fits the vibe of my website.

![Inkut](https://res.cloudinary.com/dg4yefryk/image/upload/v1691167044/font-inknut_yimden.png)

For paragraphs, I picked Roboto, which is a very casual font that works well together with Inkut that stands out as a more expressive font, and I found these two to compliment each other nicely.

![Roboto](https://res.cloudinary.com/dg4yefryk/image/upload/v1691167044/font-roboto_dfxcrd.png)

# Features
- Home page
    - Navbar

    The navbar consists of a basic Bootstrap navbar with tabs and a dropdown for categories that includes a hamburger menu for smaller viewports.
    When logged in, the user can navigate between the home page, available categories, create a new ink, or sign out.
    For users without an account or who aren't logged in, they can navigate between the home page, available categories, sign in, or create an account.
    The logo also serves as a link back to the home page.

    ![Image](https://res.cloudinary.com/dg4yefryk/image/upload/v1691146805/img-nav_c8igfc.png)

    - Intro

    The home page introduction consists of a few paragraphs of text explaining what the website is about and for whom, inspiring users to create their own Inks and leaving feedback or inkdrops (likes) on others'.

    ![Image](https://res.cloudinary.com/dg4yefryk/image/upload/v1691168745/img-intro_m958o1.png)

    - Inks

    After scouring the internet and Slack for inspiration for the structure of how the posts should be displayed, I ended up taking layout inspiration from [Kathrin's Haiku blog](https://github.com/Kathrin-ddggxh/woohoo-haiku), as they are of perfect size for cards displaying little information, compared to a lot of other blogs that need bigger cards that often includes images. With this Bootstrap card layout, the posts are responsive in all sizes, and stack prettily on smaller screens without sacrificing any text.

    Adding to the layout, I found a watercolor-esque wallpaper that I faded to a lighter opacity for the background, adding to an inky feel.

    ![Image](https://res.cloudinary.com/dg4yefryk/image/upload/v1691146806/img-posts_yiuvph.png)

    - Footer

    The footer is very basic and straight-forward, offering links to social media.

    ![Image](https://res.cloudinary.com/dg4yefryk/image/upload/v1691146804/img-footer_aazqge.png)

- Create a new Ink
    - Write

    The layout for the form to write an Ink is kept very simplistic, as creating an Ink should't feel like rocket science. It consists of an author input, category, title, an excerpt if the user feels like adding one, and then the main content. Below are two buttons, one for submitting the Ink and once for cancelling, which returns the user to the home page.

    ![Image](https://res.cloudinary.com/dg4yefryk/image/upload/v1691146805/img-create_sfsiwh.png)

    - Edit Ink

    Similarly to the Create a new Ink page, the Edit page is very simplistic. The user can update the title, excerpt, and main content. There are two buttons below, one for updating the Ink, and one for cancelling out of edit mode. This can only be accessed by the author of the Ink.

    ![Image](https://res.cloudinary.com/dg4yefryk/image/upload/v1691147794/img-update_jxgaif.png)

    - Delete Ink

    Should the user decide to delete an Ink, they'll be directed to a page where they are asked to confirm if they with to delete it or not, giving them the options to go ahead and delete their Ink, or cancel out and return to the home page.

    ![Image](https://res.cloudinary.com/dg4yefryk/image/upload/v1691146804/img-delete_j7e422.png)

- Category Archive

    - Category

    When browsing the category list, each Ink within that category is displayed in the same way as those on the Home page, making it easy to browse between them.

    ![Image](https://res.cloudinary.com/dg4yefryk/image/upload/v1691147906/img-category_swghga.png)

- Account
    - Create account

    The create account section is, like everything else, kept as simplistic as possible to make the process quick and easy, with a basic structure.

    ![Image](https://res.cloudinary.com/dg4yefryk/image/upload/v1691146805/img-create-account_ugtqsx.png)

    - Sign in

    As with Account Creation, signing in is just as easy, offering only what's needed. 

    ![Image](https://res.cloudinary.com/dg4yefryk/image/upload/v1691146742/img-sign-in_a3hyn0.png)
    

    - Sign out

    When the user signs out, they'll be directed to a page asking them if they're sure to sign out, giving them the option to proceed with the sigh out or cancel, returning them to the home page.

    ![Image](https://res.cloudinary.com/dg4yefryk/image/upload/v1691171483/signout_vbjwku.png)


# Structure

## CRUD

- Create: An authenticated user can create and submit an Ink post.
- Read: A user can browse all the posted Inks.
- Update: An authenticated user can edit their own submitted Ink posts.
- Delete: An authenticated user can delete their own submitted Ink posts.

## Custom model

The Ink and Feedback models are both based on the [Code Institute Courseware](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FST101+2021_T1/courseware/b31493372e764469823578613d11036b/dabfed30d1fc4d078b6de270117dbe50/) for I Think Therefore I Blog, with modification to both the models and the visual result to better fit the project.

The Comment model is a custom model not included in the courseware.


# Testing

## Validator

## Code

[W3 HTML checker](https://validator.w3.org)

All pages of the website has been run through W3, with two of them coming out with seemingly false positive results.

## No errors

<details>
<summary>View all results with no errors.</summary>
<br>

- Sign in

![SignIn](https://res.cloudinary.com/dg4yefryk/image/upload/v1691147698/test-login_fl1u4l.png)

- Sign out

![SignOut](https://res.cloudinary.com/dg4yefryk/image/upload/v1691147698/test-sign-out_s9dhoi.png)

- Sign up

![SignUp](https://res.cloudinary.com/dg4yefryk/image/upload/v1691147698/test-signup_bftkjh.png)

 - Home page

![Home](https://res.cloudinary.com/dg4yefryk/image/upload/v1691147698/test-home_rwd4lx.png)

 - Add new ink

![AddInk](https://res.cloudinary.com/dg4yefryk/image/upload/v1691147698/test-add-ink_tq3a5e.png)

 - View Ink post

![Category](https://res.cloudinary.com/dg4yefryk/image/upload/v1691147698/test-category_w6bujd.png)

- Delete Ink

![InkDelete](https://res.cloudinary.com/dg4yefryk/image/upload/v1691147698/text-delete_jhahvj.png)
</details>

## Errors

The errors have been documented into their separate Issue [Here #12](https://github.com/AuroraStorm-sw/Inspired-Ink/issues/12).

## [CI Python Linter](https://pep8ci.herokuapp.com/)

Each .py file has been passed through the linter with very few errors; those coming up were in regards to trailing whitespace, missing space, and missing new line at the end of the code. These were all easily fixed, and the files are now free of errors.

![linter](https://res.cloudinary.com/dg4yefryk/image/upload/v1691147698/linter-test-model_hslsux.png)


## [JSHint]([https://jshint.com/])

![https://jshint.com/](https://res.cloudinary.com/dg4yefryk/image/upload/v1691180009/test-javascript_e99aqr.png)


### Accessability

## [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/)

![Lighthouse](https://res.cloudinary.com/dg4yefryk/image/upload/v1691159942/lighthouse_eipqg2.png)

## [Axe DevTools](https://chrome.google.com/webstore/detail/axe-devtools-web-accessib/lhdoppojpmngadmnindnejefpokejbdd)

![AxeDevtools](https://res.cloudinary.com/dg4yefryk/image/upload/v1691160050/axe-devtools_nary38.png)

## [WAVE](https://wave.webaim.org/)
![WAVE](https://res.cloudinary.com/dg4yefryk/image/upload/v1691164948/wave_dxpdvl.png)


## Manual testing

| Action           | Expected Result                                                                                                                                | Pass |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------|------|
| Account creation | I can create a new account with username and password, and be notified that it's created successfully, or if not                               | Pass |
| Sign in          | I can sign in with my username and accound and get notified that I've been successfully signed in                                              | Pass |
| Sign out         | When signed in, I can sign out of the webpage, be asked if I'm sure I want to sign out, and be notified that I've been successfully signed out | Pass |
| Navbar           | Each link in the navbar takes me to the correct corresponding page. There are different paged depenting on if I am signed in or not.           | Pass |
| Create post      | When signed in, I can write an 'Ink', being a cretive text of my choice, and submit it. I'll be notified that it's successfully submitted.     | Pass |
| Edit post        | When signed in, I can edit my own posts, and be notified that it has been successfully edited                                                  | Pass |
| Delete post      | When signed in, I can delete my own posts, be asked if I'm sure I want to delete it, and be notified that it has been successfully deleted     | Pass |
| Comment on post  | When signed in, I can leave feedback on other's posts. My comment is then visible beneath the post.                                            | Pass |
| Like/unlike post | When signed in, I can like and unlike other's posts. The icon changes                                                                          | Pass |
| Category         | I can browse different categories via the navbar                                                                                               | Pass |
| Pagination       | I can browse through multiple pages on the home page if there are more than six posts                                                          | Pass |
| Links            | All of the links throughout the page are fully functional                                                                                      | Pass |
| Buttons          | All of the buttons direct me to their designated function                                                                                      | Pass |
| Footer           | I can reach the different social medias sites via the footer, and they all open in new tabs.                                                   | Pass |


# Bugs
1. Lingering 'missing data' in category table after migrating the category model and category addition to Post without creating a category index.
Solution: Reset the database to remove the error and recreate superuser.

2. Static files not loading on Heroku.
Solution: Through tutor support, they found a spelling error in loading style.css in base.html after a lot of trial and error.

# Future implements - nice to haves

- Add a word counter to the Ink posts so users can see how long the posts are in the post overview. This idea was laid to the side due to deadline.
- Add a short backstory about each writing styles' origin on the category pages.

# Deployment

Github

Steps I took to deploy my website;

1. Go to the repository for Inspired-Ink
2. Click the Settings tab and locate the Pages tab
3. Select to deploy from main branch
4. A few minutes later, upon refreshing the page, my site was live

For anyone wishing to Fork this repository, then do as follows;

1. Log in to GitHub and find your way to the GitHub repository you want, in this case, my Inspired Ink project
2. Up in the right corner of the repository page, on the row of buttons just beneath the user icon, you'll find the "Fork" button.
3. Click the "Fork" button, and you will now have created a copy of the repository to your GitHub account.

To clone this repository, then do as follows;

1. Log in to GitHub and find your way to the GitHub repository you want, in this case, my portfolio project 3 Click the "<> Code" button in the upper right above the files
2. Copy the link
3. Open Gitpod and from there, select which directory you want the clone to be created into.
4. Type in "git clone" in your Gitpod terminal and paste the link copied from GitHub, and the close will be created.

Deploying the app in Heroku:

This was done with the help of instructions from Code Institute, and goes as follows;

To properly deploy with Heroku, I've used the Code Institute Python Essentials Template that is set up to let the code that is used in the terminal to be viewed in the browser.

1. Log in to Heroku or create a new account
2. On the main page up near the top, click "New" and select "Create new app"
3. Pick your unique app name and select your region
4. Click the "Create App" button
5. On the next page, manover to the "Settings" tab and find "Config Vars"
6. Click "Reveal Config Vars" and add "Port" to key and "8000" to value, then click "Add"
7. Scroll down the page to "Buildpack" and click "Add", then select "Python"
8. Repeat an add "node.js" and make sure they're in that order, with Python first
9. Scroll back up and click the "Deploy" tab
10. Here, you select "GitHub" as deployment method and search for your repository to link them together
11. Scroll down the page and select if you want to "Enable Automatic Deploys" to automatically deploy your pushes from GitHub to Heroku.

# Technologies Used

## Languages
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/CSS)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Javascript](https://en.wikipedia.org/wiki/JavaScript)

## Frameworks
- [Django](https://www.djangoproject.com/) - The main Python framework used to develop this project.
- [Bootstrap](https://getbootstrap.com/) - For general layouts and responsiveness across the site.
- [ElephantSQL](https://www.elephantsql.com/) - The production database used for the project.
- [GitHub](https://github.com/) - Used to host the source code.
- [Gitpod](https://gitpod.io/) - Used to commit, comment, and push code throughout the project.
- [Heroku](https://www.heroku.com) - Used for app deployment.
- [Balsamiq](https://balsamiq.com/) - For creating wireframes for the project.
- [Cloudinary](https://console.cloudinary.com) - For storing all static files and images.

## Tools
- [JsHint](https://jshint.com/) - For validating Javascript code
- [CI Python Linter](https://pep8ci.herokuapp.com/#) - For validating Python code
- [W3C HTML Validator](https://validator.w3.org/) - For validating HTML code
- [Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/) - For validating CSS code
- [Chrome Developer Tools](https://developer.chrome.com/docs/devtools/) - Developer tool used throughout the project for bug fixing and error searching
- [Axe DevTools](https://chrome.google.com/webstore/detail/axe-devtools-web-accessib/lhdoppojpmngadmnindnejefpokejbdd) - A developer tool for validating accessability
- [HTMLHint](https://htmlhint.com/) - Static code analysis tool for HTML
- [Lighthouse](https://developer.chrome.com/docs/lighthouse/) - For accessability validation
- [WAVE](https://wave.webaim.org/) - For accessability and contrast validation
- [Grammarly](https://app.grammarly.com/) - Used to spell and grammar check the ReadMe

## Libraries
- Gunicorn - The server used for running Django on Heroku
- pyscopg2 - Used to connect to PostgreSQL
- Cloudinary - Used to host static files and images
- Whitenoise - Helps sort out issues with Heroku not rendering custom CSS stylesheet

## Packages

- Django - An MVP, model-template-view, Python-based web framework, used for building projects.
- django-allauth - Used for account registration, managing signing in and out, and authentication.
- cloudinary_storage - Storage backend for Cloudinary that is used for static storage.
- django_summernote - Integrates Summernote WYSIWYG editor into Django projects. This package is installed but ended up not being used in the project.
- crispy_forms - Makes styling Django forms easier.

# Resourses

## Assisting
- [Table Converter](https://tableconvert.com/) - for Manual Testing structuring.
- [Tinypng](https://tinypng.com/) - for compressing background image.
- [Coolors](https://coolors.co) - for generating a color palette.
- [Google Fonts](https://fonts.google.com) - for browsing and implementing fonts.

## Images
- [Background image](https://www.pexels.com/photo/empty-brown-canvas-235985/)
- [Quote image](https://abstract.desktopnexus.com/get/1737801/?t=146uo7bue09b2o59gjgv030rd364ccdb5086d33)
- [Ink Card Image](https://wallpapercave.com/w/wp1938057)

## Icons
- https://icon-sets.iconify.design/mdi/ink/
- https://icon-sets.iconify.design/mdi/ink-plus/
- https://icon-sets.iconify.design/mdi/ink-plus-outline/
- https://icon-sets.iconify.design/material-symbols/comment/

## Sources for example posts
- [Poem by Sappho](https://ozofe.com/sappho/to-atthis-the-inconstant/)
- [Poem by Maya Angelou](https://ozofe.com/maya-angelou/on-aging/)
- [Heiku by Ezra Pond](https://reedsy.com/discovery/blog/haiku-poem-examples)
- [Part of the lyrics to War by Poets Of the Fall](https://www.songlyrics.com/poets-of-the-fall/war-lyrics/)
- [The story of an Hour by Kate Chopin](https://americanliterature.com/author/kate-chopin/short-story/the-story-of-an-hour ) 
- [Lyric part of Lie to Me by Riell](https://genius.com/Riell-lie-to-me-lyrics)

# Credits

- [Very Academy](https://www.youtube.com/watch?v=S9-Bt1JgRjQ&list=PLOLrQ9Pn6cawWd-5UZM6CIm0uqFXeBcTd&index=4) - Youtube video guidance on how to add a category model and view for the custom model.
- [Codemy.com](https://www.youtube.com/watch?v=B40bteAMM_M&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi) - A playlist of Youtube videos going through all stages of building a Django blog that I used to browse through to get tips and tricks on how to structure models, views, and urls.
- [StackOverflow](https://stackoverflow.com/) - A forum used throughout the project when searching for solutions for errors or ideas on views or how to add specific functions to the website. Throughout the project, sources have been added to each corresponding piece of code in comments.
- [Slack](https://slack.com/) - A lot of answers to errors and frustrations have been found when browsing issues across different channels.
[Code Institute Courseware](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FST101+2021_T1/courseware/b31493372e764469823578613d11036b/dabfed30d1fc4d078b6de270117dbe50/) - Code Institute coarseware used for the basic structure of the Ink and Feedback/Comment models.
- [Code Institute Template](https://github.com/Code-Institute-Org/gitpod-full-template) - the template used as a base for the project.

- Tutor support
- Course friends