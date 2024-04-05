import pytest
from blogexample.app import create_app
from blogexample.blueprints.blog.models import Post, Tag, db

def test_index(test_client):
    response = test_client.get('/')
    assert response.status_code == 200

def test_show_posts(test_client):
    response = test_client.get('/posts')
    assert response.status_code == 200

def test_published(test_client):
    response = test_client.get('/blog')
    assert response.status_code == 200

def test_drafts(test_client):
    response = test_client.get('/drafts')
    assert response.status_code == 200

def test_database_interaction(test_client, session):
    # demonstrating direct database interaction
    title= "Database Interaction Test"
    post = Post(title='Database Interaction Test', body='Testing direct db interaction', url=Post.create_url(title), visible=True)
    db.session.add(post)
    db.session.commit()

    fetched_post = db.session.query(Post).filter_by(title='Database Interaction Test').first()
    assert fetched_post is not None
    assert fetched_post.body == 'Testing direct db interaction'

def test_add_post(test_client, session):
    form_data = {"title": "Test Post Title.", "body": "This is a test post", "visible": True}
    response = test_client.post('/add', data=form_data, follow_redirects=True)
    assert response.status_code == 200
    # post = db.session.query(Post).filter_by(title="Test Post Title.").first()
    # assert post is not None

def test_create_blog(test_client, session):
    create_blog = Post.create_blogpost({"title": "Test Post Title.", "body": "This is a test post", "taglist":"tag1, tag", "visible": True})
    fetched_post = db.session.query(Post).filter_by(title='Test Post Title.').first()
    assert fetched_post is not None

def test_detail(test_client, session):
    post = Post(title='Test Detail Post', body='This is a test post', url="detail-url", visible=True)
    db.session.add(post)
    db.session.commit()

    response = test_client.get(f'/detail/{post.url}')
    assert response.status_code == 200

def test_delete_post(test_client, session):
    post = Post(title='Test Post to Delete', body='This is a test post', url="test-url", visible=True)
    db.session.add(post)
    db.session.commit()

    response = test_client.get(f'/delete/{post.id}', follow_redirects=True)
    assert response.status_code == 200

    deleted_post = db.session.get(Post, post.id)
    assert deleted_post is None  # Post should no longer exist

def test_update_post(test_client, session):
    # For this test, you need an existing post to update, which may require adjustments based on your app's logic.
    # Here's a simplified version assuming you first add a post to update:
    post = Post(title='Initial Title', body='Initial body', url="updated-url", visible=True)
    db.session.add(post)
    db.session.commit()

    form_data = {'title': 'Updated Test Post', 'body': 'Updated test body'}
    response = test_client.post(f'/update/{post.id}', data=form_data, follow_redirects=True)
    assert response.status_code == 200

    # updated_post = db.session.query(Post).filter_by(id=post.id).first()
    # assert updated_post.title == 'Updated Test Post'

def test_view_tag(client):
    post = Post(title="Test Post with Tag", body="Test Body with Tag", url="test-url", visible=True)
    db.session.add(post)
    db.session.commit()

    response = client.get('/tag/untagged')
    assert response.status_code == 200