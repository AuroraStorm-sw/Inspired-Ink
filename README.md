# Introduction

## Why Inspired Ink?
The thought behind Inspired Ink is to invite creative minds with an itch for expressing themselves in writing to get those ideas down on 'paper', so to say, while also prodiving the opportunity to enjoy fellow writers work and leave comments or feedback.

With many forums for writing singling out a specific kind of creative writing, say fiction or poems, Inspired Ink offers a wider variety of categories for your work so that you don't have to search for one site per category. This makes it easier for beginners and master alike to share their work in one single space as well as for others to find a varied asortment of works without having to scour the internet depending on what they're looking for.

## Site goals
The goal of Inspired Ink is to provide writers from all different skill-levels to have a place to express themselves without feeling the preassure of comparing themselves to the grand minds of poetry or novel sites, where famous writers are often quoted or used as inspiration.

Writing doesn't have to be complicated or up to a certain standard, which is what I want to offer with Inspired Ink; a basic, age-less, relaxed place to write down whatever creative blurb floating around your head and categorize it the best you can.

# Agile and User Stories
The baseline of my User Stories are collected in an Excel file that I then transferred into a Github Project that uses an agile approach. See (Here)[https://github.com/users/AuroraStorm-sw/projects/7]

Each User Story is made up of an Epic, Acceptance critera, and a number of tasks, each User Story being tagged with either "must have" and/or "nice to have". I decided to collect all "must have" and "nice to have" tasks in the same User Story to keep it nice and neat.
To view all User Stories, please see the above link.

# Scope
For the site to reach its full potential for a user, these features are included in the release:

# Wireframe

# Datasbase model

# Design
## Colors
## Fonts

# Features
- Home page
    - Navbar
    - Footer
    - Main content
- Create a new Ink
    - Edit Ink
    - Delete Ink
- Category Archive
- Create account
- Sign in/Sign out

# Technologies Used
## Languages
- HTML5
- CSS
- Python
- Javascript
## Django packages
## Frameworks/Libraries

# Credits

## Images
- https://www.pexels.com/photo/empty-brown-canvas-235985/ - Background image

## Icons
- https://icon-sets.iconify.design/mdi/ink/
- https://icon-sets.iconify.design/mdi/ink-plus/
- https://icon-sets.iconify.design/mdi/ink-plus-outline/

## Sources for example posts
- https://ozofe.com/sappho/to-atthis-the-inconstant/ - Poem by Sappho
- https://ozofe.com/maya-angelou/on-aging/ - Poem by Maya Angelou
- https://reedsy.com/discovery/blog/haiku-poem-examples - Haiku by Ezra Pound
- https://www.songlyrics.com/poets-of-the-fall/war-lyrics/ - Part of the lyrics to War by Poets Of the Fall
- https://americanliterature.com/author/kate-chopin/short-story/the-story-of-an-hour - The story of an Hour by Kate Chopin
- https://genius.com/Riell-lie-to-me-lyrics - Lyric part of Lie to Me by Riell

# Testing
## Manual testing


# Bugs
1. Lingering 'missing data' in category table after migrating the category model and category addition to Post without creating a category index.
Solution: Reset the database to remove the error and recreate superuser.

2. Static files not loading on Heroku.
Solution: Through tutor support, they found a spelling error in loading style.css in base.html  after a lot of trial and error.

# Deployment

# Final thoughts