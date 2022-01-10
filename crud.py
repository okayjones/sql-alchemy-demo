### crud.py ###
import fire
from sqlalchemy import create_engine
from config import DATABASE_URI
from models import Base, Note
from sqlalchemy.orm import sessionmaker
from sqlalchemy import update

engine = create_engine(DATABASE_URI)

Session = sessionmaker(bind=engine)


def create_database():
    print('\n*********************')
    print('Creating all tables...')
    Base.metadata.create_all(engine)
    print('Done!')
    print('*********************\n')    


def destroy_database():
    print('\n*********************')
    print('Dropping all tables...')
    Base.metadata.drop_all(engine)
    print('Done!')
    print('*********************\n')

def recreate_database():
    print('\n*********************\n')
    print('Dropping all tables...')
    Base.metadata.drop_all(engine)
    print('Done!')
    print('Creating all tables...')
    Base.metadata.create_all(engine)
    print('Done!')
    print('*********************\n')


def add_note(name, desc):
    note = Note(name=name, description=desc)
    
    print('\n*********************\n')
    
    print('Opening DB session...')
    s = Session()
    print('Ready!')
    
    print('\nAdding and committing note...')
    s.add(note)
    s.commit()
    print('Successfully Added: ', note, '\n')

    
    print('Closing DB session...')
    s.close()
    print('DB session closed!')
    print('*********************\n')

def update_note(name, new_name):
    print('\n*********************\n')
    print('Opening DB session...')
    s = Session()
    print('Ready!')
    
    print('\nUpdating note...')
    update_stmt = (
        update(Note).where(Note.name == name).
        values(name=new_name).
        returning(Note.id, Note.name)
    )
    result = s.execute(update_stmt)
    result = result.fetchall()
    s.commit()
    print('Successfully Updated: ', result, '\n')

    
    print('Closing DB session...')
    s.close()
    print('DB session closed!')
    print('*********************\n')


if __name__ == '__main__': 
    fire.Fire()

    # poetry shell
    # python crud.py recreate_database
    # python crud.py add_note 'Library Demo' 'Learn SQLAlchemy and demo it'