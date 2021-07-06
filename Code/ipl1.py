from flask import Flask, render_template, request, redirect, flash
import pickle
import numpy as np

model = pickle.load(open('model5.pkl', 'rb'))

app = Flask(__name__)
app.secret_key = b'_5#y2L"F804Q8z\n\xec]/'


@app.route('/', methods=['GET','POST'])
def home():
    return render_template('index1.html')

@app.route('/predict', methods=['POST','GET'])
def predict():
    if request.method == 'POST':
        temp_array = list()
        std=list()
        batting_team = request.form['batting-team']
        if batting_team == 'Chennai Super Kings':
            temp_array = temp_array + [1,0,0,0,0,0,0,0]
        elif batting_team == 'Delhi Capitals':
            temp_array = temp_array + [0,1,0,0,0,0,0,0]
        elif batting_team == 'Kings XI Punjab':
            temp_array = temp_array + [0,0,1,0,0,0,0,0]
        elif batting_team == 'Kolkata Knight Riders':
            temp_array = temp_array + [0,0,0,1,0,0,0,0]
        elif batting_team == 'Mumbai Indians':
            temp_array = temp_array + [0,0,0,0,1,0,0,0]
        elif batting_team == 'Rajasthan Royals':
            temp_array = temp_array + [0,0,0,0,0,1,0,0]
        elif batting_team == 'Royal Challengers Bangalore':
            temp_array = temp_array + [0,0,0,0,0,0,1,0]
        elif batting_team == 'Sunrisers Hyderabad':
            temp_array = temp_array + [0,0,0,0,0,0,0,1]
        
        bowling_team = request.form['bowling-team']

        if batting_team == bowling_team:
            flash("Same Team Not allowed")
            return redirect('/')

        if bowling_team == 'Chennai Super Kings':
            temp_array = temp_array + [1,0,0,0,0,0,0,0]
        elif bowling_team == 'Delhi Daredevils':
            temp_array = temp_array + [0,1,0,0,0,0,0,0]
        elif bowling_team == 'Kings XI Punjab':
            temp_array = temp_array + [0,0,1,0,0,0,0,0]
        elif bowling_team == 'Kolkata Knight Riders':
            temp_array = temp_array + [0,0,0,1,0,0,0,0]
        elif bowling_team == 'Mumbai Indians':
            temp_array = temp_array + [0,0,0,0,1,0,0,0]
        elif bowling_team == 'Rajasthan Royals':
            temp_array = temp_array + [0,0,0,0,0,1,0,0]
        elif bowling_team == 'Royal Challengers Bangalore':
            temp_array = temp_array + [0,0,0,0,0,0,1,0]
        elif bowling_team == 'Sunrisers Hyderabad':
            temp_array = temp_array + [0,0,0,0,0,0,0,1]

        stadium=request.form['stadium']
        if stadium=='Eden Gardens':
            std=std + [1,0,0,0,0,0,0,0,0]
        elif stadium =='Feroz Shah Kotla':
            std=std+[0,1,0,0,0,0,0,0,0]
        elif stadium=='M Chinnaswamy Stadium':
            std=std+[0,0,1,0,0,0,0,0,0]
        elif stadium=='MA Chidambaram Stadium, Chepauk':
            std=std+[0,0,0,1,0,0,0,0,0]
        elif stadium=='Punjab Cricket Association Stadium, Mohali':
            std=std+[0,0,0,0,1,0,0,0,0]
        elif stadium=='Rajiv Gandhi International Stadium, Uppal':
            std=std+[0,0,0,0,0,1,0,0,0]
        elif stadium=='Sardar Patel Stadium, Motera':
            std=std+[0,0,0,0,0,0,1,0,0]
        elif stadium=='Sawai Mansingh Stadium':
            std=std+[0,0,0,0,0,0,0,1,0]
        elif stadium=='Wankhede Stadium':
            std=std+[0,0,0,0,0,0,0,0,1]


        runs = int(request.form['runs'])
        wickets = int(request.form['wickets'])
        overs = float(request.form['overs'])
        runs_in_prev_5 = int(request.form['runs_in_prev_5'])
        wickets_in_prev_5 = int(request.form['wickets_in_prev_5'])
        temp_array = temp_array + std + [runs, wickets, overs, runs_in_prev_5, wickets_in_prev_5]

        data = np.array([temp_array])
        print(data)
        pred = int(model.predict(data)[0])

        return render_template('result.html', lower_limit = abs(pred-10), upper_limit = abs(pred+10))

if __name__ == '__main__':
    app.run(debug=True)