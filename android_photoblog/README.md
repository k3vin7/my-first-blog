# PhotoBlog Android Source (ch20 참고용)

Android Studio에서 새 프로젝트를 만든 뒤, 이 폴더의 파일을 해당 경로로 복사해서 쓰세요. 이 폴더 자체는 빌드 가능한 완전한 Gradle 프로젝트가 아니라 **소스 파일만** 포함합니다.

## Android Studio 새 프로젝트 설정 (PDF p.4 기준)
- Template: **Empty Views Activity**
- Name: `PhotoBlog`
- Package name: `com.example.photoblog`
- Language: **Java**
- Minimum SDK: **API 33 ("Tiramisu"; Android 13.0)**
- Build configuration language: **Kotlin DSL (build.gradle.kts)**

## 파일 매핑
| 이 폴더 경로 | Android Studio 프로젝트 경로 |
|---|---|
| `app/src/main/AndroidManifest.xml` | `app/src/main/AndroidManifest.xml` |
| `app/src/main/res/layout/activity_main.xml` | `app/src/main/res/layout/activity_main.xml` |
| `app/src/main/java/com/example/photoblog/MainActivity.java` | `app/src/main/java/com/example/photoblog/MainActivity.java` |

## 토큰 교체
`MainActivity.java`의 `Authorization` 헤더 값은 로컬에서 생성한 `admin/test1234` 계정의 DRF 토큰입니다. PythonAnywhere에 배포 후에는 본인 계정의 토큰으로 교체해야 합니다.

토큰 재발급 (서버에서):
```
python manage.py shell -c "
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
u = User.objects.get(username='admin')
token, _ = Token.objects.get_or_create(user=u)
print(token.key)
"
```

## UPLOAD_URL 변경
- **AVD 에뮬레이터 + 로컬 Django**: `http://10.0.2.2:8000/api_root/Post/`
- **PythonAnywhere 배포본**: `https://<username>.pythonanywhere.com/api_root/Post/`
  - 이때 AndroidManifest의 `usesCleartextTraffic="true"`는 그대로 둬도 되고, HTTPS만 쓰면 빼도 됩니다.

## 동작 확인
1. AVD에서 Wi-Fi 연결 (Settings → Network & Internet → Internet → AndroidWifi)
2. 앱 실행 → "Upload Photo" 버튼 클릭
3. 사진/이미지 권한 허용 → 갤러리에서 사진 선택
4. Toast로 "Upload success" 표시되면 성공
5. 브라우저에서 `http://127.0.0.1:8000/` 접속해 새 글이 추가됐는지 확인
