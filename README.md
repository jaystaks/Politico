[![Build Status](https://travis-ci.org/jaystaks/Politico.svg?branch=develop)](https://travis-ci.org/jaystaks/Politico)[![Coverage Status](https://coveralls.io/repos/github/jaystaks/Politico/badge.svg?branch=develop)](https://coveralls.io/github/jaystaks/Politico?branch=develop)[![BCH compliance](https://bettercodehub.com/edge/badge/jaystaks/Politico?branch=develop)](https://bettercodehub.com/)[![Codacy Badge](https://api.codacy.com/project/badge/Grade/051d0de852644006aa0c3e9823d37b46)](https://www.codacy.com/app/jaystaks/Politico?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=jaystaks/Politico&amp;utm_campaign=Badge_Grade)[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-371/)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Maintainability](https://api.codeclimate.com/v1/badges/7340d568a0b95fecccbe/maintainability)](https://codeclimate.com/github/jaystaks/Politico/maintainability)

# Politico
Project Overview The general elections are around the corner, hence it’s a political season. Get into the mood of the season and help build a platform which both the politicians and citizens can use. Politico enables citizens give their mandate to politicians running for different government offices while building trust in the process through transparency.


## DOCUMENTATION
**[API End points documentation](https://politico1.docs.apiary.io/#)

## Endpoints - Features

**Endpoint** | **Request**| **Description**
--- | --- | ---
`/api/v1/parties` | `POST` | Create a political party
`/api/v1/parties` | `GET`| Fetch all political parties
`/api/v1/parties/<int:id>` | `GET` |   Fetch a specific political party
`/api/v1/parties/<int:id>` | `DELETE` |   Delete a specific political party
`/api/v1/<int:id>/name` | `PATCH` | Edit a political party
`/app/api/v1/offices` | `POST`| Create Political office
`/api/v1/offices` | `GET` | Fetch all political offices
`/api/v1/offices/<int:id>` | `GET` | Fetch a specific offices

## Manually tested
Go to github and clone repo https://github.com/jaystaks/Politico, switch to develop branch

-  Make sure to have the python _virtualenv_ if not `pip install virtualenv`
-  Create the env with this command `virtualenv venv`
-  For linux type this on the terminal `source venv/bin/activate`
-  Install the packages from the requirements.txt by using this commands `pip install -r requirements.txt`
-  And finally run` flask run`




