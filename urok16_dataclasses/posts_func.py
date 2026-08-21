from post import Post

def inp_post_data()->Post:
    posting_date_time = input("Введите дату:")
    media_url = input("Введите url видео или картинки:")
    description = input("Введите текст с описанием поста")

    return Post(
        id=0,
        posting_date_time=posting_date_time,
        media_url=media_url,
        description=description,
    )

def add_new_post_to_end(new_post:Post, posts:list[Post]):
    posts.append(new_post)

def print_post_header():
    print(f"{'id':<5}{'posting_datetime':<25}{'Media URL':<25}{'desc':<25}")

def print_one_post(post:Post):
    print(
        f"{post.id:<5}{post.posting_date_time:<25}{post.media_url:<25}{post.
        description:<25}"
    )

def print_posts(posts:list[Post]):
    print_post_header()
    for post in posts:
        print_one_post(post)