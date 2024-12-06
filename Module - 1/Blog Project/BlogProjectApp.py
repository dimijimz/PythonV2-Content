from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def home():
    return {"message": "Welcome to the Blog API!"}

# In-memory "database"
posts = {}
current_id = 1

# Get all posts
@app.route('/posts', methods=['GET'])
def get_all_posts():
    return {"status": "success", "data": list(posts.values())}

# Create a new post
@app.route('/posts', methods=['POST'])
def create_post():
    global current_id
    data = request.json

    # Validate input
    if not data or 'title' not in data or 'content' not in data:
        return {"error": "Fields 'title' and 'content' are required"}, 400

    # Add the new post
    posts[current_id] = {"id": current_id, "title": data['title'], "content": data['content']}
    current_id += 1

    return {"status": "success", "data": posts[current_id - 1]}

# Get a post by ID
@app.route('/posts/<int:id>', methods=['GET'])
def get_post(id):
    post = posts.get(id)
    if not post:
        return {"error": "Post not found"}, 404

    return {"status": "success", "data": post}

# Delete a post by ID
@app.route('/posts/<int:id>', methods=['DELETE'])
def delete_post(id):
    post = posts.pop(id, None)
    if not post:
        return {"error": "Post not found"}, 404

    return {"status": "success", "message": "Successfully Deleted"}

if __name__ == '__main__':
    app.run(debug=True)