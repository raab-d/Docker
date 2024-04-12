# views.py
from flask import Blueprint, request, jsonify
from .models import Post
from . import db

# Création d'un Blueprint
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return "Hello from Flask!"


@main.route('/posts', methods=['POST'])
def add_post():
    data = request.get_json()
    try:
        new_post = Post(title=data['title'], content=data['content'])
        db.session.add(new_post)
        db.session.commit()
        return jsonify({"message": "Post created", "post": {"id": new_post.id, "title": new_post.title, "content": new_post.content}}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    
    
@main.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()  
    # Convertit chaque post en un dictionnaire de ses attributs pour la sérialisation JSON
    posts_data = [{"id": post.id, "title": post.title, "content": post.content} for post in posts]
    return jsonify(posts_data), 200


# Mettre à jour un post
@main.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    post.title = request.json.get('title', post.title)
    post.content = request.json.get('content', post.content)
    db.session.commit()
    return jsonify({'title': post.title, 'content': post.content})

# Supprimer un post
@main.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return jsonify({'message': 'Post deleted'})
