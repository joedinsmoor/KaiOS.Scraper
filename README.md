# SQLite Scraper
Custom SQLite Scraper for use with KaiOS SQLite extractions

- Only for use on extractions of SQLite DBs pulled from KaiOS based cell phones 
- Pulls hex data from object_data table of imported db
- Removes extraneous data from row, and prints in human readable format
- Exports scraped phone numbers to 'phone_numbers.log'
- Logs output to 'run.log'


*Installation*
- run `python pip install -r requirements.txt`
- all dependencies are now installed, run with `python3 sqlite_scraper.py`

*Coming Soon*

- Efficiency Optimizations
- Setup and installation configurations
- Export cell phone numbers to csv, as well as messages between contact and owner of phone number

*Future Features*

- Ability to handle images, and recover them
- Ability to eventually handle all SQLite DBs, not just extracted from KaiOS
