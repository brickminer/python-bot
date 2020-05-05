import random

images: list = [
    'https://ih0.redbubble.net/image.488404858.0162/flat,550x550,075,f.jpg',
    'https://cdn11.bigcommerce.com/s-a9579/images/stencil/1280x1280/products/3932/17155/I_will_not_keep_calm_and_you_can_fuck_off__18812__38527.1454604401.jpg?c=2&imbypass=on?imbypass=on',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQGSyKo_Z-nl7O41Lg0VJwS8J7Tvd5S7lBYZevrDvjUkaEb8Lv0&usqp=CAU',
    'https://www.meme-arsenal.com/memes/42c24251ddfcfccf0188d2021cfdc7c6.jpg',
    'https://i.redd.it/kg9f3v4pgbsy.png',
    'https://res.cloudinary.com/teepublic/image/private/s--GZR8KBgY--/t_Resized%20Artwork/c_fit,g_north_west,h_954,w_954/co_191919,e_outline:48/co_191919,e_outline:inner_fill:48/co_ffffff,e_outline:48/co_ffffff,e_outline:inner_fill:48/co_bbbbbb,e_outline:3:1000/c_mpad,g_center,h_1260,w_1260/b_rgb:eeeeee/c_limit,f_jpg,h_630,q_90,w_630/v1511742510/production/designs/2106134_1.jpg',
]

messages: list = [
    '{} is pure crap!',
    'In a scale of 1 to 10, I give {} a 3!',
    'Seriously? {} don\'t worth the bytes spent searching it!',
    'Just fuck off, {} is pure trash!',
]


def image_link() -> str:
    return random.choice(images)


def bad_text(set_name: str) -> str:
    return random.choice(messages).format(set_name)
