#                            BOOT-CAMP-RATINGS

#                              description
* Boot-camp-ratings is a command line application that is used to give rating on the EPIC   values alignment of Bootcamp candidates during Bootcamp.
* This application caters for three kinds of users. ie; Bootcampers, LFAs AND LFs. 
* The scores range between -2 to 2 i.e (Very Unsatisfied, Unsatisfied, Neutral, Satisfied   and Very Satisfied)


##                          Project Features
*   LFs have the ability to see scores for all the candidates in Bootcamp.
    They however can’t change any of the scores and neither can they add scores. 
*   LFAs have the ability to see scores for all the candidates that are assigned to them      during Bootcamp, add scores for them and edit only their candidate’s scores.
*   Bootcampers can only see the scores they have been given.


#                                 Users
*   Users can be logged in and out.
*   When users log in, the last_seen timestamp should be set.
*   The last time-stamp should not be modified when logging out 

#                                Reports
*   LFs should be able to see which candidates are performing well and those who are not. *   They should also be able to see which candidates haven’t been scored yet for a given      day.

##                              Instalation

* Clone the GitHub repo:
 
` git clone https://github.com/nanfuka/BOOT-CAMP-RATINGS.git`

* cd into the folder and install a Virtual Environment

` virtualenv venv`

* Activate the virtual environment

`venv\scripts\activate`

* Install all application requirements from the requirements file found in the root folder

`$ pip install -r requirements.txt`

* Start Server 

`python app.py`.


## Contributors
* [Eric](https://github.com/ekumamait)
* [Mozy](https://github.com/mozzy22)
* [Josh](https://github.com/joshtrigger)
* [Anord](https://github.com/ramzinc)
* [Felix](https://github.com/felixkiryowa)
* [Peace](https://github.com/peace-apple)
* [Debbie](https://github.com/nanfuka)

## How to Contribute
1. Download and install Git
2. Clone the repo `git clone https://github.com/nanfuka/BOOT-CAMP-RATINGS.git`
3. Push your contributions to the feature- branch. do not merge
