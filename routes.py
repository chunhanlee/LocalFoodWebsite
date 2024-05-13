from flask import Blueprint, render_template, request, session
from models import DatabaseModel


bp = Blueprint('food', __name__)

@bp.route('/')
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        return render_template('error.html', error_message=str(e)), 404

@bp.route('/intro')
def intro():
    try:
        return render_template('intro.html')
    except Exception as e:
        return render_template('error.html', error_message=str(e)), 404

@bp.route('/search', methods=['GET', 'POST'])
def search():
    # try:
        if request.method == 'POST':
            db = DatabaseModel('database.db')
            search_query = request.form['query']
            results = db.searchText(search_query)
            return render_template('search.html', results=results, search_query=search_query)
        return render_template('search.html')
    # except Exception as e:
    #     return render_template('error.html', error_message=str(e)), 404
# @bp.route('/<int:food_id>')
# def details(food_id):
#     food = FoodInfo.query.get_or_404(food_id)
#     return render_template('details.html', food=food)

@bp.route('/foodcategories')
def food_categories():
    try:
        db = DatabaseModel('database.db')
        foodCategories = db.get_CategoryList()
        # foodCategories = get_categoryList()
        return render_template('foodcategories.html', foodCategories=foodCategories)
    except Exception as e:
        return render_template('error.html', error_message=str(e)), 404

    # conn = get_db_connection()
    # foodCategories = conn.execute('SELECT * FROM Food_Category').fetchall()
    # conn.close()
    # return render_template('foodcategories.html', foodCategories=foodCategories)
    
@bp.route('/foodcategories/foods/<int:category_id>')
def food_by_categories(category_id):
    try:
        db = DatabaseModel('database.db')
        foods = db.get_foodList(category_id)
        category_name = db.get_CategoryName(category_id)
        # category_name = get_categoryName(category_id)
        return render_template('foods.html', foods=foods, category_name = category_name)
    except Exception as e:
        return render_template('error.html', error_message=str(e)), 404

# @app.route('/foodcategories/foods/<int:category_id>')
# def food_by_categories(category_id):
#     foods = get_foodList(category_id)
#     category_name = get_CategoryName(category_id)
#     return render_template('foods.html', foods=foods, category_name=category_name['name'])

@bp.route('/foodcategories/foods/<int:category_id>/<int:food_id>')
def fooddetails(category_id,food_id):
    try:
        db = DatabaseModel('database.db')
        food = db.get_food(food_id)
        return render_template('fooddetails.html', food=food)
    except Exception as e:
        return render_template('error.html', error_message=str(e)), 404
# @app.route('/foodcategories/foods/<int:category_id>/<int:food_id>')
# def fooddetails(category_id,food_id):
#     food = get_food(food_id)
#     return render_template('foodDetails.html', food=food)

@bp.route('/commonillness')
def common_illness():
    try:
        db = DatabaseModel('database.db')
        common_illness_list = db.get_commonIllnessList()
        return render_template('commonillness.html', common_illness_list = common_illness_list)
    except Exception as e:
            return render_template('error.html', error_message=str(e)), 404

@bp.route('/commonillness/<int:illness_id>')
def illness_details(illness_id):
    try:
        db = DatabaseModel('database.db')
        illness = db.get_IllnessByID(illness_id)
        return render_template('illnessdetails.html', illness=illness)
    except Exception as e:
        return render_template('error.html', error_message=str(e)), 404
    
@bp.route('/lifestages')
def life_stages():
    try:
        db = DatabaseModel('database.db')
        stages_list = db.get_LifeStagesList()
        return render_template('lifestages.html', stages_list = stages_list)
    except Exception as e:
        return render_template('error.html', error_message=str(e)), 404


@bp.route('/lifestages/<int:stage_id>')
def stages_details(stage_id):
    try:
        db = DatabaseModel('database.db')
        stage = db.get_LifeStagesByID(stage_id)
        return render_template('stagedetails.html', stage=stage)
    except Exception as e:
        return render_template('error.html', error_message=str(e)), 404
    
@bp.route('/deficiency')
def deficiency():
    try:
        db = DatabaseModel('database.db')
        deficiency_list = db.get_DeficiencyList()
        return render_template('deficiency.html', deficiency_list = deficiency_list)
    except Exception as e:
        return render_template('error.html', error_message=str(e)), 404

@bp.route('/deficiency/<int:deficiency_id>')
def deficiency_details(deficiency_id):
    try:
        db = DatabaseModel('database.db')
        deficiency = db.get_DeficiencyByID(deficiency_id)
        return render_template('deficiencydetails.html', deficiency=deficiency)
    except Exception as e:
        return render_template('error.html', error_message=str(e)), 404
    
@bp.route('/seasons')
def seasons():
    db = DatabaseModel('database.db')
    seasons_list = db.get_SeasonsList()
    return render_template('season.html', seasons_list = seasons_list)

@bp.route('/seasons/<int:season_id>')
def season_details(season_id):
    try:
        db = DatabaseModel('database.db')
        season = db.get_SeasonByID(season_id)
        return render_template('seasondetails.html', season=season)
    except Exception as e:
        return render_template('error.html', error_message=str(e)), 404