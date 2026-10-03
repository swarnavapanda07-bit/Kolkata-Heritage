
from flask import Flask, render_template

app = Flask(__name__)

places = {
    "victoria-memorial": {
        "name": "Victoria Memorial",
        "description": "Victoria Memorial is one of the most famous landmarks of Kolkata. It is a large marble monument surrounded by beautiful gardens.",
        "history": "The Victoria Memorial was built in memory of Queen Victoria. Construction began in 1906 and the memorial was opened to the public in 1921.",
        "location": "Maidan, Kolkata, West Bengal",
        "timings": "10:00 AM - 6:00 PM",
        "entry_fee": "Approximately ₹50 for Indian visitors",
        "best_time": "October to February",
        "latitude": 22.5448,
        "longitude": 88.3426
    },

    "howrah-bridge": {
        "name": "Howrah Bridge",
        "description": "Howrah Bridge is one of the most recognizable landmarks of Kolkata. It connects Kolkata with Howrah across the Hooghly River.",
        "history": "The bridge was opened in 1943 and is officially known as Rabindra Setu.",
        "location": "Howrah, West Bengal",
        "timings": "Open throughout the day",
        "entry_fee": "Free",
        "best_time": "Evening",
        "latitude": 22.5958,
        "longitude": 88.2636
    },

    "indian-museum": {
        "name": "Indian Museum",
        "description": "The Indian Museum is one of the oldest and largest museums in India. It contains collections related to archaeology, history, art, geology and zoology.",
        "history": "The museum was established in 1814 and has played an important role in preserving India's cultural and natural heritage.",
        "location": "Jawaharlal Nehru Road, Kolkata",
        "timings": "10:00 AM - 6:00 PM",
        "entry_fee": "Varies by visitor category",
        "best_time": "Weekday mornings",
        "latitude": 22.5576,
        "longitude": 88.3502
    },

    "princep-ghat": {
        "name": "Princep Ghat",
        "description": "Princep Ghat is a historic riverside monument located beside the Hooghly River. It is known for its beautiful architecture and scenic surroundings.",
        "history": "The monument was constructed in 1841 and was named after James Prinsep.",
        "location": "Strand Road, Kolkata",
        "timings": "Open throughout the day",
        "entry_fee": "Free",
        "best_time": "Evening",
        "latitude": 22.5562,
        "longitude": 88.3234
    },

    "belur-math": {
        "name": "Belur Math",
        "description": "Belur Math is the headquarters of the Ramakrishna Math and Ramakrishna Mission. It is situated on the western bank of the Hooghly River.",
        "history": "Belur Math was founded by Swami Vivekananda in 1897 as the headquarters of the Ramakrishna Mission.",
        "location": "Belur, Howrah, West Bengal",
        "timings": "Morning and afternoon/evening sessions",
        "entry_fee": "Free",
        "best_time": "Winter months",
        "latitude": 22.6322,
        "longitude": 88.3556
    }
}


@app.route("/")
def home():
    return render_template("index.html", places=places)


@app.route("/place/<place_id>")
def place(place_id):

    selected_place = places.get(place_id)

    if selected_place is None:
        return "Place not found", 404

    return render_template(
        "place.html",
        place=selected_place
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)