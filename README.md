# Shortly

[Shortly](https://flask-shortly.herokuapp.com) is a online service for shortening and extending URLs made with Flask.
[Live Preview](https://flask-shortly.herokuapp.com)
## Usage

- The homepage "Shorten" allows you to type any (active) valid URL into the inputbox and compress it to a path made of 6 random latters and/or numbers
- The "Extand" page allows you to enter a URL which has already been shorted and show where they point to. (The extending works with internal aswell as external Links)
- The "About" page contains information about the Project

## Features
- The Application checks, whether a URL has been already shorted and provides already existing links to save space.
- The URL gets formatted into proper format before being shortened
- The generated Links do not have an expiration date

## Issues
- Since the application is being hosted on a free platform, the domain is pretty long.
- The database has a size limit due to the hoster so after a while the application might not create new links
- The database is easily accessible, since this is an open source project only made for demonstration

The issues can be adressed by hosting the application properly on a dedicated private server.