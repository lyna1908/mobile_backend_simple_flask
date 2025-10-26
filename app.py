from flask import Flask, jsonify
from flask_cors import CORS 
import json
import datetime

app = Flask(__name__)
CORS(app)

# EXISTING ROUTES (keeping them)
@app.route('/news.all.get')
def get_news_all_articles():
	data = []
	try:
		with open('news_data.json', 'r') as file:
			data = json.load(file)
		app.logger.debug('_________________Hello ' + str(data))
	except FileNotFoundError:
		app.logger.error('news_data.json not found')
		data = []
	return jsonify(data)


@app.route('/news.categories.get')
def get_news_categories():
	time_now_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	data = {
		'title': 'List of Categories',
		'time': time_now_str,
		'categories': [
			{'id': 1, 'name': 'Sports'},
			{'id': 2, 'name': 'Politics'},
			{'id': 3, 'name': 'Education'}
		]
	}
	return jsonify(data)


# NEW ROUTE FOR FLUTTER APP
@app.route('/api/news', methods=['GET'])
def get_news():
	news_data = [
		{
			'id': 1,
			'title': 'Breaking: New Mobile Dev Framework Released',
			'description': 'A revolutionary new framework for mobile development has been announced today',
			'image': 'https://via.placeholder.com/300x200/4CAF50/ffffff?text=News+1',
			'author': 'Tech News',
			'date': '2025-10-26',
			'category': 'Technology'
		},
		{
			'id': 2,
			'title': 'Flutter 4.0 Major Update',
			'description': 'Flutter announces major performance improvements and new features for developers',
			'image': 'https://via.placeholder.com/300x200/2196F3/ffffff?text=News+2',
			'author': 'Flutter Team',
			'date': '2025-10-25',
			'category': 'Development'
		},
		{
			'id': 3,
			'title': 'AI Integration in Mobile Apps',
			'description': 'How artificial intelligence is transforming mobile application development',
			'image': 'https://via.placeholder.com/300x200/FF9800/ffffff?text=News+3',
			'author': 'AI Weekly',
			'date': '2025-10-24',
			'category': 'AI'
		},
		{
			'id': 4,
			'title': 'Mobile Security Best Practices 2025',
			'description': 'Essential security practices every mobile developer should implement',
			'image': 'https://via.placeholder.com/300x200/F44336/ffffff?text=News+4',
			'author': 'Security Pro',
			'date': '2025-10-23',
			'category': 'Security'
		},
		{
			'id': 5,
			'title': 'Cross-Platform Development Trends',
			'description': 'Latest trends in cross-platform mobile app development',
			'image': 'https://via.placeholder.com/300x200/9C27B0/ffffff?text=News+5',
			'author': 'Dev Magazine',
			'date': '2025-10-22',
			'category': 'Development'
		}
	]
	return jsonify(news_data)


# HOME ROUTE
@app.route('/')
def index():
	return jsonify({
		'message': 'Welcome ENSIA Students from Flask!',
		'endpoints': {
			'/': 'Home page',
			'/api/news': 'Get all news (for Flutter app)',
			'/news.all.get': 'Get all articles from JSON file',
			'/news.categories.get': 'Get news categories'
		}
	})


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000, debug=True)