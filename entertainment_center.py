import fresh_tomatoes
import media  # file name: media


the_note_book = media.Movie(
    "The Note Book",
    "A poor yet passionate young man falls in love with a rich young woman,"
    "giving her a sense of freedom, but they are soon separated because of"
    "their social differences.",
    "img/the_note_book.jpg    ",
    "https://www.youtube.com/watch?v=FC6biTjEyZw"
)

perfect_getaway = media.Movie(
    "Perfect Getaway",
    "Two pairs of lovers on a Hawaiian vacation discover that psychopaths"
    "are stalking and murdering tourists on the islands.!",
    "img/perfect_getaway.jpg",
    "https://www.youtube.com/watch?v=Vk2bbLfyA4A"
)

flight_93 = media.Movie(
    "Flight 93",
    "Flight 93 is the story of the heroic passengers that took back their"
    "plane in an effort to stop a 9-11 terrorist attack.",
    "img/flight_93.jpg",
    "https://www.youtube.com/watch?v=FYw_OUresio"
)

face_off = media.Movie(
    "Face Off",
    "Two pairs of lovers on a Hawaiian vacation discover that psychopaths"
    "are stalking and murdering tourists on the islands.!",
    "img/face_off.jpg",
    "https://www.youtube.com/watch?v=YiwA3C2qeRo"
)
usual_suspect = media.Movie(
    "Usual Suspect",
    "A sole survivor tells of the twisty events leading up to a horrific"
    "gun battle on a boat, which begin when five criminals meet at a"
    "seemingly random police lineup.",
    "img/usual_suspect.jpg",
    "https://www.youtube.com/watch?v=9MjV4EwR7Mg"
)
dr_strange = media.Movie(
    "Dr. Strange",
    "A former neurosurgeon embarks on a journey of healing only to be"
    "drawn into the world of the mystic arts.",
    "img/dr_strange.jpg",
    "https://www.youtube.com/watch?v=kNdM7b1Lm04"
)


movies = []
movies.append(the_note_book)
movies.append(perfect_getaway)
movies.append(flight_93)
movies.append(face_off)
movies.append(usual_suspect)
movies.append(dr_strange)

fresh_tomatoes.open_movies_page(movies)
