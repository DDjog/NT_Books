
from src.database.models import Tag
from src.database.db import session

def add_tag(tag_name):
    tag = session.query(Tag).filter_by(tag=tag_name).first()

    if not tag:
        tag = Tag(tag=tag_name)
        session.add(tag)
        session.commit()
        print(f'Tag: {tag_name} was added.')
    else:
        print(f'Tag: {tag_name} already exists.')

def is_tag_in_db(tag_name):
    tag = session.query(Tag).filter_by(tag=tag_name).first()

    if tag:
        _id = tag.id
        print(f'ID: {_id}, Tag: {tag_name}')
        return True
    return False

def get_tags_list():
    tags_list = session.query(Tag).all()

    if tags_list:
        print(f'Tags list:')
        for tag in tags_list:
            _id = tag.id
            print(f'ID: {_id}, Tag: {tag.tag}')
        return tags_list
    return None

def update_tag(old_tag_name, updated_tag_name):
    tag = session.query(Tag).filter_by(tag=old_tag_name).first()

    if tag:
        tag.tag = updated_tag_name
        session.commit()
        _id = tag.id
        print(f'ID: {_id}, Tag: {old_tag_name} was updated to {updated_tag_name}.')
    else:
        print(f'Tag: {old_tag_name} was not found.')

def delete_tag(tag_name):
    tag = session.query(Tag).filter_by(tag=tag_name).first()

    if tag:
        _id=tag.id
        session.delete(tag)
        session.commit()
        print(f'ID: {_id}, Tag: {tag_name} was deleted.')
    else:
        print(f'Tag: {tag_name} was not found.')


