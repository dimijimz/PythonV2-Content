from flask import Flask, request, json
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

# Search by title and pagination
@app.route('/posts', methods=['GET'])
def search_posts():
    page = request.args.get('page', type=int)
    page_size = request.args.get('size', type=int)
    title = request.args.get('title')
    found_post = [post for post in posts.values() if title in post['title']]
    found_post = found_post[(page - 1) * page_size: page * page_size]
    found = {'posts': found_post}
    print(found)
    return found, 200


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

def fill_database():
    global posts
    with open('database.json', 'r') as f:
        db = json.load(fp = f)

def save_database():
    global posts
    with open('database.json', 'w') as f:
       json.dump(posts, fp = f)





if __name__ == '__main__':
    fill_database()
    app.run(debug=True)