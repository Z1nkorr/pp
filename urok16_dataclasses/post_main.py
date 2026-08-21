from post import Post
from posts_func import *

global_post_id = 0

def get_next_post_id()->int:
    global global_post_id
    global_post_id += 1

    return global_post_id

posts: list[Post] = []

new_post = inp_post_data()
new_post.id = get_next_post_id()

add_new_post_to_end(new_post, posts)


new_post = inp_post_data()
new_post.id = get_next_post_id()

add_new_post_to_end(new_post, posts)

print_posts(posts)   