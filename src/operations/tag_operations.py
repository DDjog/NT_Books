
from src.database.models import Tag
from src.database.db import session

def add_tag(new_tag):
    tag = session.query(Tag).filter_by(tag=new_tag).first()

    if not tag:
        tag = Tag(tag=new_tag)
        session.add(tag)
        session.commit()
        print(f'Tag {new_tag} was added.')
    else:
        print(f'Tag {new_tag} already exists.')

def get_tag(ta):
    tag = session.query(Tag).filter_by(tag=ta).first()

    if tag:
        print(f'Tag: {ta}, ID: {tag.id}')
    else:
        print(f':Tag {tag} was not found')

def get_tags_list():
    tags_list = session.query(Tag).all()

    if tags_list:
        print(f'Tags list:')
        for tag in tags_list:
            print(f'ID: {tag.id}, Tag: {tag.tag}')
        return tags_list
    else:
        print('Tags list is empty')
        return None

def update_tag(tag, updated_tag):
    tag = session.query(Tag).filter_by(tag=tag).first()

    if tag:
        tag.tag = updated_tag
        session.commit()
        print(f'Tag: {id} {tag} was updated to {updated_tag}.')
    else:
        print(f'Tag {tag} was not found.')

def delete_tag(tag):
    tag = session.query(Tag).filter_by(tag=tag).first()

    if tag:
        _id=tag.id
        session.delete(tag)
        session.commit()
        print(f'Tag: {_id} {tag} was deleted.')
    else:
        print(f'Tag {tag} was not found.')


