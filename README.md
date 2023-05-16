# SQLite Scraper
Custom SQLite Scraper for use with KaiOS SQLite extractions

- Only for use on extractions of SQLite DBs pulled from KaiOS based cell phones 
- Pulls hex data from object_data table of imported db
- Removes extraneous data from row, and prints in human readable format
- Exports scraped phone numbers to 'phone_numbers.csv'
- Logs output to 'run.log'
- Exports phone numbers to csv file (thanks to [@phoenixrising1800](https://github.com/phoenixrising1800))


**Installation**
- run `python3 pip install -r requirements.txt`
- all dependencies are now installed, run with `python3 sqlite_scraper.py`

**Coming Soon**

- Efficiency Optimizations
- Setup and installation configurations
- Geolocation tagging with relevant connections to event logs using Google Earth
- Timestamp recording with events tied to timestamps

*Future Features*

- Ability to handle images, and recover them
- Ability to eventually handle all SQLite DBs, not just extracted from KaiOS

Feel free to dm me on twitter [![Twitter URL](https://img.shields.io/twitter/url/https/twitter.com/joedinsmoor.svg?style=social&label=Follow%20%40joedinsmoor)](https://twitter.com/joedinsmoor) with any questions or feature requests!
