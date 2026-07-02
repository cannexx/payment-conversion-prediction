# 공유오피스 3일 체험 결제 전환 예측 (payment-conversion-app)

공유오피스 3일 무료 체험을 이용한 고객이 실제 유료 결제로 전환할지를 예측하는 **Streamlit 대시보드 & 예측 서비스**입니다.
데이터 소개 → 모델 성능 확인 → 실시간 예측 데모까지 한 화면에서 확인할 수 있습니다.

## 주요 기능

앱은 사이드바에서 3개 섹션을 전환하며 사용합니다.

- **📋 데이터 소개**: 결제자 vs 미결제자 행동 비교, 방문일수별 결제율 등 EDA 요약
- **📊 결과**: 혼동행렬, 피처 중요도, threshold별 성능(F1/Recall 등) 변화 시각화
- **🔮 예측 데모**
  - 🙋 단일 예측: 슬라이더로 값을 입력해 결제 확률 즉시 확인
  - 📁 CSV 업로드 예측: 여러 고객 데이터를 한 번에 업로드해 일괄 예측
  - ✍️ 수기 다중 입력: 표 형태로 직접 입력해 여러 고객 예측
  - 예측 결과는 CSV로 다운로드 가능

## 모델 정보

| 항목 | 내용 |
| --- | --- |
| 모델 | XGBoost (`XGBClassifier`) |
| 사용 피처 | 방문일수, 총출입횟수, 신청후첫방문일수 |
| 분류 기준 threshold | 0.45 |
| 평가 지표 | Recall(주 지표), F1(보조 지표) |

예측 시 아래 결측치/논리 규칙이 자동 적용됩니다.

- 방문일수 결측 → 방문일수 0, 총출입횟수 0, 신청후첫방문일수 -1
- 총출입횟수 결측 → 2로 대체
- 신청후첫방문일수 결측 → 0으로 대체
- 신청후첫방문일수가 -1이거나 방문일수가 0이면 미방문자로 간주해 나머지 값도 0/-1로 보정

## 프로젝트 구조

```
.
├── app.py                    # Streamlit 앱 메인 코드
├── xgb_payment_model.pkl     # 학습된 XGBoost 모델
├── best_threshold.pkl        # 최적 threshold 값
├── feature_data.pkl          # EDA/시각화용 학습 데이터
├── requirements.txt          # 파이썬 패키지 목록
├── packages.txt              # 시스템 패키지(한글 폰트: fonts-nanum)
└── .streamlit/config.toml    # 테마 설정
```

## 로컬 실행 방법

```bash
# 1. 가상환경 생성 (선택)
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# 2. 패키지 설치
pip install -r requirements.txt

# 3. 앱 실행
streamlit run app.py
```

`xgb_payment_model.pkl`, `best_threshold.pkl`, `feature_data.pkl`은 `app.py`와 같은 폴더(또는 상위 폴더)에 있어야 합니다.

## 배포 (Streamlit Community Cloud)

1. 이 저장소를 GitHub에 push
2. [Streamlit Community Cloud](https://streamlit.io/cloud)에서 새 앱 생성 후 저장소 연결
3. `packages.txt`(한글 폰트 설치용)와 `requirements.txt`가 자동으로 인식되어 빌드에 반영됨

## CSV 업로드 예측 시 필수 컬럼

| 컬럼명 | 설명 | 범위 |
| --- | --- | --- |
| 방문일수 | 체험 기간 중 방문한 일수 | 0 ~ 3 |
| 총출입횟수 | 전체 출입 카운트 | 0 ~ 50 |
| 신청후첫방문일수 | 신청 후 첫 방문까지 걸린 일수(미방문 시 -1) | -1 ~ 2 |

샘플 CSV는 앱 내 **CSV 업로드 예측** 탭에서 다운로드할 수 있습니다.

## 기술 스택

- Streamlit
- pandas / numpy
- scikit-learn
- XGBoost
- matplotlib
- joblib
