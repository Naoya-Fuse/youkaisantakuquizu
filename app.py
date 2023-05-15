# coding: utf-8

from flask import Flask, render_template, request, url_for
import os
import random
import json

app = Flask(__name__)

# 画像フォルダ内のファイル名を取得する
image_names = os.listdir('static/images/output_folder')


# answers.jsonからデータを読み込む
def get_answers():
    with open('answer.json', 'r', encoding='utf-8') as f:
        return json.load(f)
# answers.jsonのキー（日本語の名前）をリストにする
answers = get_answers()
image_names = list(answers.keys())

def create_choices(answers, correct_answer):
    # 全ての妖怪名前から正解を除く
    other_answers = [name for name in answers if name != correct_answer]
    # 正解以外の妖怪名前からランダムに3つ選ぶ
    wrong_choices = random.sample(other_answers, 2)
    # 正解と不正解の選択肢を合わせる
    choices = wrong_choices + [correct_answer]
    # 選択肢をシャッフルする
    random.shuffle(choices)
    return choices

@app.route('/')
def index():
    # 日本語名のリストからランダムに1つ選ぶ
    correct_answer_jp = random.choice(list(answers.values()))
    # 選択した日本語名に対応する英語名（画像ファイル名）を取得する
    image_name = [key for key, value in answers.items() if value == correct_answer_jp][0]
    # 画像ファイルのパスを作成する
    image_path = os.path.join('static/images/output_folder', image_name + '.jpg')  # '.png' を追加
    # 選択肢を作る
    choices = create_choices(list(answers.values()), correct_answer_jp)  # list(answers.values()) を渡す
    # シルエット化していない画像のパスを作成する
    non_silhouette_image_path = os.path.join('static/images/input_folder', image_name + '.jpg')  
    return render_template('index.html', image_path=image_path, image_name=image_name, choices=choices, non_silhouette_image_path=non_silhouette_image_path)

@app.route('/answer', methods=['POST'])
def answer():
    # 3択問題で入力した名前を取得する
    guess = request.form['guess']
    # 正解の場合は'input_folder'フォルダの画像を表示する
    image_name = request.form['image_name']
    # シルエット化していない画像のパスを作成する
    non_silhouette_image_path = os.path.join('static/images/input_folder', image_name + '.jpg')
    correct_answer_jp = [value for key, value in answers.items() if key == image_name][0]
    eng_image_name = answers[image_name]
    image_path = os.path.join('static/images/input_folder', eng_image_name + '.jpg')
    result = '不正解'
    # 3択問題で入力した名前と正解を比較する
    if guess == correct_answer_jp:
        result = '正解！'
    return render_template('answer.html', image_path=image_path, result=result, correct_answer=correct_answer_jp, guess=guess, non_silhouette_image_path=non_silhouette_image_path)
 
    
if __name__ == '__main__':
    app.run(debug=True)

  

    