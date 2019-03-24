const like_or_unlike_publication = async (like_hearth, url, like_counter, plural_or_singular) => {
    const response = await fetch(url);

    const {
        status,
        liked,
        unliked
    } = await response.json();
    if (status === 200 && liked) {
        like_hearth.classList.remove('fas');
        like_hearth.classList.remove('fa-heart-broken');
        like_hearth.classList.add('far');
        like_hearth.classList.add('fa-heart');
        like_counter.textContent = parseInt(like_counter.textContent) + 1
    }
    if (status === 200 && unliked) {
        like_hearth.classList.remove('far');
        like_hearth.classList.remove('fa-heart');
        like_hearth.classList.add('fas');
        like_hearth.classList.add('fa-heart-broken');
        like_counter.textContent = parseInt(like_counter.textContent) - 1
    }
    if (parseInt(like_counter.textContent) === 1){
        plural_or_singular.textContent = 'like'
    }
    else{
        plural_or_singular.textContent = 'likes'
    }
};

const addLikeOrUnlikeListener = (like_hearth, like_counter, plural_or_singular, url) => {
    like_hearth.addEventListener('click', e => {
        like_or_unlike_publication(
            e.target,
            url,
            like_counter,
            plural_or_singular
        )
    })
};