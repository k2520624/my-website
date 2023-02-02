# 나만의 웹사이트



### Summary


* 캠으로 얼굴 검출 후 눈 검출

* 눈 깜빡임 인식

* 일정 시간 눈이 감겨있으면 경보음 재생
  <br>

  <br>
  
  
### Block diagram


<img src="https://user-images.githubusercontent.com/75367132/214056920-bb085685-5444-45dd-a3cb-2abc99d5823b.PNG" width="80%" height="50%">


<br>

## About Project

### 얼굴 검출, 눈 검출

<img src="https://img.shields.io/badge/Language-Python-green?style=flat"/><img src="https://img.shields.io/badge/Library-Opencv-blue?style=flat"/>

* opencv dnn 모듈을 이옹해 이미 학습된 모델 파일로 얼굴 검출

* opencv의 haar cascade 알고리즘을 이용해서 눈 검출


  <br>

### 눈 깜빡임 인식

<img src="https://img.shields.io/badge/Language-Python-green?style=flat"/><img src="https://img.shields.io/badge/Library-Opencv-blue?style=flat"/>

* 샘플 데이터셋을 받아와서 학습시킨 후 모델 파일로 저장
  <img src="https://data-flair.training/blogs/wp-content/uploads/sites/2/2021/07/driver-drowsiness-dataset-sample.png" width="80%" height="50%">
* 학습시킨 모델 파일로 눈 깜빡 여부 예측
  <br>
  <br>

## Results

https://youtu.be/MJOeVdWbd_E



<br>
