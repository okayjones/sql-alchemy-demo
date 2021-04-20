# Sql Alchemy  Demo

## Setup

1. Install dependencies `poetry install`
2. Add .env with your `DATABASE_URI`
3. Activate virtual env `poetry shell`
4. Create the database `python crud.py recreate_database`
5. Add a note`python crud.py add_note 'Library Demo' 'Learn SQLAlchemy and demo it'`

> See crud.py for additional methods