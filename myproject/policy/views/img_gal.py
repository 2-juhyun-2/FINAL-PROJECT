from flask import Blueprint,request
import os
from flask.helpers import send_from_directory, url_for
from flask.templating import render_template
from werkzeug.utils import redirect


bp = Blueprint('img_gallary', __name__, url_prefix='/image')


# 데이터 어떻게 받을 것인가?

@bp.route('/',methods=('GET', 'POST'))
def search_image():
    
    args_dict = request.args.to_dict()
    # return redirect('/gallary')
    # 검색 수정중... 이미지 파일 검색안됨..


    # 검색어 받아
    print( args_dict)

    # return send_from_directory('policy/image',filename), 
    return render_template('image_gal/complete.html')
    

@bp.route('/gal/<filename>')
def send_image(filename):
    return send_from_directory("image",filename)
    # image 폴더에 있는 사진들을 개별로 조회가능


@bp.route('/gallary', methods=('GET', 'POST'))
def get_gallery():
    print(os.getcwd())
    args_dict = request.args.get('keyword')

    print(args_dict)
    print(type(args_dict))

    image_names = os.listdir('policy/image')

    if args_dict == None:
        print('wtf')
        args_dict = os.listdir('policy/image')
    else:
        # args_dict = args_dict['keyword']
        args_dict = args_dict + '.jpg'



    # args_dict = args_dict + '.png'
        if args_dict in image_names:
            image_names = [args_dict]
        else:
            return "No images"
        
    # polict의 image파일의 리스트
    # 검색어로 메타태그 조회
    # 메타태그 포함된 이미지 path/이름 가져와
    # 그것만 리스트에 넣어 준다.
    # image_namesㅇ에 넣는다.
    
    # return print(image_names)
    return render_template('image_gal/galla.html', image_names = image_names)
    # return render_template('image_gal/gallary.html', image_names = image_names)
    #  image_names에 넣어서 gallary.html로 전달 html에서 사용할 것임..



# C:\Users\hann1\Documents\카카오톡 받은 파일\myproject\policy\image