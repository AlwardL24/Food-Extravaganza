import json
from flask import Flask, redirect, request, url_for
from flask import render_template

app = Flask(__name__)
app.jinja_env.auto_reload = True
app.config["TEMPLATES_AUTO_RELOAD"] = True

dishes = [
    {
        "id": 'mixed-tomato-canapes',
        "name": 'Mixed Tomato Canapes',
        "description":
            'For a quick and easy bite-size snack, serve these tasty mixed tomato canapés with melted camembert and basil pesto.',
        "tags": [
            'Contains Gluten',
            'Contains Peanuts',
            'Contains Tree Nuts',
            'Contains Milk',
            'Contains Soy',
        ],
        "fields": "<b>Ingredients</b><p>200g red Perino tomatoes<br>200g gold Perino tomatoes<br>1 tsp olive oil<br>1 Coles Bakery stone baked wholemeal quinoa pane di casa bread, cut into 1cm-thick slices<br>Olive oil, to brush<br>1/3 cup (90g) basil pesto<br>100g camembert, cut into thin slices<br>Fresh basil leaves, to serve</p><b>Serves</b><p>15</p> ",
        "imageURL": '/static/images/1.jpeg',
        "reviews": [
            {
                "starRating": 4,
                "review": 'Test',
            },
        ],
    },
    {
        "id": 'celery-lemon-parsley-spoon-salad',
        "name": 'Celery, Lemon and Parsley Spoon Salad',
        "description":
            'Take a cue from Turkey’s lovely tomato and cucumber ‘spoon salad’, and finely dice crisp summer vegetables, as you would for a salsa. Serve with spoons to make serving and eating easier.',
        "tags": ['Contains Tree Nuts', 'Contains Celery'],
        "fields": "<b>Ingredients</b><p>2 celery stalks<br>1/2 telegraph cucumber, peeled, seeds removed, cut into 5mm cubes<br>Zested rind of 2 lemons, plus 2 tbsp juice<br>1/3 cup finely chopped flat-leaf parsley leaves<br>1 tbsp baby salted capers, rinsed<br>1 tbsp finely chopped toasted pecans<br>1/4 cup (60ml) extra virgin olive oil</p><b>Serves</b><p>4</p>",
        "imageURL": '/static/images/2.jpeg',
        "reviews": [
            {
                "starRating": 1,
                "review": 'Testing',
            },
        ],
    },
    {
        "id": 'placeholder-1',
        "name": 'Placeholder 1',
        "description":
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras non tortor tincidunt, volutpat elit non, interdum eros.',
        "tags": [
            'Contains Gluten',
            'Contains Peanuts',
            'Contains Tree Nuts',
            'Contains Milk',
            'Contains Soy',
        ],
        "fields": "<b>Ingredients</b><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras non tortor tincidunt, volutpat elit non, interdum eros. Nunc dapibus, quam sit amet iaculis pulvinar, metus ante porta ipsum, ac condimentum velit dui non libero. Etiam augue lectus, faucibus eu eros sit amet, laoreet tincidunt orci. Nullam semper mattis velit, vitae ultrices purus consequat a. Suspendisse aliquet venenatis vehicula. Integer luctus malesuada leo, et imperdiet mi varius nec. Cras orci felis, semper vitae leo non, suscipit porta lectus. Mauris convallis ut lorem nec posuere. Mauris vitae est mi.</p>",
        "imageURL": '/static/images/3.jpeg',
        "reviews": [
            {
                "starRating": 4,
                "review": 'Test',
            },
        ],
    },
    {
        "id": 'placeholder-2',
        "name": 'Placeholder 2',
        "description":
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras non tortor tincidunt, volutpat elit non, interdum eros.',
        "tags": [
            'Contains Gluten',
            'Contains Peanuts',
            'Contains Tree Nuts',
            'Contains Milk',
            'Contains Soy',
        ],
        "fields": "<b>Ingredients</b><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras non tortor tincidunt, volutpat elit non, interdum eros. Nunc dapibus, quam sit amet iaculis pulvinar, metus ante porta ipsum, ac condimentum velit dui non libero. Etiam augue lectus, faucibus eu eros sit amet, laoreet tincidunt orci. Nullam semper mattis velit, vitae ultrices purus consequat a. Suspendisse aliquet venenatis vehicula. Integer luctus malesuada leo, et imperdiet mi varius nec. Cras orci felis, semper vitae leo non, suscipit porta lectus. Mauris convallis ut lorem nec posuere. Mauris vitae est mi.</p>",
        "imageURL": '/static/images/4.jpeg',
        "reviews": [
            {
                "starRating": 4,
                "review": 'Test',
            },
        ],
    },
    {
        "id": 'placeholder-3',
        "name": 'Placeholder 3',
        "description":
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras non tortor tincidunt, volutpat elit non, interdum eros.',
        "tags": [
            'Contains Gluten',
            'Contains Peanuts',
            'Contains Tree Nuts',
            'Contains Milk',
            'Contains Soy',
        ],
        "fields": "<b>Ingredients</b><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras non tortor tincidunt, volutpat elit non, interdum eros. Nunc dapibus, quam sit amet iaculis pulvinar, metus ante porta ipsum, ac condimentum velit dui non libero. Etiam augue lectus, faucibus eu eros sit amet, laoreet tincidunt orci. Nullam semper mattis velit, vitae ultrices purus consequat a. Suspendisse aliquet venenatis vehicula. Integer luctus malesuada leo, et imperdiet mi varius nec. Cras orci felis, semper vitae leo non, suscipit porta lectus. Mauris convallis ut lorem nec posuere. Mauris vitae est mi.</p>",
        "imageURL": '/static/images/5.jpeg',
        "reviews": [
            {
                "starRating": 4,
                "review": 'Test',
            },
        ],
    },
    {
        "id": 'placeholder-4',
        "name": 'Placeholder 4',
        "description":
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras non tortor tincidunt, volutpat elit non, interdum eros.',
        "tags": [
            'Contains Gluten',
            'Contains Peanuts',
            'Contains Tree Nuts',
            'Contains Milk',
            'Contains Soy',
        ],
        "fields": "<b>Ingredients</b><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras non tortor tincidunt, volutpat elit non, interdum eros. Nunc dapibus, quam sit amet iaculis pulvinar, metus ante porta ipsum, ac condimentum velit dui non libero. Etiam augue lectus, faucibus eu eros sit amet, laoreet tincidunt orci. Nullam semper mattis velit, vitae ultrices purus consequat a. Suspendisse aliquet venenatis vehicula. Integer luctus malesuada leo, et imperdiet mi varius nec. Cras orci felis, semper vitae leo non, suscipit porta lectus. Mauris convallis ut lorem nec posuere. Mauris vitae est mi.</p>",
        "imageURL": '/static/images/6.jpeg',
        "reviews": [
            {
                "starRating": 4,
                "review": 'Test',
            },
        ],
    },
    {
        "id": 'placeholder-5',
        "name": 'Placeholder 5',
        "description":
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras non tortor tincidunt, volutpat elit non, interdum eros.',
        "tags": [
            'Contains Gluten',
            'Contains Peanuts',
            'Contains Tree Nuts',
            'Contains Milk',
            'Contains Soy',
        ],
        "fields": "<b>Ingredients</b><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras non tortor tincidunt, volutpat elit non, interdum eros. Nunc dapibus, quam sit amet iaculis pulvinar, metus ante porta ipsum, ac condimentum velit dui non libero. Etiam augue lectus, faucibus eu eros sit amet, laoreet tincidunt orci. Nullam semper mattis velit, vitae ultrices purus consequat a. Suspendisse aliquet venenatis vehicula. Integer luctus malesuada leo, et imperdiet mi varius nec. Cras orci felis, semper vitae leo non, suscipit porta lectus. Mauris convallis ut lorem nec posuere. Mauris vitae est mi.</p>",
        "imageURL": '/static/images/7.jpeg',
        "reviews": [
            {
                "starRating": 4,
                "review": 'Test',
            },
        ],
    },
    {
        "id": 'placeholder-6',
        "name": 'Placeholder 6',
        "description":
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras non tortor tincidunt, volutpat elit non, interdum eros.',
        "tags": [
            'Contains Gluten',
            'Contains Peanuts',
            'Contains Tree Nuts',
            'Contains Milk',
            'Contains Soy',
        ],
        "fields": "<b>Ingredients</b><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras non tortor tincidunt, volutpat elit non, interdum eros. Nunc dapibus, quam sit amet iaculis pulvinar, metus ante porta ipsum, ac condimentum velit dui non libero. Etiam augue lectus, faucibus eu eros sit amet, laoreet tincidunt orci. Nullam semper mattis velit, vitae ultrices purus consequat a. Suspendisse aliquet venenatis vehicula. Integer luctus malesuada leo, et imperdiet mi varius nec. Cras orci felis, semper vitae leo non, suscipit porta lectus. Mauris convallis ut lorem nec posuere. Mauris vitae est mi.</p>",
        "imageURL": '/static/images/8.jpeg',
        "reviews": [
            {
                "starRating": 4,
                "review": 'Test',
            }
        ]
    }
]

@app.route("/")
def index():
    design = "final"
    return render_template("index.html", design=design, product="", dishes=json.dumps(dishes), reviews="HIDE")

@app.route("/<product>")
def indexProduct(product):
    design = "final"
    return render_template("index.html", design=design, product=product, dishes=json.dumps(dishes), reviews="HIDE")

@app.route("/<product>/reviews")
def indexProductReviews(product):
    design = "final"
    return render_template("index.html", design=design, product=product, dishes=json.dumps(dishes), reviews="SHOW")

@app.route("/<product>/reviews/submit", methods=["POST"])
def submitProductReview(product):
    dishes[[i for i in range(len(dishes)) if dishes[i]["id"] == product][0]]["reviews"].append({
                "starRating": request.form["star-rating"],
                "review": request.form["review"],
            })
    return redirect(url_for("indexProductReviews", product=product))

if __name__ == "__main__":
	app.run()