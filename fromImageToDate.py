# =====자신만의 이미지 데이터로 CNN 적용해보기=====
# ## 이미지 파일 학습(입력) 데이터로 변경 ##
groups_folder_path = './cnn_sample/'
# './cnn_sample/' 여기 안에 각각 이미지들을 정리한거

categories = ["0", "1", "2"]
# 여기안에 폴더명들 넣기

image_w = 28
image_h = 28
# 데이터의 용량을 줄이기 위해서 이미지 크기를 28*28로 조절할려는 거

X = []
Y = []

for idex, categorie in enumerate(categories):
# enumerate = 리스트의 원소에 순서값을 부여해주는 함수(인덱스 값과 객체를 리턴)
    label = [0 for i in range(num_classes)]
    # 폴더 개수만큼 label 늘리기?
    label[idex] = 1
    image_dir = groups_folder_path + categorie + '/'
    # 이미지 폴더 있는 곳에 각각의 음식 파일 폴더 생성(?) or 이동(?)


    for top, dir, f in os.walk(image_dir):
        # os.walk() = 3개의 값이 있는 tuple을 넘겨줌
        # top = dir과 files가 있는 path
        # dir = root아래에 있는 폴더들
        # f = root 아래에 있는 파일들
        for filename in f:
          print(image_dir+filename)
          img = cv2.imread(image_dir+filename)
          #이미지 파일 읽기
          img = cv2.resize(img, None, fx=image_w/img.shape[0], fy=image_h/img.shape[1])
          # 1st = 입력 이미지(-> img)
          # 2nd = 절대 크기(-> None)
          # 3rd = 상대크기(-> fx = image_w/img.shape[0]) // 만약 fx에 2개 들어가면 사이즈 2배 // ??
          # 4th = 상대크기(-> fy = image_h/img.shape[1])
          # 5th = 보간법(X)
X.append(img/256)
# 픽셀은 0~255값을 가짐 // 학습을 하기에는 0~1 사이의 소수가 필요해서 256으로 나눔
# 비어있는 X에 img값을 0~1로 만들어서 추가
# 위에서 한것들이 다 그냥 이미지 파일을 데이터로 변경할려고 하는것들
Y.append(label)
# 여기에는 그냥 label만 넣는거??


X_train, X_test, Y_train, Y_test = train_test_split(X, Y)
# train_test_split = 데이터 분할 해주는거
# overfitting 방지할려고 한다는데, 잘 모르겠네
# 근데 Y에는 그냥 lable만 있는데, 이거는 어떻게 된다는 거지?

xy = (X_train, X_test, Y_train, Y_test)

np.save("./img_data.npy", xy)
# 1개의 배열을 NumPy format의 바이너리 파일로 저장하기 // 배열 xy를 저장하는거 같은데






