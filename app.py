from flask import Flask, render_template, request
from api.connector import pexel

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    results_data = None
    type=None
    if request.method == 'POST':
        search_query = request.form.get('search')
        type = request.form.get('type')

        pex = pexel()
        results = pex.search_api_new(search_query, type)
        #print(results)
        if type=="image":
            results_data = [{
                'photographer': photo['photographer'],
                'url': photo['url'],
                'src': photo['src']['medium']
            } for photo in results]
        else:    
            results_data = [{
                'image': video['image'],
                'url': video['url'],
                'src': video['video_files'][0]['link']
            } for video in results]
        print(results_data)    
    return render_template('index.html', results=results_data, type=type)

if __name__ == '__main__':
    app.run(debug=True)
